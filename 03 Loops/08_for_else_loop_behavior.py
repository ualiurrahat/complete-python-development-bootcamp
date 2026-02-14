# ============================================================
# File: 08_for_else_loop_behavior.py
# Chapter: 03 Loops
# Topic: Understanding for-else Loop Behavior in Python
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# You have a list of staff members with their ages.
#
# Task:
# Check if anyone is older than 18 and eligible
# to manage the staff.
#
# If someone is eligible:
#     Print eligibility message and stop checking.
#
# If no one is eligible:
#     Print "No one is eligible to manage the staff".
#
# This file explains the difference between:
# 1) if-else inside a loop
# 2) for-else structure
# ------------------------------------------------------------


# ------------------------------------------------------------
# Case 1: if-else Inside the Loop
# ------------------------------------------------------------

staff = [("Alamin", 16), ("Prince", 14), ("Shah", 17)]

for name, age in staff:
    if age > 18:
        print(f"{name} is eligible to manage the staff")
        break
    else:
        print(" Case 1: No one is eligible to manage the staff")


# ------------------------------------------------------------
# Explanation of Case 1:
# ------------------------------------------------------------
# - The else belongs to the if condition.
# - So it runs every time age <= 18.
#
# Since all ages are below 18:
# The else statement runs 3 times.
#
# Output:
# No one is eligible...
# No one is eligible...
# No one is eligible...
#
# This is normal if-else behavior.
# ------------------------------------------------------------



# ------------------------------------------------------------
# Case 2: for-else Structure
# ------------------------------------------------------------

staff = [("Alamin", 16), ("Prince", 14), ("Shah", 17)]

for name, age in staff:
    if age > 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(" Case 2: No one is eligible to manage the staff")


# ------------------------------------------------------------
# Explanation of Case 2:
# ------------------------------------------------------------
# Here, the else belongs to the FOR loop,
# not the if statement.
#
# In Python:
# A for-loop's else block executes only if:
# - The loop completes normally
# - AND no break statement was triggered
#
# Since no one is older than 18:
# - The loop finishes completely
# - break never runs
# - So the for-else executes once
#
# Output:
# No one is eligible to manage the staff
#
# It runs only once because it is attached
# to the loop, not to each iteration.
# ------------------------------------------------------------
