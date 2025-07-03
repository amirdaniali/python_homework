# Write your code here.

# Amir Daniali
# https://github.com/amirdaniali
# Code The Dream King Cobra
# Week 1

from typing import Union, List


# Task 1
def hello() -> str:
    """Write a hello function that takes no arguments and returns Hello!.  Now, what matters here is what the function returns.  You can print() whatever you want for debugging purposes, but the tests ignore that, and only check the return value."""
    return "Hello!"


# Task 2
def greet(name: str) -> str:
    """Write a greet function.  It takes one argument, a name, and returns Hello, Name!.  Use a formatted string.  Note that you have to return exactly the right string or the test fails -- but PyTest tells you what didn't match."""
    return f"Hello, {name}!"


# Task 3
def calc(
    value1: Union[int, float], value2: Union[int, float], operation: str = "multiply"
) -> Union[int, float, str]:
    """
    Write a calc function. It takes three arguments. The default value for the third argument is "multiply". The first two arguments are values that are to be combined using the operation requested by the third argument, a string that is one of the following add, subtract, multiply, divide, modulo, int_divide (for integer division) and power. The function returns the result.
    Error handling: When the function is called, it could ask you to divide by 0. That will throw an exception: Which one? You can find out by triggering the exception in your program or in the Python Interactive Shell. Wrap the code within the calc function in a try block, and put in an except statement for this exception. If the exception occurs, return the string "You can't divide by 0!".
    More error handling: When the function is called, the parameters that are passed might not work for the operation. For example, you can't multiply two strings. Find out which exception occurs, catch it, and return the string "You can't multiply those values!".
    Here's a tip. You have to do different things for add, multiply, divide and so on. So you can do a conditional cascade, if/elif/elif/else. That's perfectly valid. But you might want to use the match-case Python statement instead. Look it up! It just improves code appearance.
    """
    analysed_operation = operation.lower()
    correct_operations = [
        "add",
        "subtract",
        "multiply",
        "divide",
        "modulo",
        "int_divide",
        "power",
    ]

    if analysed_operation not in correct_operations:
        return "Incorrect Operation"

    # we could check here if value1 and value2 are numerical but we dont

    if analysed_operation == "add":
        return value1 + value2
    elif analysed_operation == "subtract":
        try:
            return value1 - value2
        except TypeError:
            return "You can't subtract those values!"
    elif analysed_operation == "multiply":
        try:
            return value1 * value2
        except TypeError:
            return "You can't multiply those values!"
    elif analysed_operation == "divide":
        try:
            return value1 / value2
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif analysed_operation == "modulo":
        try:
            return value1 % value2
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif analysed_operation == "int_divide":
        try:
            return value1 // value2
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif analysed_operation == "power":
        try:
            return value1**value2
        except TypeError:
            return "Values need to be numerical!"


# Task 3
def data_type_conversion(
    value: Union[int, str, float], name: str
) -> Union[int, str, float]:
    """
    Create a function called data_type_conversion. It takes two parameters, the value and the name of the data type requested, one of float, str, or int. Return the converted value.
    Error handling: The function might be called with a bad parameter. For example, the caller might try to convert the string "nonsense" to a float. Catch the error that occurs in this case. If this error occurs, return the string You can't convert {value} into a {type}., except you use the value and data type that are passed as parameters -- so again you use a formatted string.
    """
    lower_case_name = name.lower()
    if lower_case_name not in [
        "int",
        "str",
        "float",
    ]:
        return "Type name not valid!"
    if lower_case_name == "int":
        try:
            return int(value)
        except TypeError:
            return f"You can't convert {value} into a {name}."
        except ValueError:
            return f"You can't convert {value} into a {name}."
    elif lower_case_name == "float":
        try:
            return float(value)
        except TypeError:
            return f"You can't convert {value} into a {name}."
        except ValueError:
            return f"You can't convert {value} into a {name}."
    elif lower_case_name == "str":
        try:
            return str(value)
        except TypeError:
            return f"You can't convert {value} into a {name}."
        except ValueError:
            return f"You can't convert {value} into a {name}."


# Task 5
def grade(*args: int):
    """
    Create a grade function. It should collect an arbitrary number of parameters, compute the average, and return the grade. based on the following scale:
        A: 90 and above
        B: 80-89
        C: 70-79
        D: 60-69
        F: Below 60
    When you use *args you get access to a variable named args in your function, which is a tuple, an ordered collection of values like a list. You'll learn more about tuples and lists in the next lesson. There are some helpful functions you can use at this point: sum(args), len(args), and so on. One of the curiosities of Python is that these are not methods of any class. They are just standalone functions.
    Handle the error that occurs if the parameters are nonsense. Return the string "Invalid data was provided." in this case. (Typically, you don't handle every possible exception in your error handling, except if the values in the parameters comes from the end user.)
    """

    try:
        calculated_sum: float = sum([x for x in args]) / len(args)

        if calculated_sum >= 90:
            return "A"
        elif calculated_sum >= 80:
            return "B"
        elif calculated_sum >= 70:
            return "C"
        elif calculated_sum >= 60:
            return "D"
        else:
            return "F"

    except (ValueError, TypeError):
        return "Invalid data was provided."


