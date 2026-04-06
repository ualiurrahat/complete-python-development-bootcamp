"""
File: 02_decorator_with_args_kwargs.py
Chapter: 08 — Decorators in Python
Topic: Writing Decorators That Support *args and **kwargs

Problem Statement
-----------------
A basic decorator works well when the function it wraps takes no arguments.
However, real-world functions often accept a variety of positional and
keyword arguments.

To make a decorator truly reusable across any function — regardless of
how many arguments that function accepts — the wrapper function inside
the decorator must be designed to forward all arguments to the original
function.

Python provides `*args` and `**kwargs` for this exact purpose.

This file demonstrates:
1. Why a basic decorator fails when the wrapped function takes arguments.
2. How `*args` collects any number of positional arguments.
3. How `**kwargs` collects any number of keyword arguments.
4. How to build a decorator that works universally for any function.
5. How the decorator forwards all arguments to the original function.

Key Concepts
------------
*args
    Collects all positional arguments passed to a function into a tuple.
    Allows a function to accept any number of positional inputs.

**kwargs
    Collects all keyword arguments passed to a function into a dictionary.
    Allows a function to accept any number of named inputs.

Reusable Decorator
    A decorator designed to work with any function regardless of
    the number or type of arguments that function accepts.

Argument Forwarding
    Passing all received arguments from the wrapper function
    directly into the original function using `*args` and `**kwargs`.
"""

# ---------------------------------------------------------
# Step 1: Import Required Tool
# ---------------------------------------------------------
# `wraps` is imported from Python's built-in `functools` module.
#
# It preserves the original function's metadata (name, docstring)
# after the decorator wraps it.

from functools import wraps


# ---------------------------------------------------------
# Step 2: Define the Decorator
# ---------------------------------------------------------
# The wrapper function uses `*args` and `**kwargs` so it can
# accept any combination of positional and keyword arguments.
#
# These are then forwarded directly to the original function
# using `func(*args, **kwargs)`.
#
# This is what makes the decorator universally reusable —
# it does not need to know in advance what arguments
# the wrapped function expects.


def logActivity(func):
    """
    A decorator that logs when a function starts and finishes execution.

    This decorator is reusable across any function because it uses
    *args and **kwargs to accept and forward any arguments.

    Parameters
    ----------
    func : function
        The original function being decorated.

    Returns
    -------
    function
        The wrapper function that logs activity and forwards
        all arguments to the original function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper that accepts any positional and keyword arguments
        and forwards them to the original function.

        *args    : captures all positional arguments as a tuple
        **kwargs : captures all keyword arguments as a dictionary
        """
        print(f"🚀 Calling: {func.__name__}")

        # Call the original function and forward all arguments.
        # The return value is stored so it can be passed back
        # to the caller — important if the original function returns data.
        result = func(*args, **kwargs)

        print(f"✅ Finished: {func.__name__}")

        # Return the result so the caller receives it
        return result

    return wrapper


# ---------------------------------------------------------
# Step 3: Apply the Decorator
# ---------------------------------------------------------
# `brewChai` takes one positional argument (`type`) and
# one keyword argument (`milk`) with a default value.
#
# The decorator handles both automatically because the wrapper
# uses `*args` and `**kwargs`.

@logActivity
def brewChai(type, milk="no"):
    """
    Simulates brewing a type of chai with optional milk.

    Parameters
    ----------
    type : str
        The variety of chai to brew (e.g., "Masala", "Ginger").

    milk : str, optional
        Whether milk is added. Defaults to "no".
    """
    print(f"Brewing {type} chai and milk status {milk}")


# ---------------------------------------------------------
# Step 4: Execute and Observe
# ---------------------------------------------------------
# Calling `brewChai("Masala")` now runs through the wrapper first.
#
# Execution order:
#   1. Wrapper prints "🚀 Calling: brewChai"
#   2. Original `brewChai` runs and prints the brewing message
#   3. Wrapper prints "✅ Finished: brewChai"

brewChai("Masala")