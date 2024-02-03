"""
Script para mostrar los resultados que se adaptan a las exigencias del cliente.
"""
import pandas as pd

df = pd.read_csv("outputs/filtered_df.csv")

df.shape()
df.head()

if __name__ == "__main__":
    pass