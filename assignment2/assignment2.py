# Amir Daniali
# https://github.com/amirdaniali
# Code The Dream King Cobra
# Week 2

import csv
import traceback
import os
from datetime import datetime

import custom_module


# Task 2
def read_employees() -> dict[list[str]]:
    """This task, and the others that follow below, use the same pattern as for assignment1. This pattern is known as Test Driven Development (TDD).  It is a good practice which is often used in software industry.  You will need to create assignment2.py for the rest of the tasks.  Then type the following command:

    pytest -v -x assignment2-test.py

    This will give errors to report what you need to fix.  You run it repeatedly as you create the following functions, until all functions are working correctly.

    Remember to import the csv module for this task.

        Create a function called read_employees that has no arguments, and do the following within it.
            Declare an empty dict. You'll add the key/value pairs to that. Declare also an empty list to store the rows.
            You next read a csv file. Use a try block and a with statement, so that your code is robust and so that the file gets closed.
            Read ../csv/employees.csv using csv.reader(). (This csv file is used in a later lesson to populate a database.)
            As you loop through the rows, store the first row in the dict using the key "fields". These are the column headers.
            Add all the other rows (not the first) to your rows list.
            Add the list of rows (this is a list of lists) to the dict, using the key "rows".
            The function should return the dict.
            Add a line below the function that calls read_employees and stores the returned value in a global variable called employees. Then print out this value, to verify that the function works.
            In this case, it's not clear what to do if you get an exception. You might get an exception because the filename is bad, or because the file couldn't be parsed as a CSV file. For now, just use the same approach as described above: catch the exception, print out the information, and exit the program. One likely exception in this case is an error in the syntax of your code.

        Run the test to see if you have this much right.

    A word about what's going on when the test runs: The test file imports your assignment2.py module.  When the import statement occurs, all the program statements in your module that are outside of functions do run.  That means the statement which sets your employees global variable is run.  As a result, the assignment2-test.py can reference this global variable too -- and it does.  If you forget to set this variable in your program, the test reports an error.
    """
    employess = {}
    rows = []
    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            first_line = next(reader)
            employess["fields"] = first_line

            for row in reader:
                rows.append(row)

            employess["rows"] = rows
            return employess
    except Exception as e:
        trace_back: traceback.StackSummary = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


employees = read_employees()


# Task 3
def column_index(string: str) -> int:
    """
        Create a function called column_index. The input is a string. The function looks in employees["fields"] (an array of column headers) to find the index of the column header requested. There won't be much to this function, because you just use the index() method of the list class, like so:

    employees["fields"].index("first_name")

    The index() method returns the index of the matching value from the list.

        The column_index function should return this index.

        Run the test again to see if the test passes.

        Call the column_index function in your program, passing the parameter "employee_id".  Store the column you get back in a variable called employee_id_column.  This global value is used for subsequent steps.
    """
    return employees["fields"].index(string)


# Task 4
def first_name(row_number: int) -> str:
    """

    Create a function called first_name.  It takes one argument, the row number.  The function should retrieve the value of first_name from a row as stored in the employees dict.

    You should first call your column_index function to find out what column index you want.

    Then you go to the requested row as stored in the employees dict, and get the value at that index in the row.

    Return the value.

    Try the test again.
    """
    name_index: int = column_index("first_name")
    return employees["rows"][row_number][name_index]


employee_id_column = column_index("employee_id")
print(employees)


# Task 5
def employee_find(employee_id: int) -> list:
    """



        Create a function called employee_find.  This is passed one argument, an integer.  Just call it employee_id in your function declaration. We want it to return the rows with the matching employee_id.  There should only be one, but sometimes a CSV file has bad data.

        We could do this with a loop.  But we are going to use the filter() function.  Inside the employee_find function (yes, you do declare functions inside functions sometimes), create the following employee_match function:

    def employee_match(row):
       return int(row[employee_id_column]) == employee_id

    This function is referencing the employee_id value that is passed to the employee_find function.  It can access that value because the employee_match function is inside the employee_find function.  Note that we need to do type conversion here, because the CSV reader just returns strings as the values in the roows.  This inner function returns True if there is a match.  We are using the employee_id_column global value you set in Task 3.

        Now, still within the employee_find function, call the filter() function. This is another one of those Python free standing functions. (It is not a method of the list class.) You call filter() as follows:

    matches=list(filter(employee_match, employees["rows"]))

    The filter() function needs to know how to filter, and the employee_match function provides that information.  The filter() function calls employee_match once per row, saying, Do we want this one?  When the filter function completes, we need to do type conversion to convert the result to a list.

        The employee_find function then returns the matches.

        Run the test and see if you got it right.


    """

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


