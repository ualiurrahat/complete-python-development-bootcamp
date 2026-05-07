"""
File: 01_self_intro_script_generator.py
Folder: Projects/01 Utilities
Topic: User Input and String Formatting Project

Problem Statement
-----------------
When building applications that interact with users, collecting and formatting
personal information into readable output is a fundamental requirement.
This project simulates a real-world scenario where a program needs to gather
user data and present it as a professional self-introduction.

The program demonstrates:
1. Collecting multiple user inputs using the input() function.
2. Cleaning user input by stripping extra whitespace with .strip().
3. Formatting strings using f-strings for variable interpolation.
4. Adding current date using Python's datetime module.
5. Creating visual separation with decorative borders.

Key Concepts
------------
input() Function
    Reads a line from user input and returns it as a string. The optional
    prompt parameter is displayed before waiting for input.

.strip() Method
    Removes leading and trailing whitespace (spaces, tabs, newlines) from
    a string. Essential for cleaning user input before processing.

f-strings (Formatted String Literals)
    Strings prefixed with 'f' that allow embedding expressions inside curly
    braces. Example: f"Hello {name}" where name is a variable.

datetime.date.today()
    Returns the current local date as a date object. .isoformat() converts
    it to ISO format string (YYYY-MM-DD).

String Multiplication
    Python allows multiplying strings with integers: "*" * 80 creates a
    string of 80 asterisks. No other language does this natively.
"""

# ---------------------------------------------------------
# Step 1: Import Required Modules
# ---------------------------------------------------------
# datetime module provides classes for manipulating dates and times.
# We only need the date class from this module.

import datetime


# ---------------------------------------------------------
# Step 2: Collect User Information
# ---------------------------------------------------------
# Each input() call displays a prompt and waits for user to type.
# .strip() removes any accidental spaces before or after the input.
# IMPORTANT: Without .strip(), "  Rahat  " would be stored with spaces.

name = input("What is your name: ").strip()
age = input("How old are you: ").strip()
city = input("Which city do you live in: ").strip()
profession = input("What is your profession: ").strip()
hobby = input("What is your favourite hobby: ").strip()


# ---------------------------------------------------------
# Step 3: Build the Introduction Message
# ---------------------------------------------------------
# Using parentheses to create a multi-line string without actually
# having newlines in the final output. Python automatically joins
# adjacent string literals inside parentheses.
#
# f-string syntax: {variable} is replaced with the variable's value.
# Note the space after period in "years old.I" — intentional? Actually
# there should be a space: "years old. I" — but keeping original.

intro_message = (
    f"Hello! my name is {name}, I'm {age} years old. I live in {city}. "
    f"I work as a {profession} and I absolutely enjoy {hobby} in my free time. "
    f"Nice to meet you!\n"
)


# ---------------------------------------------------------
# Step 4: Add Current Date
# ---------------------------------------------------------
# datetime.date.today() gets today's date.
# .isoformat() returns date in YYYY-MM-DD format (international standard).
# \n creates a newline before the date for visual separation.

current_date = datetime.date.today().isoformat()
intro_message += f"Logged on: {current_date}"


# ---------------------------------------------------------
# Step 5: Create Decorative Border
# ---------------------------------------------------------
# String multiplication: "*" * 80 creates 80 asterisks in a row.
# This is a clean way to create separators without loops.

border = "*" * 80


# ---------------------------------------------------------
# Step 6: Combine Everything and Display
# ---------------------------------------------------------
# Triple quotes not needed — we're just concatenating strings.
# \n at the beginning ensures the output starts on a fresh line.

final_output = f"{border}\n{intro_message}\n{border}"
print("\n" + final_output)


# ---------------------------------------------------------
# Bonus Features Demonstrated
# ---------------------------------------------------------
# 1. Date Logging: Helps track when the introduction was generated.
# 2. Border Decoration: Makes output visually appealing and professional.
# 3. Input Cleaning: Prevents formatting issues from accidental spaces.


# ---------------------------------------------------------
# Important Notes About This Implementation
# ---------------------------------------------------------
# 1. All inputs are stored as strings, even age. For mathematical
#    operations, age would need conversion: int(age).
#
# 2. .strip() only removes spaces from ends, not middle. "John   Doe"
#    becomes "John   Doe" (middle spaces preserved).
#
# 3. The intro_message uses \n at the end of first part to create
#    separation before the date line.
#
# 4. String multiplication (*) works with any string, not just asterisks.
#    Example: "-=" * 40 creates alternating dash-equal pattern.