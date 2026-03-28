"""
File: 01_generator_basics_and_yield.py
Chapter: 07 Generators and Decoreation in Python
Topic: Generator Functions, yield Keyword, and Lazy Evaluation

Problem Statement
-----------------
In Python, when working with large datasets or sequences of values, storing
everything in memory at once can be inefficient. Generators solve this problem
by producing values one at a time instead of storing them all in memory.

This file demonstrates:
1. What a generator is.
2. Why generators are useful.
3. How the `yield` keyword works.
4. The difference between returning a list and using a generator.
5. How to iterate through a generator.
6. How the `next()` function retrieves values from a generator.

Key Generator Concepts
----------------------
• Memory Efficiency:
  Generators do not store all values in memory at once. They generate values
  only when needed.

• Lazy Evaluation:
  Values are computed only when requested, making programs more efficient.

• Execution Pause:
  The `yield` keyword pauses the function and resumes execution from the
  same location the next time the generator is called.
"""

# ---------------------------------------------------------
# Step 1: Creating a generator function
# ---------------------------------------------------------
# A generator function is a normal Python function that uses
# the keyword `yield` instead of `return`.
#
# Every time `yield` is encountered:
#   • The function pauses
#   • The current value is returned
#   • The function resumes from that same line on the next call


def serve_chai():
    """
    Generator function that simulates serving different cups of chai.

    Each `yield` statement returns one value at a time.
    The function pauses after each yield and resumes later.
    """

    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"


# ---------------------------------------------------------
# Step 2: Creating a generator object
# ---------------------------------------------------------
# Calling a generator function does NOT run the function immediately.
# Instead, Python returns a generator object.

stall = serve_chai()

# ---------------------------------------------------------
# Step 3: Iterating through the generator
# ---------------------------------------------------------
# A generator can be used in loops.
# The loop automatically calls `next()` internally to get values.

for cup in stall:
    print(cup)


# ---------------------------------------------------------
# Step 4: Understanding how `yield` works
# ---------------------------------------------------------
# The `yield` keyword:
#   • Pauses the function
#   • Returns the value
#   • Saves the current execution state
#   • Resumes from the same location on the next call
#
# This behavior allows generators to produce values gradually
# instead of computing everything at once.


# ---------------------------------------------------------
# Step 5: Traditional approach using lists
# ---------------------------------------------------------
# A normal function typically returns a list containing all values.
# This means all values must be created and stored in memory.


def get_chai_list():
    """
    Traditional function that returns all chai cups as a list.

    Disadvantage:
    The entire list is created and stored in memory immediately.
    """
    return ["Cup 1", "Cup 2", "Cup 3"]


# ---------------------------------------------------------
# Step 6: Generator version of the same function
# ---------------------------------------------------------
# Instead of returning a full list, a generator yields values one by one.


def get_chai_gen():
    """
    Generator function that yields chai cups one at a time.

    Advantage:
    Values are generated only when requested.
    This improves memory efficiency.
    """

    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


# ---------------------------------------------------------
# Step 7: Creating a generator object
# ---------------------------------------------------------

chai = get_chai_gen()

# Printing the generator object itself
# This shows that the function returned a generator object
print(chai)


# ---------------------------------------------------------
# Step 8: Using next() to manually retrieve values
# ---------------------------------------------------------
# The `next()` function retrieves the next value from a generator.

print(next(chai))  # First yield
print(next(chai))  # Second yield
print(next(chai))  # Third yield

# If we call next() again after all values are exhausted,
# Python raises a StopIteration error.

# print(next(chai))  # Uncommenting this line will raise StopIteration