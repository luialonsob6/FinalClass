"""
This script will be use to clean the dataframe
"""
import unittest
import os
import pandas as pd
import click


class Cleaningclass:
    """
    Class with functions to clean the dataset
    """

    def __init__(self, df):
        self.df = df

    def erase_duplicates(self):
        """
        Borrar duplicados
        """
        self.df = self.df.drop_duplicates()
        return self.df

    def count_null(self, column):
        """
        Contar valores nulos de una columna
        """
        count = 0
        for i in self.df[column]:
            if pd.isna(i):
                count = count + 1
        return count

    def erase_columns(self, column):
        """
        Borrar aquellas columnas que tengan mas de un 30% de valores nulos
        """
        count = self.count_null(column)
        if count > (len(self.df) * 0.3):
            del self.df[column]
        else:
            pass

    def cleaning_columns(self):
        """
        Aplicar las funciones de cleaning a todas las columnas
        """
        for column in self.df.columns:
            self.erase_columns(column)
        return self.df


def load_dataset(filename):
    """
    Function to load dataset
    """
    extension = filename.rsplit(".", 1)[-1]
    if extension == "csv":
        return pd.read_csv(filename)
    else:
        raise TypeError(
            f"The extension is {extension} and not csv, try again"
        )  # Hacemos un raise del error(lo mismo que en el try and except)


@click.command(short_help="parser to import dataset")
@click.option("-i", "--input_file", required=True, help="File to import")
@click.option("-o", "--output", help="File to import")
def main(input_file, output):
    """
    Main Function
    """
    dataset_dir = "dataset"
    file_path = os.path.join(dataset_dir, input_file)

    df = load_dataset(file_path)
    print(df.shape)

    df = Cleaningclass(df).cleaning_columns()
    df = Cleaningclass(df).erase_duplicates()

    print(df.head())
    print(df.info())
    print(df.shape)

    if output:
        output_path = os.path.join("dataset", output)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        output_file = os.path.join(output_path, "cleaned_df.csv")
    else:
        output_file = "dataset/cleaned_df.csv"

    df.to_csv(output_file, index= None)


if __name__ == "__main__":
    unittest.main()
