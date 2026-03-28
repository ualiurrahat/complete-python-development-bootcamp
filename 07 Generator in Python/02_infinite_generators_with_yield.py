"""
File: 02_infinite_generators_with_yield.py
Chapter: 07 Generators and Decoreation in Python
Topic: Infinite Generators, yield Keyword, and Streaming Data

Problem Statement
-----------------
Sometimes we need a sequence of values that does not have a fixed end.
Examples include:
• Live data streams
• Continuous event processing
• Sensor data collection
• Real-time logs

In such cases, Python generators can produce values indefinitely.
These are called **infinite generators**.

This file demonstrates:
1. What an infinite generator is.
2. How the `yield` keyword allows continuous value generation.
3. Why infinite generators are useful in streaming scenarios.
4. Why they must be used carefully to avoid infinite loops.

Key Concepts
------------
Infinite Generator
    A generator that produces values forever unless manually stopped.

Streaming Data
    Data that arrives continuously over time.

Lazy Evaluation
    Values are produced only when requested using `next()` or iteration.
"""

# ---------------------------------------------------------
# Step 1: Creating an Infinite Generator
# ---------------------------------------------------------
# An infinite generator typically uses a `while True` loop.
#
# `while True` creates an endless loop. However, because we
# use `yield`, the function pauses after producing each value.
#
# The function only resumes when the next value is requested.

def infinite_chai():
    """
    Generator that produces an unlimited number of chai refills.

    Returns
    -------
    str
        A refill message such as:
        "Refill #1", "Refill #2", "Refill #3", ...

    Important
    ---------
    Since this generator runs indefinitely, it must be controlled
    by limiting how many values we request from it.
    """

    # Counter to track refill numbers
    count = 1

    # Infinite loop that keeps generating new values
    while True:

        # Yield the refill message
        yield f"Refill #{count}"

        # Increase the counter for the next refill
        count += 1


# ---------------------------------------------------------
# Step 2: Creating Generator Objects
# ---------------------------------------------------------
# Each call to the generator function creates a **separate generator instance**.
#
# This means each generator maintains its own internal state.

refill = infinite_chai()
user2 = infinite_chai()


# ---------------------------------------------------------
# Step 3: Retrieving values from the first generator
# ---------------------------------------------------------
# We limit the number of values using `range()`
# to avoid an infinite loop.

for _ in range(5):
    print(next(refill))


# ---------------------------------------------------------
# Step 4: Retrieving values from another generator instance
# ---------------------------------------------------------
# Notice that user2 starts from the beginning again
# because it is a separate generator object.

for _ in range(6):
    print(next(user2))


# ---------------------------------------------------------
# Important Notes About Infinite Generators
# ---------------------------------------------------------
# 1. Infinite generators are very useful for:
#       • Real-time data streams
#       • Continuous event processing
#       • Monitoring systems
#
# 2. Because they never stop automatically,
#    they must always be controlled carefully.
#
# 3. If used improperly inside loops without limits,
#    they can create infinite loops and cause programs
#    to run forever.
#
# 4. Despite being infinite, they are still memory efficient
#    because they generate values one at a time instead of
#    storing them all in memory.