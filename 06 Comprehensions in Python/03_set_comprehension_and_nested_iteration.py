# ============================================================
# File: 03_set_comprehension_and_nested_iteration.py
# Chapter: 06 - Comprehensions in Python
# Topic: Set Comprehension and Nested Iteration
# ============================================================


# Problem Statement:
#
# In many programs we need to remove duplicate values
# from a collection or extract unique elements from
# nested data structures.
#
# Python provides **Set Comprehension** as a concise
# way to build sets directly from iterables.
#
# A set automatically stores **only unique values**,
# making it very useful when we want to eliminate
# duplicates from a dataset.
#
# In this file we will:
# 1. Create a set using a traditional loop
# 2. Create a set using a set comprehension
# 3. Perform a more complex task involving
#    nested iteration inside a comprehension



# ============================================================
# Step 1: Example Dataset
# ============================================================

favourite_chais = [
    "Masala Tea", "Green Tea", "Masala Tea",
    "Lemon Tea", "Green Tea", "Elaichi Tea"
]


# Notice that some tea names appear multiple times.
# Our goal is to extract only the **unique tea names**.



# ============================================================
# Step 2: Using Set Comprehension
# ============================================================

# General Syntax of Set Comprehension:
#
# {expression for item in iterable if condition}
#
# The condition part is optional.


unique_chai = {chai for chai in favourite_chais}


print("Unique Chais using comprehension:", unique_chai)


# Explanation:
#
# chai
#   -> The value that will be placed into the set
#
# for chai in favourite_chais
#   -> Iterates through each item in the list
#
# Because sets automatically remove duplicates,
# repeated tea names appear only once in the result.



# ============================================================
# Step 3: Using Traditional Loop
# ============================================================

unique_chai_using_loop = set()

for chai in favourite_chais:
    unique_chai_using_loop.add(chai)


print("Unique Chais using loop:", unique_chai_using_loop)


# Explanation:
#
# Here we manually create an empty set and
# add each element using the add() method.
#
# Both methods produce the same result.
#
# However, the comprehension version is shorter
# and easier to read once you are familiar with it.



# ============================================================
# Step 4: Complex Example (Nested Data)
# ============================================================

# In real-world programs data is often nested.
# For example, a dictionary may store recipes
# where each chai type contains multiple spices.


recipes = {
    "Masala Tea": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}


# Our goal:
# Extract all **unique spices** used across
# every recipe.



# ============================================================
# Step 5: Using Nested Set Comprehension
# ============================================================

unique_spices = {
    spice
    for ingredients in recipes.values()
    for spice in ingredients
}


print("Unique spices:", unique_spices)


# Explanation:
#
# recipes.values()
#   -> Returns all ingredient lists
#
# Example:
#
# [
#   ["ginger", "cardamom", "clove"],
#   ["cardamom", "milk"],
#   ["ginger", "black pepper", "clove"]
# ]
#
#
# for ingredients in recipes.values()
#   -> Iterates through each ingredient list
#
# for spice in ingredients
#   -> Iterates through each spice in the list
#
# spice
#   -> Each spice is added to the set
#
# Because sets store only unique values,
# duplicate spices automatically disappear.



# ============================================================
# Step 6: Traditional Loop Version (Nested Loops)
# ============================================================

unique_spices_using_loop = set()

for ingredients in recipes.values():
    for spice in ingredients:
        unique_spices_using_loop.add(spice)


print("Unique spices using loop:", unique_spices_using_loop)


# Explanation:
#
# This version performs the same logic using nested loops:
#
# 1. Iterate through each ingredient list
# 2. Iterate through each spice in that list
# 3. Add the spice to the set
#
# The comprehension version performs the same steps
# but in a much more compact and readable format.



# ============================================================
# Key Takeaways
# ============================================================

# 1. Set comprehensions create sets in a concise way.
#
# 2. Sets automatically remove duplicate values.
#
# 3. Comprehensions can contain multiple loops,
#    allowing them to work with nested data structures.
#
# 4. They provide a cleaner and more Pythonic
#    alternative to writing multiple nested loops.