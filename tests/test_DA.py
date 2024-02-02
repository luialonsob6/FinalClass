"""
Functions to test the data analysis script
"""
import unittest
import pandas as pd
from matplotlib.figure import Figure
from scripts.data_analysis import DataAnalyzer


class TestDataAnalyzer(unittest.TestCase):
    """
    Clase para testear las funciones de data analysis
    """

    def setUp(self):
        """
        Creamos un dataframe nuevo para hacer los tests
        """
        data = {
            "columna1": [1, 2, 3, 4, 5],
            "columna2": [5, 6, 7, 8, 9],
            "neighbourhood_group": ["A", "B", "A", "B", "A"],
            "price": [100, 200, 150, 250, 180],
        }
        self.df = pd.DataFrame(data)
        self.analyzer = DataAnalyzer(self.df.copy())

    def test_describe_df(self):
        """
        Test para la función describe
        """
        description = self.analyzer.describe_df()
        self.assertEqual(description.shape, (8, 3))

    def test_value_counting(self):
        """
        Test para la función de contar valores
        """
        value_counts = self.analyzer.value_counting("neighbourhood_group")
        self.assertEqual(value_counts["A"], 3)

    def test_hist_column(self):
        """
        Test para la función de crear un histograma
        """
        hist_plot = self.analyzer.hist_column("price")
        self.assertIsInstance(hist_plot, Figure)

    def test_boxplot_column(self):
        """
        Test para la función de crear un boxplot
        """
        boxplot_plot = self.analyzer.boxplot_column("price")
        self.assertIsInstance(boxplot_plot, Figure)

    def test_mean_price_neighbourhood(self):
        """
        Test para la funcion de precio medio
        """
        mean_price_plot = self.analyzer.mean_price_neighbourhood()
        self.assertIsInstance(mean_price_plot, Figure)


if __name__ == "__main__":
    unittest.main()
