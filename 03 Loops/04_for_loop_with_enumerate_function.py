# ============================================================
# File: 04_for_loop_with_enumerate_function.py
# Chapter: 03 Loops
# Topic: Using enumerate() to Access Index and Value
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# You are designing a digital tea menu board.
#
# Task:
# - Store menu items in a list.
# - Display each item with a serial number.
#
# Output format:
#     1 : Green Tea
#     2 : Lemon Tea
#     ...
#
# Previously, we iterated over list elements.
# In this file, we learn how to access both:
#   - The index (position)
#   - The value (actual item)
# simultaneously using enumerate().
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Create the Menu List
# ------------------------------------------------------------

menu = ["Green Tea", "Lemon Tea", "Spiced Tea", 
        "Mint Tea", "Milked Tea", "Ginger Tea"]


# ------------------------------------------------------------
# Step 2: Use enumerate() for Indexed Iteration
# ------------------------------------------------------------
# enumerate(sequence, start)
#
# - sequence → iterable object (list)
# - start → starting index number (default is 0)
#
# It returns:
# (index, element) pair in each iteration

for index, item in enumerate(menu, start=1):
    print(f"{index} : {item}")


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - enumerate() automatically provides index and value.
# - No need to manually track counter variables.
# - start=1 ensures numbering begins from 1 instead of 0.
#
# This is the cleanest and most Pythonic way
# to print numbered lists.
# ------------------------------------------------------------
