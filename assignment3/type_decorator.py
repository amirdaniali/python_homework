# # Amir Daniali
# https://github.com/amirdaniali
# Code The Dream King Cobra
# Week 3


# Task 2
def type_converter(type_of_output):
    """
        Within your assignment3 folder, write a script called type-decorator.py.
    Declare a decorator called type_converter. It has one argument called type_of_output, which would be a type, like str or int or float. It should convert the return from func to the corresponding type, viz:

    x = func(*args, **kwargs)
    return type_of_output(x)

    Write a function return_int() that takes no arguments and returns the integer value 5. Decorate that function with type-decorator. In the decoration, pass str as the parameter to type_decorator.
    Write a function return_string() that takes no arguments and returns the string value "not a number". Decorate that function with type-decorator. In the decoration, pass int as the parameter to type_decorator. Think: What's going to happen?
    In the mainline of the program, add the following:

    y = return_int()
    print(type(y).__name__) # This should print "str"
    try:
       y = return_string()
       print("shouldn't get here!")
    except ValueError:
       print("can't convert that string to an integer!") # This is what should happen
    """

    def decorator_wrapper(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            if type_of_output == "str":
                return str(x)
            elif type_of_output == "int":
                return int(x)
            elif type_of_output == "float":
                return float(x)
            else:
                return "Invalid type specified. Type must be <str or int or float>"

        return wrapper

    return decorator_wrapper
