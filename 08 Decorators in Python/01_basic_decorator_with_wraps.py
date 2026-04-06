"""
File: 01_basic_decorator_with_wraps.py
Chapter: 08 — Decorators in Python
Topic: Using functools.wraps to Preserve Function Metadata

Problem Statement
-----------------
In Python, decorators are used to add extra behavior to existing functions
without modifying their source code. However, when a decorator wraps a
function, it replaces the original function with a new wrapper function.

This causes a problem: the original function's identity — its name,
docstring, and other metadata — gets lost and replaced by the wrapper's
identity.

Python's `functools.wraps` solves this problem by copying the original
function's metadata onto the wrapper function.

This file demonstrates:
1. How a basic decorator is structured and applied.
2. What problem occurs when `functools.wraps` is not used.
3. How `functools.wraps` preserves the original function's metadata.
4. How to verify that metadata is preserved correctly.

Key Concepts
------------
Decorator
    A function that takes another function as input, adds extra behavior,
    and returns a modified version of that function.

functools.wraps
    A built-in tool that copies the original function's metadata
    (name, docstring, etc.) onto the wrapper function inside a decorator.

Function Metadata
    Information attached to a function such as its name (`__name__`)
    and its docstring (`__doc__`).

Wrapper Function
    The inner function inside a decorator that wraps the original
    function and adds extra behavior around it.
"""

# ---------------------------------------------------------
# Step 1: Import Required Tool
# ---------------------------------------------------------
# `wraps` is imported from Python's built-in `functools` module.
#
# It is used inside decorators to preserve the original function's
# metadata such as its name and docstring.
#
# Without `wraps`, the decorator would replace the function's
# identity with the wrapper's identity.

from functools import wraps


# ---------------------------------------------------------
# Step 2: Define the Decorator
# ---------------------------------------------------------
# A decorator is simply a function that:
#   • Accepts another function as its parameter
#   • Defines a wrapper function that adds behavior
#   • Returns the wrapper function
#
# The `@wraps(func)` line copies the metadata of `func`
# onto the `wrapper` function before it is returned.


def my_decorator(func):
    """
    A simple decorator that prints messages before and after
    the execution of the decorated function.

    Parameters
    ----------
    func : function
        The original function being decorated.

    Returns
    -------
    function
        The wrapper function with additional behavior added
        before and after the original function call.
    """

    @wraps(func)  # Copies metadata from `func` onto `wrapper`
    def wrapper():
        """
        Wrapper function that adds extra behavior
        before and after the original function call.
        """
        print("Before function runs")
        func()  # Calls the original function
        print("After function runs")

    return wrapper


# ---------------------------------------------------------
# Step 3: Apply the Decorator
# ---------------------------------------------------------
# The `@my_decorator` syntax is a shorthand for:
#   greet = my_decorator(greet)
#
# Python automatically passes `greet` as `func` into
# `my_decorator` and replaces `greet` with the returned wrapper.

@my_decorator  # Applying the decorator to `greet`
def greet():
    """
    A simple greeting function.
    """
    print("Hello! Nice to meet you.")


# ---------------------------------------------------------
# Step 4: Execute and Observe
# ---------------------------------------------------------
# Calling `greet()` now runs the wrapper function,
# which adds behavior before and after the original `greet`.

greet()

# ---------------------------------------------------------
# Step 5: Verify That Metadata is Preserved
# ---------------------------------------------------------
# Checking the function's name using `__name__`
#
# Without `@wraps(func)`:
#   greet.__name__ would print "wrapper"
#   because the decorator replaced `greet` with `wrapper`
#
# With `@wraps(func)`:
#   greet.__name__ correctly prints "greet"
#   because `wraps` copied the original metadata onto `wrapper`

print(greet.__name__)