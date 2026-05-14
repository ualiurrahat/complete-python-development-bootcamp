"""
File: 03_simple_bill_splitter.py
Folder: Projects/01 Utilities
Topic: Loops, Lists, Error Handling, and Arithmetic Operations

Problem Statement
-----------------
When dining out with friends, splitting the bill evenly is a common task.
Manual calculation becomes tedious with large groups. This program automates
the process by collecting group member names and total bill amount, then
calculating each person's equal share.

The program demonstrates:
1. Using a for loop to collect variable number of user inputs.
2. Storing multiple names in a list for later display.
3. Implementing input validation with try-except for numeric values.
4. Rounding monetary values to 2 decimal places.
5. Formatting output with decorative borders for readability.

Key Concepts
------------
Input Validation with try-except
    When converting user input to numbers, invalid entries (like letters)
    cause ValueError. try-except catches this and allows retrying instead
    of crashing the program.

round() Function
    Rounds a floating-point number to specified decimal places.
    Essential for monetary calculations to avoid long decimal chains
    (e.g., 33.3333333 → 33.33).

List append() Method
    Adds a new element to the end of a list. Used here to build the
    names list incrementally as each person's name is entered.

while True Loop
    Creates an infinite loop that only exits when valid input is received.
    Combined with break or return, this pattern is standard for input
    validation.
"""


# ---------------------------------------------------------
# Step 1: Define Input Validation Function
# ---------------------------------------------------------
# This function safely converts user input to a float.
# It keeps asking until the user provides a valid number.
# IMPORTANT: This pattern is essential for robust programs.

def get_float(prompt):
    """
    Repeatedly ask user for a floating-point number until valid input is given.
    
    Parameters
    ----------
    prompt : str
        Message displayed to user when asking for input.
    
    Returns
    -------
    float
        Valid floating-point number entered by user.
    
    Important
    ---------
    This function does not accept empty input. User must enter a number.
    """
    while True:
        try:
            # Attempt to convert user input to float
            return float(input(prompt))
        except ValueError:
            # Conversion failed (user entered text like "abc" or nothing)
            print("❌ Please enter a valid number.")


# ---------------------------------------------------------
# Step 2: Get Number of People in Group
# ---------------------------------------------------------
# int() converts the input to an integer (whole number).
# Note: No validation here — entering letters would crash the program.
# In production code, you'd also validate this input.

num_people = int(input("How many people are there in the group? "))


# ---------------------------------------------------------
# Step 3: Collect All Names Using a For Loop
# ---------------------------------------------------------
# Create an empty list to store names.
# The loop runs num_people times, collecting one name per iteration.

names = []

for i in range(num_people):
    # i starts at 0, so i+1 gives human-readable person numbers (1, 2, 3...)
    name = input(f"Enter the name of person #{i+1}: ").strip()
    names.append(name)  # Add the name to our list


# ---------------------------------------------------------
# Step 4: Get Total Bill Amount with Validation
# ---------------------------------------------------------
# Using get_float ensures user cannot crash the program with invalid input.
# This function will keep asking until a valid number is provided.

total_bill = get_float("Enter the bill amount in number only: ")


# ---------------------------------------------------------
# Step 5: Calculate Each Person's Share
# ---------------------------------------------------------
# Divide total bill by number of people, then round to 2 decimal places.
# Rounding is critical for money — floating-point math can produce
# numbers like 33.3333333333 which need to be displayed as 33.33.

share = round(total_bill / num_people, 2)


# ---------------------------------------------------------
# Step 6: Display Results with Decorative Formatting
# ---------------------------------------------------------
# Asterisk border creates visual separation from console history.
# The f-string for each person shows name and calculated share.

print("\n" + "*" * 40)
print(f"Total bill: ${total_bill}")
print(f"Each person owes: ${share}")
print()

for name in names:
    print(f"{name} owes ${share}")

print("*" * 40)


# ---------------------------------------------------------
# Example Run
# ---------------------------------------------------------
# Input:
#   How many people? 3
#   Person #1: Nasim
#   Person #2: Minul
#   Person #3: Rahat
#   Bill amount: 1200
#
# Output:
#   ****************************************
#   Total bill: $1200.0
#   Each person owes: $400.0
#
#   Nasim owes $400.0
#   Minul owes $400.0
#   Rahat owes $400.0
#   ****************************************


# ---------------------------------------------------------
# Important Notes About This Implementation
# ---------------------------------------------------------
# 1. Input Validation Gaps:
#    • Number of people is not validated (negative numbers or letters crash)
#    • Bill amount validation only checks for numbers (not negative amounts)
#
# 2. Floating-Point Precision:
#    For production finance apps, use Decimal from decimal module.
#    Example: from decimal import Decimal
#
# 3. Even Split Limitation:
#    This program assumes equal split. Real-world splitting might have
#    different percentages or items — that's a more advanced version.
#
# 4. Improvement Ideas:
#    • Add validation for number of people (must be positive integer)
#    • Handle tip percentage calculation
#    • Allow percentage-based unequal splits
#    • Display total with 2 decimal places always (${share:.2f})s