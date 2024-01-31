"""
Tests for the cleaning script
"""
import unittest
import pandas as pd
from Cleaning import Cleaning

class TestCleaning(unittest.TestCase):
    def setUp(self):
        data = {
            "col1": [1, 2, 3, 4, 5],
            "col2": [6, 7, pd.NA, 9, 10],  
            "col3": ["A", "B", "C", "D", "E"]
        }
        self.df = pd.DataFrame(data)

    def test_erase_duplicates(self):
        cleaning_obj = Cleaning(self.df)
        cleaned_df = cleaning_obj.erase_duplicates()
        self.assertEqual(len(cleaned_df), len(self.df.drop_duplicates()))  

    def test_count_NaN(self):
        cleaning_obj = Cleaning(self.df)
        nan_count = cleaning_obj.count_NaN("col2")
        self.assertEqual(nan_count, 1)  

    def test_erase_columns(self):
        cleaning_obj = Cleaning(self.df)
        cleaning_obj.erase_columns("col2")
        self.assertNotIn("col2", cleaning_obj.df.columns) 

    def test_cleaning_columns(self):
        cleaning_obj = Cleaning(self.df)
        cleaning_obj.cleaning_columns()
        self.assertNotIn("col2", cleaning_obj.df.columns)  
        
if __name__ == "__main__":
    unittest.main()