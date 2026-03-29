"""
File: 02_decorator_with_args_kwargs.py
Chapter: 08 — Decorators in Python
Topic: Writing Decorators That Support *args and **kwargs

Problem Statement:
Demonstrate how to build a reusable decorator that can wrap
any function regardless of the number of positional and keyword
arguments it accepts, while preserving function metadata using wraps.
"""

# ---------------------- Step 1: Import Required Tool ----------------------
from functools import wraps


# ---------------------- Step 2: Define the Decorator ----------------------
def logActivity(func):
    """
    A decorator that logs when a function starts and finishes execution.

    Parameters:
    func (function): The original function to be decorated.

    Returns:
    function: Wrapped function supporting any arguments.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper that accepts any positional and keyword arguments
        and forwards them to the original function.
        """
        print(f"🚀 Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished: {func.__name__}")
        return result

    return wrapper


# ---------------------- Step 3: Apply the Decorator ----------------------
@logActivity
def brewChai(type, milk="no"):
    """
    Simulates brewing a type of chai with optional milk.
    """
    print(f"Brewing {type} chai and milk status {milk}")


# ---------------------- Step 4: Execute and Observe ----------------------
brewChai("Masala")