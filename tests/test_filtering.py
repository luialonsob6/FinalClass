"""
Test for filtering fucntions
"""
import unittest
import pandas as pd
from filtering import Filterdata


class TestFilterdataMethods(unittest.TestCase):
    """
    Clase para testear las funciones de filering
    """

    def setUp(self):
        """
        Creamos un dataframe nuevo para hacer los tests
        """
        data = {
            "neighbourhood_group": ["A", "B", "A", "B", "A"],
            "room_type": [
                "Entire home/apt",
                "Private room",
                "Entire home/apt",
                "Private room",
                "Entire home/apt",
            ],
            "price": [100, 200, 150, 250, 180],
            "minimum_nights": [1, 2, 3, 4, 5],
            "availability_365": [100, 200, 300, 400, 500],
        }
        self.df = pd.DataFrame(data)
        self.filter = Filterdata(self.df.copy())

    def test_filter_neighbourhood(self):
        """
        Test para la función de barrio
        """
        filtered_df = self.filter.filter_neighbourhood("A")
        self.assertEqual(len(filtered_df), 3)

    def test_filter_type(self):
        """
        Test para la función de tipo habitación
        """
        filtered_df = self.filter.filter_type("Private room")
        self.assertEqual(
            len(filtered_df), 2)

    def test_filter_higher_mean(self):
        """
        Test para la función de precio
        """
        filtered_df = self.filter.filter_higher_mean()
        self.assertEqual(len(filtered_df), 3)

    def test_filter_min_nights(self):
        """
        Test para la función de noches minimas
        """
        filtered_df = self.filter.filter_min_nights(3)
        self.assertEqual(len(filtered_df), 3)

    def test_filter_availability(self):
        """
        Test para la función de disponibilidad
        """
        filtered_df = self.filter.filter_availability(300)
        self.assertEqual(len(filtered_df), 3) 


if __name__ == "__main__":
    unittest.main()
