'''
Copyright: 2020
Author: Raffael Veser
Program for collecting weather data from NASA weather database
'''

# coding: utf-8
import requests
import datetime
import json
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# use this site https://power.larc.nasa.gov/data-access-viewer/ to retrieve parameter names needed in query
# (unfortunately, there is no documentation for the parameters, so you have to retrive them there)

# e.g. TS: Earth skin temperature



def getNasaData(start, end, lat, lon, params=['temp_mean', 'precipitation'], save_to_csv=True):
    '''
    queries NASA database for weather information
    args:
     start, end: start and end dates in the format yyyy-mm-dd
     lat, lon: longitudinal and lateral coordinates
     params: list of parameters which should be obtained. Available parameters are:
             temp_mean, temp_min, temp_max, precipitation, soil_temp, humidity
             DEFAULT: average temperature and precipitation 
     save_as_txt: save  response as csv, default is true

    returns:
     dataframe
    
    '''
    
    # dictionary mapping function parameters to the actual url parameters which are less comprehensible
    # temperature of soil, temp 2 meters above ground average, min and max for each day, precipitation, relative humidity
    param_keys = {'soil_temp': 'TS',
              'temp_mean': 'T2M',
              'temp_min': 'T2M_MIN',
              'temp_max': 'T2M_MAX', 
              'precipitation': 'PRECTOT',
              'humidity': 'RH2M'
    } 



    rows_to_skip = 9 + len(params) # specific for response format
    
    start = start.replace('-', '')
    end = end.replace('-', '')

    param_string = ''
    # replace specified params with actual url params
    for param in params:
        param_string += param_keys[param]
        param_string += ","
    param_string = param_string[:-1]    



    queryUrl = 'https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?request=execute&identifier=SinglePoint'\
    +'&parameters=' + param_string + '&startDate=' + start + '&endDate=' + end\
    + '&userCommunity=AG&tempAverage=DAILY&outputList=CSV&'\
    + 'lat=' + str(lat) + '&lon=' + str(lon) + '&user=anonymous'
    
    response = requests.get(queryUrl)
    try:
        data = response.json()    
        URL = data['outputs']['csv']
        print("Link to dataset", URL)       # result URL
    
    
        # Loading data from the downloaded CSV
        missing_values = [-99,-999]  #this is specific to CSV file format for single location

        df = pd.read_csv(URL,
                  skiprows=rows_to_skip, na_values = missing_values)  # importing taking into account header rows and missing values


        df['Date'] = pd.to_datetime(df['YEAR'] * 1000 + df['DOY'], format="%Y%j")   #recalculating actual date for each observation
        df = df.set_index(df['Date'])                                               #make a date index for weather
        df.drop(columns=['Date'], inplace=True)

        # save dataframe to csv file
        if save_to_csv:
            filename = lat + '-' + lon + '.csv'
            df.to_csv(os.path.dirname(os.path.realpath(__file__)) + "/files/" + filename)


        return df # returns dataframe 
    
    
    except json.decoder.JSONDecodeError:
        print("There is a possible problem with NASA server, check the link https://power.larc.nasa.gov")


def processData(data, num_bins):
    '''
    divides dataset into bins of non-equal size

    args:
     data: Dataframe as returned by getNasaData
     num_bins: number of bins the data should be divided in

    returns:
     map of arrays of aggregated data of length num_bins

    '''
    
    n = len(data)
    # divide data points into logarithmic bins, i.e. the first data points have higher
    # weighting than the later ones
    indices = 10**np.linspace(np.log10(1), np.log10(n), num_bins)

    # change bins to integers without duplicates
    for i in range(1, len(indices)):
    
        if (int(indices[i]) > indices[i-1]):
            indices[i] = int(indices[i])
        else:
            indices[i] = int(indices[i-1]) + 1    


     # sanity check
    if (max(indices) > n):
        raise("invalid number of datapoints")   

    aggregated = {}   
    for col in list(data.columns):
        if (col in ['YEAR','LAT', 'LON', 'DOY']):
            continue
         
        aggregated[col] = []

        # aggregate data in the specified bins
        for i in range(0, len(indices)):
            if (i > 0):
                # average from bin boundary to next bin boundary
                aggregated[col].append(np.mean(data[col][int(indices[i-1]):int(indices[i])]))

            else:
                aggregated[col].append(data[col][0])

    return(aggregated)            


# query some example dates

'''
LAT = '3.85001'
LON = '-59.58999'

start_date = '2019-01-01'
end_date = '2019-12-31'
# temperature of soil, temp 2 meters above ground, precipitation, relative humidity
params = ['soil_temp', 'temp_mean', 'precipitation', 'humidity'] 
df = getNasaData(start_date, end_date, LAT, LON, params, False)
processData(df)
'''