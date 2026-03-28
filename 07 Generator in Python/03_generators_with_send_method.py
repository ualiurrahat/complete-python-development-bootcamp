"""
File: 03_generators_with_send_method.py
Chapter: 07 Generators and Decoreation in Python
Topic: Generator Communication using yield and send()

Problem Statement
-----------------
Generators in Python are usually used to produce values one at a time.
However, generators can also receive values from the outside using the
`send()` method.

This feature allows two-way communication between the caller and the
generator function.

This file demonstrates:
1. How `yield` can pause execution and wait for external input.
2. How the `send()` method sends data into a generator.
3. Why an additional `yield` inside loops is important when handling
   multiple inputs.
4. How generator state resumes exactly where it paused.

Key Concepts
------------
yield
    Pauses the function and optionally returns a value.

send(value)
    Sends a value into a generator at the location of the paused `yield`.

Generator Initialization
    Before sending data, the generator must first be started using
    `next()` or `send(None)`.
"""

# ---------------------------------------------------------
# Step 1: Creating a generator that receives input
# ---------------------------------------------------------
# In this example, the generator represents a chai stall.
# The stall receives chai orders from customers.


def chai_customer():
    """
    Generator that accepts chai orders using the `send()` method.

    Workflow
    --------
    1. The generator starts and prints a welcome message.
    2. It pauses at `yield` waiting for the first order.
    3. Each order sent using `send()` is processed.
    4. The generator keeps running indefinitely to handle
       multiple customer orders.
    """

    # Welcome message when the stall starts
    print("Welcome! What chai would you like to have?")

    # -----------------------------------------------------
    # Step 2: Receive the first order
    # -----------------------------------------------------
    # This yield pauses execution and waits for input
    # from the caller using the `send()` method.

    order = yield

    # -----------------------------------------------------
    # Step 3: Infinite loop to process orders continuously
    # -----------------------------------------------------
    # This allows the generator to keep accepting new orders.

    while True:

        # Prepare the current order
        print(f"Preparing: {order}")

        # -------------------------------------------------
        # Step 4: Wait for the next order
        # -------------------------------------------------
        # This yield is extremely important.
        #
        # It pauses the generator again so that a new value
        # can be sent using `send()`.
        #
        # Without this line, the loop would run infinitely
        # using the previous value of `order`.
        #
        # Example problem - if this yield is removed:
        #   stall.send("Masala Chai")
        #
        # The generator would print:
        #   Preparing: Masala Chai
        #   Preparing: Masala Chai
        #   Preparing: Masala Chai
        #
        # endlessly, because no new input could be received.

        order = yield


# ---------------------------------------------------------
# Step 5: Creating the generator object
# ---------------------------------------------------------
# Calling the generator function does NOT execute it.
# It simply returns a generator object.

stall = chai_customer()


# ---------------------------------------------------------
# Step 6: Starting the generator
# ---------------------------------------------------------
# A generator must be started before sending data.
#
# `next()` runs the generator until it reaches the first
# `yield` statement.

next(stall)


# ---------------------------------------------------------
# Step 7: Sending values into the generator
# ---------------------------------------------------------
# The `send()` method sends a value into the generator.
# That value becomes the result of the paused `yield`.

stall.send("Masala Chai")
stall.send("Lemon Chai")