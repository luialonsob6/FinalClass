"""
Tests for the filtering script
"""
import unittest
import pandas as pd
from Filtering import Filterdata

class TestFilterData(unittest.TestCase):
    def setUp(self):
        data = {
            "neighbourhood_group": ["A", "B", "A", "C", "B"],
            "Year": ["type1", "type2", "type1", "type1", "type2"],
            "price": [100, 200, 150, 180, 220],
            "minimum_nights": [2, 3, 1, 2, 4],
            "availability_365": [100, 200, 150, 180, 220]
        }
        self.df = pd.DataFrame(data)

    def test_filter_neighbourhood(self):
        filter_obj = Filterdata(self.df)
        filtered_df = filter_obj.filter_neighbourhood("A")
        self.assertEqual(filtered_df.shape[0], 2)  
    def test_filter_type(self):
        filter_obj = Filterdata(self.df)
        filtered_df = filter_obj.filter_type("type1")
        self.assertEqual(filtered_df.shape[0], 3)  

    def test_filter_higher_mean(self):
        filter_obj = Filterdata(self.df)
        filtered_df = filter_obj.filter_higher_mean()
        self.assertEqual(filtered_df.shape[0], 2)  

    def test_filter_min_nights(self):
        filter_obj = Filterdata(self.df)
        filtered_df = filter_obj.filter_min_nights(3)
        self.assertEqual(filtered_df.shape[0], 2)  
    def test_filter_availability(self):
        filter_obj = Filterdata(self.df)
        filtered_df = filter_obj.filter_availability(150)
        self.assertEqual(filtered_df.shape[0], 3)  

if __name__ == "__main__":
    unittest.main()