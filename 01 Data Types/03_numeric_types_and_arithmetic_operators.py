"""
Topic: Numeric Data Types & Arithmetic Operators in Python

Core Concepts Covered:
----------------------
1. Integer arithmetic operations
2. Unique Python features:
   - Floor division (//)
   - Modulus (%)
   - Exponentiation (**)
   - Large number readability using underscore (_)
3. How arithmetic operators work internally

This file demonstrates how Python handles numeric calculations in real-life scenarios.
"""

# ---------------------- Addition (+) ----------------------

# Total tea ingredients in grams
tea_leaves_grams = 18
ginger_grams = 4

total_ingredients = tea_leaves_grams + ginger_grams
print(f"Total ingredients used: {total_ingredients} grams")

# Explanation:
# 18 + 4 = 22
# The '+' operator performs arithmetic addition.

# ---------------------- Subtraction (-) ----------------------

remaining_tea_leaves = tea_leaves_grams - ginger_grams
print(f"Remaining tea leaves: {remaining_tea_leaves} grams")

# Explanation:
# 18 - 4 = 14
# '-' subtracts the right operand from the left operand.

# ---------------------- Division (/) ----------------------

total_milk_liters = 6
cups = 4

milk_per_cup = total_milk_liters / cups
print(f"Milk per cup: {milk_per_cup} liters")

# Explanation:
# '/' ALWAYS produces a floating-point result in Python
# 6 / 4 = 1.5

# ---------------------- Floor Division (//) ----------------------

tea_bags = 9
pots = 4

bags_per_pot = tea_bags // pots
print(f"Tea bags per pot (floor division): {bags_per_pot}")

# Explanation:
# '//' divides and returns ONLY the integer part (quotient).
# 9 // 4 = 2   (not 2.25)

# This is VERY useful when:
# - Distributing items evenly
# - Grouping
# - Chunking data

# ---------------------- Modulus (%) ----------------------

total_spices = 11
cups = 3

leftover_spices = total_spices % cups
print(f"Leftover spices: {leftover_spices}")

# Explanation:
# '%' gives the remainder after division.
# 11 % 3 = 2

# This is extremely useful for:
# - Checking even/odd numbers
# - Cyclic patterns
# - Remainder calculations

# ---------------------- Exponentiation (**) ----------------------

base_flavor = 3
intensity_scale = 4

flavor_power = base_flavor ** intensity_scale
print(f"Flavor intensity scale: {flavor_power}")

# Explanation:
# '**' performs power calculation.
# 3 ** 4 = 3 × 3 × 3 × 3 = 81

# ---------------------- Large Numbers with Underscore ----------------------

# Python allows underscores inside numbers for readability.
# This does NOT change the value.

total_tea_leaves_collected = 1_250_000_000
print(f"Total tea leaves collected: {total_tea_leaves_collected}")

# Explanation:
# 1_250_000_000 is the same as 1250000000
# The underscore improves human readability for large numbers.

# This feature is UNIQUE and extremely useful for:
# - Financial data
# - Scientific calculations
# - Large datasets
