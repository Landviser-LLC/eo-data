# Description of EO Data access scripts / protocols
To work with this repo, please, setup Virtual environment with Python 3.8. Then
~~~
pip install -r requirements.txt
~~~

## Test Data Set - US Corn trials 2015-2016
**data** folder [locations CSV](\data\location_table.csv)

## Weather

NASA POWER per point data historical downloads: two Jupyther notebooks available in **weather** folder. data are on 0.5 x 0.5 decimal degree grid daily from 


## Soils
Soil properties dataset was pulled from HWSD GRIB grid and MS Access data set for the test locations, the detailed report 


## Copernicus.eu EO services
Data on weather with better resolution than previously used from NASA is availble. In additional, gridded temporal information is availble for soil moisture and derived agricultural variables from climate and satellite (Sentenial and Landsat). As I explore those data datasets/python tools, I put them into **copernicus** folder in this repo.
See the detailed README file about datasets in that folder.


## rasdaman

Rasdaman provides Marketplace (Mundi) for geospatial data (mostly rasters - imagery). They also provide access to the Copernicus data store - have to figure out what is the advantage of going through them instead of using downloads from Copernicus Data Store or Copernicus Toolbox directly, hence meeting on Monday, Feb 1st.
Description of how to access satellite imagery data using Jupyter notebook is available at https://tutorial.rasdaman.org/rasdapy-tutorial/ 
That tutorial notebook has been downloaded into *rasdaman* folder in this repo

**What do I need before using rasdapy?**

A running rasdaman instance, see: http://rasdaman.org/wiki/Download.
A general idea about what is rasdaman and how it works (recommended for begginers), see: http://tutorial.rasdaman.org/rasdaman-and-ogc-ws-tutorial/