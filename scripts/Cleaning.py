"""
This script will be use to clean the dataframe
"""
import unittest
import pandas as pd

class Cleaning:
    """
    Class with functions to clean the dataset
    """
    def __init__(self, df):
        self.df = df

    def erase_duplicates(self):
        self.df.drop_duplicates()
        return self.df
    
    def count_NaN(self, column):
        count = 0
        for i in self.df[column]:
            if pd.isna(i):
                count = count +1
        return count
    
    def erase_columns(self, column):
        count = count_NaN(self,column)
        if count > 1000:
            del self.df[column]
        else:
            pass

    def cleaning_columns(self):
        for column in self.df.columns:
            erase_columns(self,column)






if __name__ == "__main__":
    unittest.main()
