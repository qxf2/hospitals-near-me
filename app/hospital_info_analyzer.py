"""
This module will handle logic pertaining to hfiltering ospital data
"""
import os
import numpy as np
import pandas as pd

class Hospital_Data:
    "A class to analyze hospital data"

    def __init__(self):
        "Read the hospital info"
        self.data = ''
        csv = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', 'data', 'HospInfo.csv'))
        self.read_csv(csv)

    def read_csv(self, csv):
        "Read a given csv and store it in a dataframe"
        self.data = pd.read_csv(csv)
        self.data['ZIP Code'] = self.data['ZIP Code'].astype(str)
        return self.data

    def filter_data_by_zipcode(self,zipcodes=[]):
        "Filter data based on a list of zipcodes"
        return self.data[self.data['ZIP Code'].isin(zipcodes)]



#----START OF SCRIPT
if __name__=='__main__':
    my_obj = Hospital_Data()
    print my_obj.filter_data_by_zipcode(zipcodes=['22181', '13210', '22210'])[['Hospital Name', 'Hospital overall rating', 'ZIP Code']]
