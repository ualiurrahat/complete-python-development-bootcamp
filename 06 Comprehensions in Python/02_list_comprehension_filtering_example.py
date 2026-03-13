# ============================================================
# File: 02_list_comprehension_filtering_example.py
# Chapter: 06 - Comprehensions in Python
# Topic: Filtering Data Using List Comprehension
# ============================================================


# Problem Statement:
#
# We have a tea shop menu containing different types of tea.
# Our task is to extract only the iced tea items from the menu.
#
# We will solve this problem in two ways:
#
# 1. Using a traditional loop
# 2. Using a List Comprehension
#
# This will help us understand how comprehensions simplify
# common data filtering operations.



# ============================================================
# Step 1: Create the Menu
# ============================================================

menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]



# ============================================================
# Step 2: Filtering Using a Traditional Loop
# ============================================================

# Here we manually iterate through each item of the menu
# and check if the word "Iced" exists inside the tea name.

iced_tea_using_loop = []

for tea in menu:

    # Check condition
    if "Iced" in tea:

        # Add matching item to the result list
        iced_tea_using_loop.append(tea)


print(f"Iced Tea using loop: {iced_tea_using_loop}")


# Explanation:
#
# The loop performs the following steps:
#
# 1. Iterate through every item in the menu list
# 2. Check if the string "Iced" is present
# 3. If the condition is True, append the item
#    to the result list
#
# Final Result:
#
# ['Iced Lemon Tea', 'Iced Peach Tea']



# ============================================================
# Step 3: Filtering Using List Comprehension
# ============================================================

# Python provides a shorter and cleaner syntax to perform
# the same operation using a List Comprehension.


# General Syntax:
#
# [expression for item in iterable if condition]


iced_tea_using_comprehension = [
    tea for tea in menu if "Iced" in tea
]


print(f"Iced Tea using comprehensions: {iced_tea_using_comprehension}")


# Explanation of Each Part:
#
# tea
#   -> This is the value that will be added to the new list
#
# for tea in menu
#   -> Iterates through each element in the menu list
#
# if "Iced" in tea
#   -> Filters only the items that contain the word "Iced"
#
#
# So internally Python performs something conceptually similar to:
#
# result = []
# for tea in menu:
#     if "Iced" in tea:
#         result.append(tea)



# ============================================================
# Why List Comprehension is Preferred
# ============================================================

# Advantages:
#
# 1. Shorter code
# 2. More readable once familiar with the syntax
# 3. Often slightly faster than traditional loops
#
# Because of these advantages, list comprehensions are
# widely used in professional Python codebases.



# ============================================================
# Final Result
# ============================================================

# Both approaches produce the same output:
#
# ['Iced Lemon Tea', 'Iced Peach Tea']
#
# The comprehension version simply achieves the same
# result in a more concise and Pythonic way.