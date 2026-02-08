# ============================================================
# File: 03_elif_ladder_and_multi_condition_handling.py
# Topic: elif Ladder and Multi-Condition Decision Making
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# Build a billing system for a tea shop.
#
# Task:
# - Ask the user to confirm the cup size.
# - Based on the selected size, display the corresponding bill.
#
# Cup size and price mapping:
#   Small  → $10
#   Medium → $15
#   Large  → $20
#
# If the user enters an invalid size, display an error message.
#
# This introduces:
# - if → elif → else ladder
# - Multi-condition decision flow
# - User input validation
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Take User Input
# ------------------------------------------------------------
# input() captures the user’s entry.
# lower() ensures consistent lowercase comparison.

chai_size = input("Please confirm your cup size (Small / Medium / Large): ").lower()


# ------------------------------------------------------------
# Step 2: Apply Conditional Decision Logic
# ------------------------------------------------------------
# elif ladder checks multiple conditions sequentially.
# The first True condition gets executed.

if chai_size == "small":
    print("Your bill is $10")

elif chai_size == "medium":
    print("Your bill is $15")

elif chai_size == "large":
    print("Your bill is $20")

else:
    print("Unknown cup size! Please choose Small, Medium, or Large.")


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Python checks conditions from top to bottom.
# - Once a matching condition is found, remaining checks are skipped.
#
# Execution flow:
#   1) Check small
#   2) If not matched → check medium
#   3) If not matched → check large
#   4) If none match → execute else
#
# This structure allows clean handling of multiple conditions.
# ------------------------------------------------------------
