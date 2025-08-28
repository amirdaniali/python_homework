# Amir Daniali
# https://github.com/amirdaniali
# Code The Dream King Cobra
# Week 3

# Task 1
from log_decorator import logger_decorator
from type_decorator import type_converter


@logger_decorator
def my_function_1():
    """Declare a function that takes no parameters and returns nothing. Maybe it just prints "Hello, World!". Decorate this function with your decorator."""
    print("hello ctd")


@logger_decorator
def my_function_2(number):
    """Declare a function that takes no parameters and returns nothing. Maybe it just prints "Hello, World!". Decorate this function with your decorator."""
    print(f"{number} squared equals", number**2)
    return number**2


@logger_decorator
def my_function_3(*args):
    """Declare a function that takes a variable number of positional arguments and returns True. Decorate this function with your decorator."""
    return True


@logger_decorator
def my_function_4(**kwargs):
    """Declare a function that takes no positional arguments and a variable number of keyword arguments, and that returns logger_decorator. Decorate this function with your decorator."""
    return logger_decorator


my_var_1 = my_function_1()
my_var_2 = my_function_2(4)
my_var_3 = my_function_3("5", "hello", "ctd is awesome")
my_var_4 = my_function_4(jack=14, bob=21, samantha=98)


# Task 2
@type_converter("str")
def return_int():
    return 5


@type_converter("int")
def return_string():
    return "not a number"


y = return_int()
print(type(y).__name__)

try:
    y = return_string()
    print("shouldn't get here!")
except ValueError:
    print("can't convert that string to an integer!")
