"""Example functions for accessing environmental data.

A package that is created in the course of PARSEC should provide
functionality similar to the examples included here.
The idea is that Computomics can call these functions from xSeedScore
to obtain usable EO data that can be easily integrated
"""

from datetime import date, time
from typing import List, Union, Tuple


def get_env_data(gps_lat: float,
                 gps_lon: float,
                 radius: Union[float, None],
                 start_date: date,
                 end_date: date,
                 measure_points: int,
                 time_of_day: Union[time, None],
                 data_type: str) -> Tuple[List[date], List[float]]:
    """Example function for obtaining environmental data at one location point

    This function provides data types for a specific location identified by one GPS coordinate.
    It should be used if the data type is not dependent on the exact layout of the target region,
    but is measured at one point.
    Example could be the average weekly templerature from the nearest wheather station.
    It returns a list of measurements corresponding to the time range and interval length

    Args:
        gps_lat: GPS latitude
        gps_lon: GPS longitude
        radius: radius in meters around the GPS coordinates to take into account.
            This is only needed for data types that rely on satellite images or similar,
            can be set to None if not applicable
        start_date: Start date of time range
        end_date: End date of time range
        measure_points: Number of measure points to report in the time range defined by
            start_date and end_date. They should be as evenly distributed as possible
        time_of_day: The time of day of the measurements, if applicable, e.g. temperature at 11:00 AM
        data_type: Name of data type to obtain

    Returns:
        Two lists of same length. First has list of date of measurement, second has value

    Raises:
        ConnectionError: If cannot connect to the data source
        ValueError: If argument values are invalid
    """
    

# Get 10 measurements between May 1 and September 10, 2020
#   of the average temperature at 11:00 AM in Tübingen 
(measure_dates, mean_temperatures) = get_env_data(
    48.51616,
    9.06378,
    None,
    date(2020,5,1),
    date(2020,9,10),
    10,
    time(11, 0),
    'mean_temperature'
)
