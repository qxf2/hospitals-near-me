"""
This module will handle logic pertaining to zip codes
"""

from uszipcode import ZipcodeSearchEngine
from geopy.distance import vincenty

def get_nearest_zips(zip_code, radius=20):
    "Return a list of nearest zip codes"
    nearest_zip_codes = []
    search = ZipcodeSearchEngine()
    my_zip = search.by_zipcode(zip_code)
    if my_zip['Latitude'] is not None and my_zip['Longitude'] is not None:
        results = search.by_coordinate(my_zip['Latitude'], my_zip['Longitude'], radius=radius, returns=200)
        for result in results:
            nearest_zip_codes.append(result['Zipcode'])

    return nearest_zip_codes


def get_distance_between_zips(zip1, zip2):
    "Return the distance in miles between two zips"
    search = ZipcodeSearchEngine()
    my_zip1 = search.by_zipcode(zip1)
    loc1 = (my_zip1['Latitude'], my_zip1['Longitude'])
    my_zip2 = search.by_zipcode(zip2)
    loc2 = (my_zip2['Latitude'], my_zip2['Longitude'])

    return vincenty(loc1,loc2).miles