# Task 6
def employee_find_2(employee_id: int) -> list:
    """
    The employee_match function is a silly one-liner.  Lambdas allow us to give the logic inline.

        Create a function employee_find_2. This function does exactly what employee_find does -- but it uses a lambda.

    def employee_find_2(employee_id): matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"])) return matches

    Note that there is no return statement in the lambda.  There is the parameter passed to the lambda (a row), followed by a colon, followed by the expression that gives the result.

        Run the test to make sure things still work.

    """

    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]
        )
    )
    return matches


# Task 7
def sort_by_last_name():
    """We want to call the sort() method on the rows.  However, we need to tell it which column to use for the sort.

    Create a function sort_by_last_name.  It takes no parameters.  You sort the rows you have stored in the dict.

    Within the function, you call employees["rows"].sort().  This sorts the list of rows in place. But, you need pass to the list.sort() method a keyword argument called key (so you pass a parameter with key= when you call it).  You set that keyword parameter equal to a lambda.  The lambda is passed the row, and the expression after the colon gives the value from the row to be used in the sort.  You might want to use your column_index function for last_name so you know which value from the row should be given in the lambda expression.  Remember that the sort() method sorts the list in place and does not return the sorted list.

    The sort_by_last_name function returns the sorted list of rows.

    Run the test until this works.

    Call the function in your program, and then print out the employees dict, to see it in sorted form.
    """

    employees["rows"].sort(key=lambda row: row[column_index("last_name")])

    return employees["rows"]


sort_by_last_name()
print("\n\n", employees)


# Task 8
def employee_dict(row):
    """

        Create a function called employee_dict.  It is passed a row from the employees dict (not a row number).  It returns a dict.
            The keys in the dict are the column headers from employees["fields"].
            The values in the dict are the corresponding values from the row.
            Do not include the employee_id in the dict. You skip that field for now.

        Return the resulting dict for the employee.

        Add a line to your program that calls this function and prints the result.  Use a row from the rows stored in the employees dict to pass to the function for this test.

        Get the test working.

    If you want to try something extra, look up the zip() function, which can be used to simplify the code for this problem.
    """
    employee = {}
    for index, column in enumerate(employees["fields"]):
        if column == "employee_id":
            continue
        employee[column] = row[index]

    return employee

    # Alternatively we can use the zip function
    return {x: y for x, y in zip(employees["fields"], row) if x != "employee_id"}


test_employee2 = employees["rows"][1]
print("\n\n", employee_dict(test_employee2))


# Task 9
def all_employees_dict():
    """

    Create a function called all_employees_dict.
        The keys in the dict are the employee_id values from the rows in the employees dict.
        For each key, the value is the employee dict created for that row. (Use the employee_dict function you created in task 8.)

    The function should return the resulting dict of dicts.

    Add a line to your program that calls this function and prints the result.

    Get the test working.
    """
    return {row[employee_id_column]: employee_dict(row) for row in employees["rows"]}


employees_dict = all_employees_dict()
print("\n\n", employees_dict)


# Task 10


def get_this_value():
    """Sometimes the behavior of a program is to be modified without changing the program itself.  One way is to use environment variables.  Environment variables are also used to store secrets needed by the program, such as passwords.  Environment variables are accessed via the os.getenv() function.  Of course, there are many other functions in the os package.

    Within the terminal, enter the command export THISVALUE=ABC.

    Add a line to assignment2.py to import the os module.

    Create a function get_this_value().  This function takes no parameters and returns the value of the environment variable THISVALUE.

    Get the test working.  (Note that each time you want this test to pass, you have to have the THISVALUE environment variable set in your terminal session.)
    """
    return os.getenv("THISVALUE")


print(get_this_value())


# Task 11
def set_that_secret(new_secret):
    """
        In the same folder, create a file called custom_module.py, with the following contents:

    secret = "shazam!"

    def set_secret(new_secret):
       global secret
       secret = new_secret

        Add the line import custom_module to assignment2.py.

        Create a function called set_that_secret.  It should accept one parameter, which is the new secret to be set.  It should call custom_module.set_secret(), passing the parameter, so as to set the secret in custom_module.

        Add a line to your program to call set_that_secret, passing the new string of your choice.

        In another line, print out custom_module.secret.  Verify that it has the value you expect.

        Run the test until the next part passes.
    """
    custom_module.set_secret(new_secret)


set_that_secret("hidden_secret_5")
print(custom_module.secret)


