# # Amir Daniali
# https://github.com/amirdaniali
# Code The Dream King Cobra
# Week 3

# Task 1

import logging
from pathlib import Path


logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(
    logging.FileHandler(Path(__file__).resolve().parent / "decorator.log", "a")
)


def logger_decorator(func):
    """
    Within the assignment3 folder, create a file called log-decorator.py. It should contain the following.
    Declare a decorator called logger_decorator. This should log the name of the called function (func.__name__), the input parameters of that were passed, and the value the function returns, to a file ./decorator.log. (Logging was described in lesson 1, so review this if you need to do so.) Functions may have positional arguments, keyword arguments, both, or neither. So for each invocation of a decorated function, the log would have:

    function: <the function name> positional parameters: <a list of the positional parameters, or "none" if none are passed> keyword parameters: <a dict of the keyword parameters, or "none" if none are passed> return: <the return value>

    Here's a cookbook on logging:

    # one time setup
    import logging
    logger = logging.getLogger(__name__ + "_parameter_log")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.FileHandler("./decorator.log","a"))
    ...
    # To write a log record:
    logger.log(logging.INFO, "this string would be logged")

    Declare a function that takes no parameters and returns nothing. Maybe it just prints "Hello, World!". Decorate this function with your decorator.
    Declare a function that takes a variable number of positional arguments and returns True. Decorate this function with your decorator.
    Declare a function that takes no positional arguments and a variable number of keyword arguments, and that returns logger_decorator. Decorate this function with your decorator.
    Within the mainline code, call each of these three functions, passing parameters for the functions that take positional or keyword arguments. Run the program, and verify that the log file contains the information you want.
    """

    def wrapper(*args, **kwargs):
        return_val = func(*args, **kwargs)
        logger.log(
            logging.INFO,
            f"function: {func.__name__} positional parameters: {args or 'none'} keyword parameters: {kwargs or 'none'} return: {return_val}",
        )

    return wrapper
