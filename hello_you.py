#!/usr/bin/env python3
# hello_you.py
import sys


def hello_name(name="you"):
    """
    Takes 1 argument and returns "Hello, [Name]!" if a string is passed
    or "Hello, you!" if no string is passed
    """
    greet = f"Hello, {name}!"
    return print(greet)


if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    if arg_count != 1:
        hello_name()
    else:
        hello_name(sys.argv[1])
