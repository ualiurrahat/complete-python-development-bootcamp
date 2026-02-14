# ============================================================
# File: 06_while_loop_with_condition_control.py
# Chapter: 03 Loops
# Topic: Using while Loop for Condition-Based Iteration
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# You want to simulate the heating process of tea.
#
# Task:
# - Temperature starts at 40°C.
# - Tea boils at 100°C.
# - Increase temperature by 15°C in each step.
# - Print the temperature at every stage.
# - Stop when temperature reaches or exceeds 100°C.
#
# Previously, we used for loops (fixed iterations).
# In this file, we use a while loop,
# which runs based on a condition.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Initialize Starting Temperature
# ------------------------------------------------------------

temperature = 40


# ------------------------------------------------------------
# Step 2: Use while Loop for Condition-Based Repetition
# ------------------------------------------------------------
# while condition:
#     execute block
#
# The loop continues as long as the condition is True.

while temperature < 100:
    print(f"Current Temperature: {temperature}")

    # Increase temperature by 15 degrees
    temperature += 15


# ------------------------------------------------------------
# Step 3: Final Message After Loop Ends
# ------------------------------------------------------------

print("Tea is ready to boil")


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - The loop runs while temperature is less than 100.
# - Each iteration increases temperature by 15.
# - When temperature becomes 100 or more,
#   the condition becomes False and the loop stops.
#
# This is called condition-controlled iteration.
# ------------------------------------------------------------
