# Amir Daniali
# https://github.com/amirdaniali
# Code The Dream King Cobra
# Week 4

import pandas as pd
import pathlib
from dateutil import parser

BASEDIR = pathlib.Path(__file__).parent
print(BASEDIR)


# Task 1
def task1_1():
    """
    Use a dictionary containing the following data:
        Name: ['Alice', 'Bob', 'Charlie']
        Age: [25, 30, 35]
        City: ['New York', 'Los Angeles', 'Chicago']
    Convert the dictionary into a DataFrame using Pandas.
    Print the DataFrame to verify its creation.
    save the DataFrame in a variable called task1_data_frame and run the tests.
    """
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"],
    }

    data_pd = pd.DataFrame(data)
    return data_pd


task1_data_frame = task1_1()


def task1_2(df: pd.DataFrame) -> pd.DataFrame:
    """
    Make a copy of the dataFrame you created named task1_with_salary (use the copy() method)
    Add a column called Salary with values [70000, 80000, 90000].
    Print the new DataFrame and run the tests.
    """
    new_df = df.copy()
    other = pd.DataFrame({"Salary": [70000, 80000, 90000]})
    # print(other)
    return pd.concat([new_df, other], axis=1)


task1_with_salary = task1_2(task1_data_frame)
print(task1_with_salary)


def task1_3(df: pd.DataFrame) -> pd.DataFrame:
    """
    Make a copy of task1_with_salary in a variable named task1_older
    Increment the Age column by 1 for each entry.
    Print the modified DataFrame to verify the changes and run the tests.

    """
    new_df = df.copy()
    ages = new_df.iloc[:, 1]
    ages = ages + 1
    new_df["Age"] = ages
    return new_df


task1_older = task1_3(task1_with_salary)
print(task1_older)


def task1_4(df: pd.DataFrame):
    """
    Save the task1_older DataFrame to a file named employees.csv using to_csv(), do not include an index in the csv file.
    Look at the contents of the CSV file to see how it's formatted.
    Run the tests.

    """
    # with open(BASEDIR / "employees.csv", "w") as f:
    with open("employees.csv", "w") as f:
        # my project root dir is not python_homework so i needed the Basedir path resolver
        # but then the test wouldnt run because the test is checking assert os.access("./employees.csv", os.F_OK) == True
        # which fails because my ./ is not the parent file directory
        df.to_csv(f, index=False)


task1_4(task1_older)


def task2_1() -> pd.DataFrame:
    """

    Load the CSV file from Task 1 into a new DataFrame saved to a variable task2_employees.
    Print it and run the tests to verify the contents.


    """
    # with open(BASEDIR / "employees.csv", "r") as f:
    with open("employees.csv", "r") as f:
        # my project root dir is not python_homework so i needed the Basedir path resolver
        # but then the test wouldnt run because the test is checking assert os.access("./employees.csv", os.F_OK) == True
        # which fails because my ./ is not the parent file directory
        return pd.read_csv(f)


task2_employees = task2_1()
print(task2_employees)


def task2_2() -> pd.DataFrame:
    """

    Create a JSON file (additional_employees.json). The file adds two new employees. Eve, who is 28, lives in Miami, and has a salary of 60000, and Frank, who is 40, lives in Seattle, and has a salary of 95000.
    Load this JSON file into a new DataFrame and assign it to the variable json_employees.
    Print the DataFrame to verify it loaded correctly and run the tests.


    """
    new_df = pd.DataFrame(
        [
            ["Eve", 28, "Miami", 60000],
            ["Frank", 40, "Seattle", 95000],
        ],
        columns=["Name", "Age", "City", "Salary"],
    )

    with open(BASEDIR / "additional_employees.json", "w") as f:
        # with open("additional_employees.json", "w") as f:
        # my project root dir is not python_homework so i needed the Basedir path resolver
        # but then the test wouldnt run because the test is checking assert os.access("./additional_employees.json", os.F_OK) == True
        # which fails because my ./ is not the parent file directory
        new_df.to_json(f)


task2_2()


