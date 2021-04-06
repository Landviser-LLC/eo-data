'''
Pre-processing functions to standartize geographical Latitude/Longitude.
Strictly mathematical/geographical/astronomical functions to recalculate location coordinates and some EO data (day light length)
'''

# define formulafunction for decimal degree recalculation
def decdegree(d, m, s, go):
    '''
    recalculates the geographical latitude/longitude to standard decimal degrees from Degree (d, integer), Minute (m, integer), Second (s, float)
    and given direction (go, only four valid strings ['N', 'S', 'E', 'W'])
    examples:
    Latitude = round(decdegree(11,5,9.9, "S"), 2)
    Longitude = round(decdegree(49,43,2.7, "W"), 2)

    Latitude = round(decdegree(31,22,60, "S"), 2)
    Longitude = round(decdegree(57,58,0, "W"), 2)
    print(str(Latitude) +', '+ str(Longitude))  
    '''
    directions = ['N', 'S', 'E', 'W']
    if go not in directions:
        return print("wrong 'go' parameter, only S, N, W, E strings are accepted")
    else:
        dd = d + m/60 + s/3600
        if go == 'N' or go == 'E':
            return dd
        else:
            return -dd


# pre-processing function to standartize locations to middle of half-decimal degree lat/long grid

def grid05(latlong):
    '''
    to  standartized grid of input Latitude or Longitude (float, in decimal degrees)
    (f.e. NOAA POWER data set pulls the same historical data for data placed in the .5 decimal degrees)
    i.e. each 1 decimal degree lat/long cell on Earth is split into four sub-cells with center points at 
       (0.25, 0.25) (0.25, 0.75)
       (0.75, 0.25) (0.75, 0.75)
    '''
    if latlong <= (floor(latlong + 0.5)):
        grdstandard =  floor(latlong)+0.25 
    else:
        gridstandard =  floor(latlong)+0.75

    return gridstandard

# formula for calculating daylength from the location latitude and day of the year (1-365)

def daylight(latitude, doy):
    '''
    only two parameters for any location on earth, Latitude in Decimal Degrees and DOY - day of the year (1-365)
    example:
    print(Daylight(-29, 1))         # daylight hours in  example location in South America on Jan 1st
    '''

    P = math.asin(0.39795 * math.cos(0.2163108 + 2 *
                                     math.atan(0.9671396 * math.tan(.00860 * (doy - 186)))))
    pi = math.pi
    
    daylightamount = 24 - (24 / pi) * math.acos((math.sin((0.8333 * pi / 180)
                                                          + math.sin(latitude * pi / 180) * math.sin(P)) / (math.cos(latitude * pi / 180) * math.cos(P))))
    return daylightamount

