"""
Script to analyze the datframe
"""
import unittest
import pandas as pd
import click
import matplotlib.pyplot as plt
import seaborn as sns


class DataAnalyzer:
    """
    Clase con las funciones para realizar el data analysis
    """

    def __init__(self, df):
        self.df = df

    def describe_df(self):
        """
        A summary of the numeric columns
        """
        return self.df.describe()

    def value_counting(self, column):
        """
        Get unique values for each column
        """

        return self.df[column].value_counts()

    def hist_column(self, column):
        """
        Plot a histogram of a certain column
        """
        self.df[column].hist()
        return plt.gcf()

    def boxplot_column(self, column):
        """
        Plot a boxplot of a certain column
        """
        sns.boxplot(x=column, data=self.df)
        return plt.gcf()

    def correlation_matrix(self):
        """
        The correlation between
        """
        numeric_columns = self.df.select_dtypes(include=["int", "float"])
        correlation_matrix = numeric_columns.corr()
        fig = plt.figure()
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
        return fig

    def mean_price_neighbourhood(self):
        """
        Muestra cual es el precio medio por barrio
        """
        precio_barrio = self.df.groupby("neighbourhood_group")["price"].mean()

        precio_barrio.plot(kind="bar")
        plt.xlabel("Barrio")
        plt.ylabel("Precio medio")
        plt.title("Precio medio por barrio")

        return plt.gcf()


@click.command(short_help="parser to import dataset")
@click.option("-i", "--insert", required=True, help="Path to my Input Dataset")
@click.option("-c", "--column", required=True, help="Column value counts")
def main(insert, column):
    """
    Data analysis functions
    """
    df = pd.read_csv(insert)

    print("Describe:")
    print(df.describe_df())

    print("\nValue Counts:")
    print(df.value_counting(column))

    print("\nMHistogram:")
    print(df.hist_column(column))

    print("\nBoxplot:")
    print(df.boxplot_column(column))

    print("\nCorrelation Matrix:")
    print(df.correlation_matrix())

    print("\nMean price:")
    print(df.mean_price_neighbourhood())


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
