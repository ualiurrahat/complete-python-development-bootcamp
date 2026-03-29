"""
File: 01_basic_decorator_with_wraps.py
Chapter: 08 — Decorators in Python
Topic: Using functools.wraps to Preserve Function Metadata

Problem Statement:
Demonstrate how a decorator works in Python and why `functools.wraps`
is important to preserve the original function's metadata such as
its name and docstring.
"""

# ---------------------- Step 1: Import Required Tool ----------------------
# `wraps` is used inside decorators to preserve the original function's metadata
from functools import wraps


# ---------------------- Step 2: Define the Decorator ----------------------
def my_decorator(func):
    """
    A simple decorator that prints messages before and after
    the execution of the decorated function.

    Parameters:
    func (function): The original function to be decorated.

    Returns:
    function: The wrapped function with additional behavior.
    """

    @wraps(func)  # This preserves the metadata of `func`
    def wrapper():
        """
        Wrapper function that adds extra behavior
        before and after the original function call.
        """
        print("Before function runs")
        func()
        print("After function runs")

    return wrapper


# ---------------------- Step 3: Apply the Decorator ----------------------
@my_decorator  # Applying the decorator to `greet`
def greet():
    """
    A simple greeting function.
    """
    print("Hello! Nice to meet you.")


# ---------------------- Step 4: Execute and Observe ----------------------
greet()

# Checking the function name
print(greet.__name__)

# Without using `wraps`, this would print: "wrapper"
# Because the decorator replaces the original function with `wrapper`
# Using `wraps` preserves the original function's identity: "greet"