def task2_2_load() -> pd.DataFrame:
    """

    Create a JSON file (additional_employees.json). The file adds two new employees. Eve, who is 28, lives in Miami, and has a salary of 60000, and Frank, who is 40, lives in Seattle, and has a salary of 95000.
    Load this JSON file into a new DataFrame and assign it to the variable json_employees.
    Print the DataFrame to verify it loaded correctly and run the tests.


    """

    with open(BASEDIR / "additional_employees.json", "r") as f:
        # with open("./additional_employees.json", "r") as f:
        # my project root dir is not python_homework so i needed the Basedir path resolver
        # but then the test wouldnt run because the test is checking assert os.access("./additional_employees.json", os.F_OK) == True
        # which fails because my ./ is not the parent file directory
        return pd.read_json(f)


json_employees = task2_2_load()
print(json_employees)

csv_employees = task2_employees.copy()
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)


def task3_1(df: pd.DataFrame):
    """

    Use the head() method:

        Assign the first three rows of the more_employees DataFrame to the variable first_three
        Print the variable and run the tests.

    """
    df_head = df.head(3)
    print(df_head)
    return df_head


first_three = task3_1(more_employees)


def task3_2(df: pd.DataFrame):
    """
    Use the tail() method:

        Assign the last two rows of the more_employees DataFrame to the variable last_two
        Print the variable and run the tests.
    """
    df_tail = df.tail(2)
    print(df_tail)
    return df_tail


last_two = task3_2(more_employees)


def task3_3(df: pd.DataFrame):
    """
    Get the shape of a DataFrame

        Assign the shape of the more_employees DataFrame to the variable employee_shape
        Print the variable and run the tests


    """
    return df.shape


employee_shape = task3_3(more_employees)
print(employee_shape)


def task3_4(df: pd.DataFrame):
    """
    Print a concise summary of the DataFrame using the info() method to understand the data types and non-null counts.


    """
    print(df.info())


task3_4(more_employees)


def task4_1():
    """
    Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.
            Print it and run the tests.
            Create a copy of the dirty data in the varialble clean_data (use the copy() method). You will use data cleaning methods to update clean_data.

    """

    return pd.read_csv(BASEDIR / "dirty_data.csv")


dirty_data = task4_1()
print(dirty_data)
clean_data = dirty_data.copy()


def task4_2(df: pd.DataFrame):
    """
    Remove any duplicate rows from the DataFrame
        Print it and run the tests.

    """

    return df.drop_duplicates()


clean_data = task4_2(clean_data)


def task4_3(df: pd.DataFrame):
    """
    Convert Age to numeric and handle missing values
        Print it and run the tests.

    """
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    return df


clean_data = task4_3(clean_data)


def task4_4(df: pd.DataFrame):
    """
    Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
        print it and run the tests.

    """
    df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
    return df


clean_data = task4_4(clean_data)


def task4_5(df: pd.DataFrame):
    """
    Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
        Print it and run the tests

    """

    df.fillna({"Salary": df["Salary"].median()}, inplace=True)
    df.fillna({"Age": df["Age"].median()}, inplace=True)
    return df


clean_data = task4_5(clean_data)
print(clean_data)


def task4_6(df: pd.DataFrame):
    """

    Convert Hire Date to datetime
        Print it and run the tests

    """
    # df["Hire Date"] = pd.to_datetime(df["Hire Date"], errors="coerce")
    df["Hire Date"] = df["Hire Date"].apply(
        lambda x: parser.parse(x, fuzzy=True) if pd.notnull(x) else pd.NaT
    )
    return df


clean_data = task4_6(clean_data)
print(clean_data)


def task4_7(df: pd.DataFrame):
    """

    Strip extra whitespace and standardize Name and Department as uppercase
        Print it and run the tests

    """
    # df["Hire Date"] = pd.to_datetime(df["Hire Date"], errors="coerce")
    df["Name"] = df["Name"].apply(lambda x: x.upper().strip() if pd.notnull(x) else x)
    df["Department"] = df["Department"].apply(
        lambda x: x.upper().strip() if pd.notnull(x) else x
    )
    return df


clean_data = task4_7(clean_data)
print(clean_data)