# Task 6
def repeat(string: str, count: int):
    """Task 6: Use a For Loop with a Range

    Create a function called repeat. It takes two parameters, a string and a count, and returns a new string that is the old one repeated count times.
    You can get the test to pass by just returning string * count. That would produce the correct return value. But, for this task, do it using a for loop and a range.
    """
    if type(count) != int and type(string) != str:
        raise ValueError

    generated_string: str = ""

    for _ in range(count):
        generated_string += string

    return generated_string


# Task 7
def student_scores(operation: str, **kwargs: int):
    """Task 7: Student Scores, Using **kwargs

    Create a function called student_scores. It takes one positional parameter and an arbitrary number of keyword parameters. The positional parameter is either "best" or "mean". If it is "best", the name of the student with the higest score is returned. If it is "mean", the average score is returned.
    As you are using **kwargs, your function can access a variable named kwargs, which is a dict. The next lesson explains about dicts. What you need to know now is the following:
        A dict is a collection of key value pairs.
        You can iterate through the dict as follows:

    for key, value in kwargs.items():

        You can also get kwargs.keys() and kwargs.values().
    The arbitrary list of keyword arguments uses the names of students as the keywords and their test score as the value for each.
    """
    if type(operation) != str:
        return "Invalid operation was provided."

    analysed_operation: str = operation.lower()

    if analysed_operation not in ["mean", "best"]:
        return "Invalid operation was provided."

    if analysed_operation == "best":
        values = list(kwargs.values())
        keys = list(kwargs.keys())
        return keys[values.index(max(values))]

    elif analysed_operation == "mean":
        try:
            return sum([number for number in kwargs.values()]) / len(kwargs)
        except (TypeError, ValueError):
            return "Invalid data was provided."


# Task 8
def titleize(string: str) -> str:
    """
        Create a function called titleize. It accepts one parameter, a string. The function returns a new string, where the parameter string is capitalized as if it were a book title.
        The rules for title capitalization are: (1) The first word is always capitalized. (2) The last word is always capitalized. (3) All the other words are capitalized, except little words. For the purposes of this task, the little words are "a", "on", "an", "the", "of", "and", "is", and "in".
        The following string methods may be helpful: split(), join(), and capitalize(). Look 'em up.
        The split() method returns a list. You might store this in the words variable. words[-1] gives the last element in the list.
        The in comparison operator: You have seen in used in loops. But it can also be used for comparisons, for example to check to see if a substring occurs in a string, or a value occurs in a list.
        A new trick: As you loop through the words in the words list, it is helpful to have the index of the word for each iteration. You can access that index using the enumerate() function:

    for i, word in enumerate(words):"""

    try:
        all_words: List[str] = string.split(" ")
        return " ".join(
            word.capitalize()
                if word not in ["a", "on", "an", "the", "of", "and", "is", "in"]
                or index in [0, len(all_words) - 1]
                else (word)
            for index, word in enumerate(all_words)
        )

    except ValueError:
        return "Invalid input."


#Task 9
def hangman(secret: str, guess: str) -> str:
    """
    Create a function hangman. It takes two parameters, both strings, the secret and the guess.
    The secret is some word that the caller doesn't know. So the caller guesses various letters, which are the ones in the guess string.
    A string is returned. Each letter in the returned string corresponds to a letter in the secret, except any letters that are not in the guess string are replaced with an underscore. The others are returned in place. Not everyone has played this kid's game, but it's common in the US.
    Example: Suppose the secret is "alphabet" and the guess is "ab". The returned string would be "a___ab__".
    Note that Python strings are immutable. That means that the following code would give an error:

secret = "alphabet"
secret[1] = "_"

    On the other hand, you can concatenate strings with the + operator.
"""
    return ''.join(
        char 
            if char in list(guess) 
            else '_'
        for char in list(secret)
    )

#Task 10
def pig_latin(sentence: str) -> str:
    """
    Pig Latin is a kid's trick language. Each word is modified according to the following rules. (1) If the string starts with a vowel (aeiou), "ay" is tacked onto the end. (2) If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them. (3) "qu" is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.
    Create a function called pig_latin. It takes an English string or sentence and converts it to Pig Latin, returning the result. We will assume that there is no punctuation and that everything is lower case.
"""
    all_words : List[str] = sentence.split(' ')
    modified_sentence_list : List[str] = []

    for word in all_words:
        new_word : str = word
        if word[0] in 'aeiou':
            modified_sentence_list.append(word + 'ay')
            continue
        while new_word[0] not in 'aeiou':
            if new_word[:2] in ['qu',]:
                new_word =  new_word[2:] + new_word[:2] 
            else:
                new_word =  new_word[1:] + new_word[:1] 
        modified_sentence_list.append(new_word + 'ay')

    return ' '.join(modified_sentence_list)