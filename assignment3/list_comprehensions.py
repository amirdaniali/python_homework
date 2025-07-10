# # Amir Daniali
# https://github.com/amirdaniali
# Code The Dream King Cobra
# Week 3

# Task 3

import pandas as pd
from pathlib import Path


def read_employees() -> dict[list[str]]:
    """
    Within the assignment3 folder, create a file called list-comprehensions.py. Add code that reads the contents of ../csv/employees.csv into a DataFrame.
    Using a list comprehension, create a list of the employee names, first_name + space + last_name. The list comprehension should iterate through the rows of the DataFrame. Print the resulting list. Hint: If df is your dataframe, df.iterrows() gives an iterable list of rows. Each row is a tuple, where the first element of the tuple is the index, and the second element is a dict with the key/value pairs from the row.
    Using a list comprehension, create another list from the previous list of names. This list should include only those names that contain the letter "e". Print this list.

    """
    df = pd.read_csv(
        Path(__file__).resolve().parent.parent / "csv/employees.csv",
        header=0,
        names=["id", "first", "last", "phone"],
    )
    employees = [
        f"{employee['first']} {employee['last']}"
        for index, employee in df.iloc[:, [1, 2]].iterrows()
    ]
    employees_e = [
        employee for employee in employees if employee.count("e")
    ]  # counts of zero are ignored
    print(employees_e)


employees = read_employees()
