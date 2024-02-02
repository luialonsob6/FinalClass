"""
Functions to test the cleaning scripts
"""
import unittest
import pandas as pd
from scripts.cleaning import Cleaningclass


class TestCleaningMethods(unittest.TestCase):
    """
    Clase para testear las funciones de cleaning
    """

    def setUp(self):
        """
        Creamos un dataframe nuevo para hacer los tests
        """
        data = {
            "A": [1, 2, 3, 3, 4],
            "B": [5, pd.NA, pd.NA, 8, pd.NA],
            "C": [pd.NA, 7, pd.NA, pd.NA, 9],
        }
        self.df = pd.DataFrame(data)
        self.cleaning = Cleaningclass(self.df.copy())

    def test_erase_duplicates(self):
        """
        Test función duplicados
        """
        cleaned_df = self.cleaning.erase_duplicates()
        self.assertEqual(len(cleaned_df), len(self.df.drop_duplicates()))

    def test_count_null(self):
        """
        Test función nulos
        """
        nan_count = self.cleaning.count_null("B")
        self.assertEqual(nan_count, 3)

    def test_cleaning_columns(self):
        """
        Test función limpiar todas las columnas
        """
        cleaned_df = self.cleaning.cleaning_columns()
        self.assertNotIn("B", cleaned_df.columns)


if __name__ == "__main__":
    unittest.main()
