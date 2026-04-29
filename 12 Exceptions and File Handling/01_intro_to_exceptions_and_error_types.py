"""
File: 01_intro_to_exceptions_and_error_types.py
Chapter: 12 — Exceptions and File Handling
Topic: Understanding Exceptions and Common Error Types

Problem Statement
-----------------
When Python programs run, they encounter situations that prevent normal
execution. Accessing a list index that doesn't exist, dividing by zero,
or trying to use a variable that wasn't defined — these are all errors
that cause programs to crash.

In programming terminology, these runtime errors are called "exceptions."
Instead of letting programs crash unexpectedly, we can "handle" exceptions
to provide graceful failure, alternative behavior, or meaningful error
messages to users.

This file introduces:
1. What exceptions are and why they occur.
2. Why exception handling is essential for robust programs.
3. Common built-in exception types in Python.
4. The difference between syntax errors and runtime exceptions.

Key Concepts
------------
Exception
    An event that occurs during program execution that disrupts the normal
    flow of instructions. When Python encounters an exception, it creates
    an exception object and stops execution unless the exception is handled.

Exception Handling
    The practice of writing code that anticipates possible exceptions
    and responds to them appropriately. This prevents crashes and allows
    programs to recover from unexpected situations.

Syntax Error vs Runtime Exception
    Syntax Error: Occurs when code violates Python's grammar rules.
    Python cannot even run the program. Example: missing colon, unmatched
    parentheses.

    Runtime Exception: Code is syntactically correct but something goes
    wrong during execution. Example: accessing index 2 in a list with only
    2 items (indices 0 and 1 exist, index 2 does not).

Common Python Exception Types
-----------------------------
IndexError
    Raised when trying to access a list or tuple index that does not exist.
    Example: my_list = [1, 2]; my_list[5]

KeyError
    Raised when trying to access a dictionary key that does not exist.
    Example: my_dict = {"name": "Ali"}; my_dict["age"]

NameError
    Raised when a variable or function name is not defined.
    Example: print(undefined_variable)

ZeroDivisionError
    Raised when attempting to divide a number by zero.
    Example: result = 10 / 0

TypeError
    Raised when an operation is performed on an inappropriate data type.
    Example: "hello" + 5  (cannot add string and integer)

ValueError
    Raised when a function receives an argument of correct type but
    inappropriate value. Example: int("hello") (cannot convert string to int)

AttributeError
    Raised when trying to access an attribute or method that doesn't exist.
    Example: "hello".split(",") works, but "hello".something() fails

FileNotFoundError
    Raised when trying to open a file that doesn't exist.
    Example: open("nonexistent_file.txt")

ImportError
    Raised when an import statement cannot find the specified module.
    Example: import some_module_that_doesnt_exist
"""


# ---------------------------------------------------------
# Demonstration: What Happens When Exceptions Are NOT Handled
# ---------------------------------------------------------
# The code below will crash because index 2 doesn't exist in a list of 2 items.
# List indices for ['masala', 'ginger'] are 0 and 1 only.

orders = ["masala", "ginger"]

# This line raises IndexError because index 2 is out of range
# Uncommenting this line will crash the program:
# print(orders[2])

"""
When the above line runs, Python prints:
Traceback (most recent call last):
  File "filename.py", line XX, in <module>
    print(orders[2])
          ~~~~~~^^^
IndexError: list index out of range

The program stops immediately. Any code after this line never executes.
This is why we need exception handling — to catch these errors and
respond gracefully instead of crashing.
"""

# ---------------------------------------------------------
# Why Exception Handling Matters
# ---------------------------------------------------------
# Without exception handling:
#   • Programs crash unexpectedly
#   • Users see technical tracebacks instead of helpful messages
#   • Running applications stop completely
#   • Data being processed can be lost
#
# With exception handling:
#   • Programs can recover from errors
#   • Users receive friendly error messages
#   • Alternative actions can be taken
#   • Logs can record what went wrong for debugging


# ---------------------------------------------------------
# Important Notes
# ---------------------------------------------------------
# 1. Exceptions are not always bad. They signal that something unexpected
#    occurred, giving you a chance to handle it.
#
# 2. Different exception types help you handle specific errors differently.
#    You might retry an IndexError but log a TypeError as a bug.
#
# 3. Python has many built-in exceptions. The ones above are the most common.
#
# 4. You can also create custom exception classes for your specific needs.
#
# 5. The next files in this chapter will demonstrate how to handle these
#    exceptions using try, except, else, finally blocks.