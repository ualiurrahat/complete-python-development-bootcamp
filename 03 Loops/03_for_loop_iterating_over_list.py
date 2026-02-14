# ============================================================
# File: 03_for_loop_iterating_over_list.py
# Chapter: 03 Loops
# Topic: Iterating Over a List Using for Loop
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# A chai shop receives multiple customer orders.
#
# Task:
# - Store customer names in a list.
# - Print the order queue using a loop.
#
# Output format:
#     "Order ready for [name]"
#
# Previously, we used range() to loop through numbers.
# In this file, we loop directly over elements inside a list.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Create a List of Orders
# ------------------------------------------------------------
# A list stores multiple values in a single variable.

orders = ["rahat", "ayon", "minul", "nasim", "shohan", "nabila", "tamanna"]


# ------------------------------------------------------------
# Step 2: Iterate Directly Over the List
# ------------------------------------------------------------
# Instead of looping over numbers,
# we loop over actual elements in the list.

for name in orders:
    print(f"Order ready for {name}")


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - The loop runs once for each item in the list.
# - 'name' stores the current list element in each iteration.
# - No indexing is needed.
#
# This is called sequence iteration.
# It is cleaner and more Pythonic than using indexes.
# ------------------------------------------------------------
