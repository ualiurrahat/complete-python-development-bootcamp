# ============================================================
# File: 01_basic_if_statement_and_boolean_check.py
# Topic: Introduction to Conditional Statements using if
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# We want to simulate a simple real-life condition.
#
# Task:
# Check whether a kettle has finished boiling water.
# If the kettle is boiled, print a message indicating that
# it is time to prepare tea (chai).
#
# This introduces:
# - Boolean data type (True / False)
# - if conditional statement
# - Basic decision-making logic
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Define a Boolean Condition
# ------------------------------------------------------------
# Boolean variables store either True or False.
# Here, we use it to represent the state of the kettle.

is_kettle_boiled = True


# ------------------------------------------------------------
# Step 2: Apply the if Condition
# ------------------------------------------------------------
# The if statement executes the indented block only when
# the condition evaluates to True.

if is_kettle_boiled:
    print("Kettle is boiled! Time to make chai ☕")


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - If is_kettle_boiled is True → print statement runs.
# - If is_kettle_boiled is False → nothing is printed.
#
# This demonstrates how Python makes decisions using conditions.
# ------------------------------------------------------------
