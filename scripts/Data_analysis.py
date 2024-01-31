"""
Script to analyze the datframe
"""
import unittest
import pandas as pd

df = "Airbnb_NYC.csv"

class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def summary_statistics(self):
        """
        Generate summary statistics for numerical columns
        """
        return self.df.describe()

    def unique_values(self):
        """
        Get unique values for each column
        """
        unique_vals = {}
        for col in self.df.columns:
            unique_vals[col] = self.df[col].unique()
        return unique_vals

    def missing_values(self):
        """
        Count missing values in each column
        """
        return self.df.isnull().sum()

    def correlation_matrix(self):
        """
        Calculate the correlation matrix for numerical columns
        """
        return self.df.corr()




summary_stats = df.summary_statistics()
print("Summary Statistics:")
print(summary_stats)


unique_vals = df.unique_values()
print("\nUnique Values:")
print(unique_vals)


missing_vals = df.missing_values()
print("\nMissing Values:")
print(missing_vals)


correlation_matrix = df.correlation_matrix()
print("\nCorrelation Matrix:")
print(correlation_matrix)
        


if __name__ == "__main__":
    unittest.main()












































if __name__ == "__main__":
    unittest.main()