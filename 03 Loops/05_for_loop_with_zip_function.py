# ============================================================
# File: 05_for_loop_with_zip_function.py
# Chapter: 03 Loops
# Topic: Iterating Over Multiple Lists Using zip()
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# You are preparing a daily order summary for a tea shop.
#
# Task:
# - Store customer names in one list.
# - Store their corresponding bill amounts in another list.
# - Print the summary in the format:
#
#     "[Name] paid $[amount]"
#
# Previously, we learned how to iterate over:
# - Numbers (range)
# - Single lists
# - Indexed lists (enumerate)
#
# In this file, we learn how to iterate over
# multiple lists at the same time using zip().
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Create Two Related Lists
# ------------------------------------------------------------

names = ["Rahat", "Nabila", "Tamanna", "Shithi", "Maria", "Rebecca"]
bills = [10, 500, 35, 70, 89, 200]


# ------------------------------------------------------------
# Step 2: Use zip() for Parallel Iteration
# ------------------------------------------------------------
# zip(list1, list2)
#
# - Combines elements from both lists into pairs.
# - Stops when the shortest list ends.
#
# Each iteration returns:
# (element_from_list1, element_from_list2)

for name, amount in zip(names, bills):
    print(f"{name} paid ${amount}")


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - zip() pairs corresponding elements together.
# - No manual indexing is required.
# - This is the cleanest way to process related data
#   stored in separate lists.
#
# Example pairing:
# Rahat  → 10
# Nabila → 500
#
# This technique is commonly used in real-world data processing.
# ------------------------------------------------------------
