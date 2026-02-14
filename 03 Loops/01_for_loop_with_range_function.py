# ============================================================
# File: 01_for_loop_with_range_function.py
# Chapter: 03 Loops
# Topic: Introduction to for Loop using range()
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# A tea stall owner uses a digital token display system.
#
# Task:
# For every customer waiting in line, generate a token number
# from 1 to 10 and display a message:
#
#     "Serving chai to Token #[number]"
#
# This introduces:
# - for loop
# - range() function
# - Iteration in Python
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Understanding range()
# ------------------------------------------------------------
# range(start, stop)
#
# - start → starting number (inclusive)
# - stop  → ending number (exclusive)
#
# range(1, 11) generates numbers:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


# ------------------------------------------------------------
# Step 2: Using a for Loop
# ------------------------------------------------------------
# A for loop is used to iterate over a sequence.
#
# Syntax:
# for variable in sequence:
#     block of code

for token in range(1, 11):
    print(f"Serving chai to Token #{token}")


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - The loop runs 10 times.
# - Each time, 'token' stores the current number.
# - The print statement executes for every iteration.
#
# Output:
# Serving chai to Token #1
# Serving chai to Token #2
# ...
# Serving chai to Token #10
#
# This is the foundation of iteration in Python.
# ------------------------------------------------------------
