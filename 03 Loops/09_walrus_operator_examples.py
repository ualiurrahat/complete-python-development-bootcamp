# -------------------------------------------------------------
# File: 09_walrus_operator_examples.py
# Chapter: 03 Loops
#
# Topic: Walrus Operator (:=) in Python
#
# The walrus operator allows assignment inside expressions.
# It helps reduce extra lines of code when a value is needed
# immediately inside a condition or loop.
#
# Syntax:
# variable := expression
#
# This file demonstrates three examples:
# 1. Using walrus operator in an if condition
# 2. Using walrus operator with user input
# 3. Using walrus operator inside a while loop
# -------------------------------------------------------------


# -------------------------------------------------------------
# Example 1: Using Walrus Operator in an IF Condition
# -------------------------------------------------------------

value = 13

# Calculate remainder and assign it at the same time
if remainder := value % 5:
    print(f"Not divisible, remainder is {remainder}")


# -------------------------------------------------------------
# Example 2: Walrus Operator with User Input
# -------------------------------------------------------------

available_sizes = ["small", "medium", "large"]

# Take input and assign it during the condition check
if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Sorry! {requested_size} chai is unavailable")


# -------------------------------------------------------------
# Example 3: Walrus Operator Inside a WHILE Loop
# -------------------------------------------------------------

flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors:", flavors)

# Keep asking the user until they choose a valid flavor
while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You chose {flavor} chai")