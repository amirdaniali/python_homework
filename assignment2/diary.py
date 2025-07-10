# Amir Daniali
# https://github.com/amirdaniali
# Code The Dream King Cobra
# Week 2
# Task 1

import traceback

with open(file="diary.txt", mode="a+") as file:
    try:
        user_input = input("What happened today? ")
        while user_input != "done for now":
            file.write(user_input + "\n")
            user_input: str = input("What else? ")
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
