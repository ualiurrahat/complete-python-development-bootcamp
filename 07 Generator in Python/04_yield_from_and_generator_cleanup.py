"""
File: 04_yield_from_and_generator_cleanup.py
Chapter: 07 Generators and Decoreation in Python
Topic: yield from Delegation, Generator Composition, and Proper Generator Cleanup

Problem Statement
-----------------
Generators can be combined together to form larger generators.
Python provides the `yield from` syntax to delegate part of a generator’s
work to another generator.

This file demonstrates:
1. How multiple generators can be combined into one using `yield from`.
2. Why we must CALL the generator function while using `yield from`.
3. How generators can be gracefully closed using `.close()`.
4. How `try` and `except` blocks help in handling generator shutdown.
5. What happens internally when a generator is manually closed.

Key Concepts
------------
yield from
    Delegates control to another generator and yields all its values.

Generator Delegation
    One generator uses values from another generator.

Generator Cleanup
    Generators can be manually stopped using `.close()` to free resources.

try / except
    Used to handle exceptions and perform safe cleanup.
"""

# ---------------------------------------------------------
# Step 1: Define small generators (sub-menus)
# ---------------------------------------------------------
# These represent separate sources of chai items.


def local_chai():
    """Generator for locally available chai varieties."""
    yield "Masala Chai"
    yield "Ginger Chai"


def imported_chai():
    """Generator for imported chai varieties."""
    yield "Matcha"
    yield "Oolong"


# ---------------------------------------------------------
# Step 2: Combine multiple generators using `yield from`
# ---------------------------------------------------------
# `yield from` takes all values from another generator
# and yields them as if they were part of this generator.
#
# IMPORTANT:
# We MUST call the generator function using parentheses.
#
# Correct:  yield from local_chai()
# Wrong:    yield from local_chai
#
# Because `local_chai` is a function, but
# `local_chai()` is a generator object.


def full_menu():
    """Generator that combines local and imported chai menus."""

    # Delegating to another generator
    yield from local_chai()

    # Delegating to another generator
    yield from imported_chai()


# ---------------------------------------------------------
# Step 3: Iterating through the combined generator
# ---------------------------------------------------------

for chai in full_menu():
    print(chai)


# ---------------------------------------------------------
# Step 4: Generator that waits for orders continuously
# ---------------------------------------------------------
# This generator keeps running and waiting for orders.
# It demonstrates how generators can run indefinitely
# and why proper cleanup is important.


def chai_stall():
    """
    Generator that simulates a chai stall waiting for orders.

    This generator runs in an infinite loop and keeps waiting
    at `yield` for the next order.

    When the generator is manually closed using `.close()`,
    Python raises a special exception called GeneratorExit.
    We handle that using try/except to print a closing message.
    """

    try:
        while True:
            # Pause and wait for next order
            order = yield "Waiting for chai order"

    except GeneratorExit:
        # This block runs when `.close()` is called
        print("Stall closed! No More Chai!!")


# ---------------------------------------------------------
# Step 5: Using the chai stall generator
# ---------------------------------------------------------

stall = chai_stall()

# Start the generator to reach the first yield
print(next(stall))

# ---------------------------------------------------------
# Step 6: Manually closing the generator
# ---------------------------------------------------------
# Why do we close generators?
#
# 1. To free resources.
# 2. To stop infinite generators safely.
# 3. To trigger cleanup code inside the generator.
#
# `.close()` raises GeneratorExit inside the generator,
# which we catch using the except block above.

stall.close()