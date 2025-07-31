# # Amir Daniali
# https://github.com/amirdaniali
# Code The Dream King Cobra
# Week 3

# Task 5
import pandas as pd
from pathlib import Path


class DFPlus(pd.DataFrame):
    """
        Within the assignment3 folder, create a file called print-dataframe-with-headers.py.
        Create a class called DFPlus. It should inherit from the Pandas DataFrame class. You are going to add a single method to the class. You do not need an __init__ method, because you are going to use the one already provided.
        You want to create a DFPlus instance by reading in ../csv/products.csv. Now we have a problem. pd.read_csv() creates a DataFrame, not a DFPlus. So here's the sneak path. This creates a from_csv class method so that you can do dfp = DFPlus.from_csv("../csv/products.csv")

    class DFPlus(pd.DataFrame):
        @property
        def _constructor(self):
            return DFPlus

        @classmethod
        def from_csv(cls, filepath, **kwargs):
            df = pd.read_csv(filepath, **kwargs)
            return cls(df)

        Within the DFPlus class, declare a function called print_with_headers(). It only takes one argument, self. When you print a big DataFrame, you can't see the column headers because they scroll up. This function will provide a way to print the DataFrame giving column headers every 10 lines. The function will print the whole DataFrame in a loop, printing 10 rows at a time.
        Well, how to do this? You need to know the length of the DataFrame. That's easy: len(self). Now, how do you get a given 10 rows? That's easy too. You have access to super().iloc so you can specify the ten line slice you want. And then you just print what you get back, looping until you get to the bottom.
        Using the from_csv() class method, create a DFPlus instance from "../csv/products.csv".
        Use the print_with_headers() method of your DFPlus instance to print the DataFrame.
    """

    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        for index in range(0, len(self), 10):
            rows = super().iloc[index : index + 10, :]
            print(rows)


df = DFPlus.from_csv(
    Path(__file__).resolve().parent.parent / "csv/products.csv",
    header=0,
    names=["id", "name", "price"],
)
df.print_with_headers()
