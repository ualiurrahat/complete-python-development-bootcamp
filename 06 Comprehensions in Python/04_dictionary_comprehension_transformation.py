# ============================================================
# File: 04_dictionary_comprehension_transformation.py
# Chapter: 06 - Comprehensions in Python
# Topic: Dictionary Comprehension for Data Transformation
# ============================================================


# Problem Statement:
#
# In many real-world applications we need to transform data
# stored inside dictionaries. For example, converting prices
# from one currency to another.
#
# In this example, we have tea prices stored in Bangladeshi
# Taka (BDT), and our goal is to convert those prices to
# US Dollars (USD).
#
# We will use **Dictionary Comprehension** to perform this
# transformation in a concise and readable way.



# ============================================================
# Step 1: Original Dataset
# ============================================================

# Tea prices stored in Bangladeshi Taka (BDT)

tea_prices_bdt = {
    "Masala Tea": 80,
    "Green Tea": 150,
    "Lemon Tea": 360
}



# ============================================================
# Step 2: Dictionary Comprehension Syntax
# ============================================================

# General Syntax:
#
# { key_expression : value_expression
#   for item in iterable
#   if condition (optional)
# }


# In this case:
#
# key_expression   -> tea
# value_expression -> price / 120
#
# Here we assume:
# 1 USD ≈ 120 BDT



# ============================================================
# Step 3: Converting BDT to USD
# ============================================================

tea_prices_usd = {
    tea: price / 120
    for tea, price in tea_prices_bdt.items()
}


print(tea_prices_usd)



# ============================================================
# Explanation
# ============================================================

# tea_prices_bdt.items() returns key-value pairs from the
# dictionary.
#
# Example output of .items():
#
# [
#   ("Masala Tea", 80),
#   ("Green Tea", 150),
#   ("Lemon Tea", 360)
# ]


# During iteration Python unpacks each pair into two variables:
#
# tea   -> the dictionary key
# price -> the dictionary value


# For each pair, the comprehension creates a new entry:
#
# key   -> tea
# value -> price / 120
#
# So the dictionary is transformed into USD prices.


# ============================================================
# Final Result
# ============================================================

# {
#   'Masala Tea': 0.6667,
#   'Green Tea': 1.25,
#   'Lemon Tea': 3.0
# }


# ============================================================
# Why Dictionary Comprehension is Useful
# ============================================================

# Advantages:
#
# 1. Shorter and cleaner code
# 2. Efficient transformation of dictionary data
# 3. Widely used in real-world Python applications
#
# Without comprehension, the same task would require
# multiple lines using a traditional loop.