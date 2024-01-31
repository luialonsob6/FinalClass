import unittest
import pandas as pd
from Data_analysis import DataAnalyzer

class TestDataAnalyzer(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv("Airbnb_NYC.csv")

    def test_summary_statistics(self):
        analyzer = DataAnalyzer(self.df)
        summary_stats = analyzer.summary_statistics()
        self.assertIsInstance(summary_stats, pd.DataFrame)
        self.assertEqual(len(summary_stats), len(self.df.describe()))

    def test_unique_values(self):
        analyzer = DataAnalyzer(self.df)
        unique_vals = analyzer.unique_values()
        self.assertIsInstance(unique_vals, dict)
        self.assertEqual(len(unique_vals), len(self.df.columns))

    def test_missing_values(self):
        analyzer = DataAnalyzer(self.df)
        missing_vals = analyzer.missing_values()
        self.assertIsInstance(missing_vals, pd.Series)
        self.assertEqual(len(missing_vals), len(self.df.columns))

    def test_correlation_matrix(self):
        analyzer = DataAnalyzer(self.df)
        correlation_matrix = analyzer.correlation_matrix()
        self.assertIsInstance(correlation_matrix, pd.DataFrame)
        self.assertEqual(correlation_matrix.shape[0], correlation_matrix.shape[1])
        self.assertEqual(len(correlation_matrix.columns), len(self.df.select_dtypes(include='number').columns))

if __name__ == "__main__":
    unittest.main()