# Task 12
def read_minutes():
    """The "story" behind the following list of tasks is as follows.  A club meets, and for each meeting, there is a chairperson.  The club keeps several notebooks that record who whas the chairperson on a given date.  Some of the information is in one notebook, some in the other.  The club now wants to combine this information, to get the list of chairpersons sorted by date.  But the information in the csv files contains duplicates and is in no particular order.  (Yeah, the story is lame, but it is similar to other data analysis tasks.)

    Create a function called read_minutes.  It takes no parameters.  It creates two dicts, minutes1 and minutes2, by reading ../csv/minutes1.csv and ../csv/minutes2.csv.  Each dict has fields and rows, just as the employees dict had.  However! As you create the list of rows for both minutes1 and minutes2, convert each row to a tuple.  The function should return both minutes1 and minutes2.  Note You can return several values from a Python function, as follows: return v1, v2.  Don't worry about duplicates yet.  They will be dealt with in later tasks.  Think about the DRY (Don't repeat Yourself principal).  You may want to create a helper function to avoid duplicating code.

    Call the function within your assignment2.py script.  Store the values from the values it returns in the global variables minutes1 and minutes2. Note When a function returns several values, you get them as follows: v1, v2 = function(). Print out those dicts, so that you can see what's stored.

    Run the test until this part passes.
    """

    with open("../csv/minutes1.csv") as file1:
        reader1 = csv.reader(file1)
        minutes1 = {}
        minutes1["fields"] = next(reader1)
        minutes1["rows"] = tuple([tuple(x) for x in reader1])

    with open("../csv/minutes2.csv") as file2:
        reader2 = csv.reader(file2)
        minutes2 = {}
        minutes2["fields"] = next(reader2)
        minutes2["rows"] = tuple([tuple(x) for x in reader2])

    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
print(minutes1, minutes2)


# Task 13
def create_minutes_set():
    """

    Create a function called create_minutes_set.  It takes no parameters. It creates two sets from the rows of minutes1 and minutes2 dicts.  (This is just type conversion.  However, to make it work, each row has to be hashable!  Sets only support hashable elements.  Lists aren't hashable, so that is why you stored the rows as tuples in Task 10.)  Combine the members of both sets into one single set.  (This operation is called a union.)  The function returns the resulting set.

    Call the function within your assignment2.py script.  Store the value returned in the global variable minutes_set.

    Run the test until the next part passes.
    """
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    set1.update(set2)
    return set1


minutes_set = create_minutes_set()


# Task 14
def create_minutes_list():
    """

    Add a statement, from datetime import datetime, to your program.  The datetime module has some nice capabilities for converting strings to dates.  You can look them up: strptime() and strftime().

    Create a function called create_minutes_list.  It takes no parameters, and does the following:
        Create a list from the minutes_set. This is just type conversion.
        Use the map() function to convert each element of the list. At present, each element is a list of strings, where the first element of that list is the name of the recorder and the second element is the date when they recorded.
        The map() should covert each of these into a tuple. The first element of the tuple is the name (unchanged). The second element of the tuple is the date string converted to a datetime object.
        You convert the date strings into datetime objects using datetime.strptime(string, "%B %d, %Y").
        So, you could use the following lambda: lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y"))
        The function should return the resulting list.

    Call the function from within your program.  Store the return value in the minutes_list global.  Print it out, so you can see what it looks like.

    Run the test until the next part passes.
    """
    minutes_list = list(minutes_set)

    # minutes = map(
    #     lambda row: (row[0], datetime.strptime(row[1], "%B %d, %Y")), minutes_list
    # )

    minutes = [
        (item[0], datetime.strptime(item[1], "%B %d, %Y")) for item in minutes_list
    ]

    return list(minutes)


minutes_list = create_minutes_list()


# Task 15
def write_sorted_list():
    """

    Create a function called write_sorted_list.  It takes no parameters.  It should do the following:
        Sort minutes_list in ascending order of datetime.
        Call map again to convert the list. In this case, for each tuple, you create a new tuple. The first element of the tuple is the name (unchanged). The second element of the tuple is the datetime converted back to a string, using datetime.strftime(date, "%B %d, %Y")
        Open a file called ./minutes.csv. Use a csv.writer to write out the resulting sorted data. The first row you write should be the value of fields the from minutes1 dict. The subsequent rows should be the elements from minutes_list.
        The function should return the converted list.

    Call this function from within your program.  Then check that the file is created, and that it contains appropriate content.

    Run the test again until the next test has passed.
    """
    minutes_list.sort(key=lambda row: row[1])
    minutes = list(
        map(lambda row: (row[0], datetime.strftime(row[1], "%B %d, %Y")), minutes_list)
    )

    with open("./minutes.csv", "w") as file:
        writer = csv.writer(file)

        for row in minutes:
            writer.writerow(row)

    return minutes


minutes = write_sorted_list()
print(minutes)

"""Check for Understanding

    You created the minutes_set from several lists.  You then created a list from the set.  What's the point of the set, if you're going to end up with a list?

    Why did you subsequently need to create the list called minutes_list?  Couldn't you just keep working with the set?

    Why did you need to convert the date strings to datetime objects?

    Why did you convert them back to strings before writing out the CSV?
"""
# the answers:
# We used a set to get rid of duplicate values so we converted to sets
# in order to use mutable lists we have to convert set back to list
# the date string was converted to allow easier sorting via datetime
# the datetime object needs to be converted to str to be printed in a prededined way
