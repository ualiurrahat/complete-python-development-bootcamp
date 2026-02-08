# ============================================================
# File: 02_if_else_and_user_input_handling.py
# Topic: if-else Statement and User Input Processing
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# Build a simple restaurant order system.
#
# Task:
# - Take a snack order from the user.
# - If the snack is either "cookies" or "pasta",
#   accept the order.
# - Otherwise, politely inform the user that
#   the item is not available.
#
# This introduces:
# - input() function
# - String comparison
# - Logical OR operator
# - if-else conditional logic
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Take User Input
# ------------------------------------------------------------
# input() reads a line of text entered by the user.
# lower() converts all characters to lowercase to ensure
# case-insensitive comparison.

snack = input("Enter your preferred snack: ").lower()


# ------------------------------------------------------------
# Step 2: Apply Conditional Logic
# ------------------------------------------------------------
# We check if the snack matches either of the available options.
#
# Logical OR:
# condition_1 OR condition_2
#
# → True if any one condition is True.

if snack == "cookies" or snack == "pasta":
    print(f"Great choice! We will serve you {snack}.")
else:
    print("Sorry! We only serve cookies or pasta.")


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - If user enters "Cookies", "cookies", "COOKIES", etc.,
#   lower() converts it into "cookies".
#
# - This avoids input mismatch errors.
#
# - If the condition fails, the else block executes.
# ------------------------------------------------------------
