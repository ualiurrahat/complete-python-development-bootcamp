# ============================================================
# File: 07_break_and_continue_in_loops.py
# Chapter: 03 Loops
# Topic: Controlling Loop Execution using break and continue
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# You are checking available chai flavours in a tea shop.
#
# Task:
# - If a flavour is "Out of Stock", skip it.
# - If a flavour is "Discontinued", stop checking completely.
# - Otherwise, print that the flavour is available.
#
# This file introduces:
# - continue → skips current iteration
# - break → stops the loop entirely
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Create List of Flavours
# ------------------------------------------------------------

flavours = ["Ginger", "Out of Stock", "Lemon", 
            "Discontinued", "Tulsi"]


# ------------------------------------------------------------
# Step 2: Iterate and Control Loop Flow
# ------------------------------------------------------------

for flavour in flavours:

    # Skip unavailable flavour
    if flavour == "Out of Stock":
        continue

    # Stop loop if flavour is discontinued
    if flavour == "Discontinued":
        break

    print(f"{flavour} item found")


# ------------------------------------------------------------
# Step 3: Code Outside the Loop
# ------------------------------------------------------------

print("Outside of loop")


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# continue:
# - Skips the current iteration.
# - Moves directly to the next item in the loop.
#
# break:
# - Immediately terminates the loop.
# - Control moves to the code after the loop.
#
# Important:
# - "Tulsi" is never printed because the loop
#   stops when "Discontinued" is encountered.
# ------------------------------------------------------------
