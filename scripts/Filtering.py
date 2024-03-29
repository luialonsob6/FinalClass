"""
Script to make filter of the dataset
"""
import unittest
import os
import pandas as pd
import click


class Filterdata:
    """
    Define class with filter functions
    """

    def __init__(self, df):
        self.df = df

    def filter_neighbourhood(self, neighbourhood):
        """
        filter by neighbourhood
        """
        return self.df[self.df["neighbourhood_group"] == neighbourhood]

    def filter_type(self, room):
        """
        Filter by room type
        """
        return self.df[self.df["room_type"] == room]

    def filter_price(self, price):
        """
        Filter by higher revenue than mean
        """
        return self.df[self.df["price"] < price]

    def filter_min_nights(self, nights):
        """
        Filter by minimum nights
        """
        return self.df[self.df["minimum_nights"] < nights]

    def filter_availability(self, availability):
        """
        Filter by the days available
        """
        return self.df[self.df["availability_365"] >= availability]


@click.command(short_help="parser to import dataset")
@click.option("-i", "--insert", required=True, help="Path to my Input Dataset")
@click.option("-o", "--output", help="Where to store the filtered dataset")
@click.option("-f", "--filtering", is_flag=True, help="Set a filtering or not")
@click.option("-n", "--neighbourhood", help="Neighbour filter")
@click.option("-p", "--price", help="Price filter")
@click.option("-r", "--room", help="Room type to filter")
@click.option("-ni", "--nights", help="Minimum nights")
@click.option("-a", "--availability", help="Available filter")
def main(insert, output, filtering, room, neighbourhood, price, nights, availability):
    """
    Start functions
    """

    df = pd.read_csv(insert)

    print(df.shape)
    print(df.info())

    if filtering:
        print("Im going to filter")
        df = Filterdata(df).filter_neighbourhood(neighbourhood)
        df = Filterdata(df).filter_type(room)
        df = Filterdata(df).filter_price(price)
        df = Filterdata(df).filter_min_nights(nights)
        df = Filterdata(df).filter_availability(availability)

        print(df.shape)
        print(df.head())

    if not os.path.exists(output):
        os.makedirs(output)

    df.to_csv("outputs/filtered_df.csv", index=None)


if __name__ == "__main__":
    unittest.main()
