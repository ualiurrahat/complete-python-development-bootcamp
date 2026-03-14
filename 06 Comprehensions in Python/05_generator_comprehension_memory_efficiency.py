# ============================================================
# File: 05_generator_comprehension_memory_efficiency.py
# Chapter: 06 - Comprehensions in Python
# Topic: Generator Comprehensions and Memory Efficiency
# ============================================================


# Problem Statement:
#
# When working with very large datasets, storing all values
# in memory at once may not be efficient. Python provides
# **Generator Comprehensions** to handle such situations.
#
# Generators produce values **one at a time** instead of
# creating the entire collection in memory.
#
# This approach helps save memory and is commonly used when
# processing large data streams.



# ============================================================
# List Comprehension vs Generator Comprehension
# ============================================================

# Syntax Comparison:
#
# List Comprehension:
# [expression for item in iterable if condition]
#
# Generator Comprehension:
# (expression for item in iterable if condition)


# Key Difference:
#
# [x for x in items]
# -> Creates the entire list in memory immediately
#
# (x for x in items)
# -> Produces one value at a time when needed
#
# Because generators produce values lazily,
# they behave more like a **data stream**.



# ============================================================
# Example Dataset
# ============================================================

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

# This list represents the number of chai cups sold each day.



# ============================================================
# Step 1: Creating a Generator
# ============================================================

total_cups = (sale for sale in daily_sales if sale > 5)

print(total_cups)


# Output example:
#
# <generator object <genexpr> at 0x...>
#
# Explanation:
#
# A generator does not immediately compute the values.
# Instead, it creates a generator object that will
# produce values **only when they are requested**.



# ============================================================
# Why Generators Behave This Way
# ============================================================

# Generators must be **consumed** to produce values.
#
# This means we need to iterate through them or use
# functions like:
#
# - sum()
# - list()
# - max()
# - min()
# - for loops
#
# These operations pull values from the generator
# one by one.



# ============================================================
# Comparison with List Comprehension
# ============================================================

# Example list comprehension:

# total_cups_list = [sale for sale in daily_sales if sale > 5]

# This would immediately produce:

# [10, 12, 7, 8, 9, 15]

# The entire list is created and stored in memory.



# ============================================================
# Practical Use Case of Generators
# ============================================================

# Generators are especially useful when working with:
#
# - large files
# - large datasets
# - streaming data
# - pipelines of transformations


# Here we calculate the total cups sold where
# the number of cups sold is greater than 5.


total_cups_sum = sum(
    sale for sale in daily_sales if sale > 5
)

print(total_cups_sum)



# ============================================================
# Explanation of the Generator Expression
# ============================================================

# sale for sale in daily_sales if sale > 5
#
# sale
# -> the value produced by the generator
#
# for sale in daily_sales
# -> iterates through each item in the list
#
# if sale > 5
# -> filters only the values greater than 5
#
# The sum() function then consumes the generator
# and adds each value one by one.



# ============================================================
# Key Takeaways
# ============================================================

# 1. Generator comprehensions use parentheses ().
#
# 2. They produce values lazily (one at a time).
#
# 3. They are more memory efficient than list comprehensions.
#
# 4. They are commonly used with functions like sum(),
#    max(), min(), and iteration loops.