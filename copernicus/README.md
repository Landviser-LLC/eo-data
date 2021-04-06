# Copernicus Data Store

Climate historical grids and combination parameters available. Anybody can create an account to download data from Copernicus Climate Data store, although training and familiarity with special geographical software is needed. There is also CDS-remote Python package - exploring https://pypi.org/project/cdstoolbox-remote/
~~~
pip install cdstoolbox-remote
~~~
**Configure**
If you are not already registered to the CDS, register here:

https://cds.climate.copernicus.eu/user/register

then log in the CDS and configure the cdsapi library following the instructions at:

https://cds.climate.copernicus.eu/api-how-to

## Soil moisture grid for top-soil

The link to data set - select period and location - submit request for download. Also creates an API call - example for 2015-2016 - daily for the months April-September - for our test dataset. It prepares a download in the user profile, and then ZIP file needs to be downloaded. a global grid of soil moisture for the dates described above is ~770 Mb.
~~~
import cdsapi

c = cdsapi.Client()

c.retrieve(
    'satellite-soil-moisture',
    {
        'format': 'zip',
        'variable': 'volumetric_surface_soil_moisture',
        'type_of_sensor': 'combined_passive_and_active',
        'time_aggregation': 'day_average',
        'year': [
            '2015', '2016',
        ],
        'month': [
            '04', '05', '06',
            '07', '08', '09',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'type_of_record': 'cdr',
        'version': 'v201912.0.0',
    },
    'download.zip')
    ~~~