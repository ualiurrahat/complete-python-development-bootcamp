"""
Topic: Floating-Point Precision & Understanding Imports

Core Concepts Covered:
----------------------
1. Floating-point precision issues
2. Why decimal calculations can be inaccurate
3. Importing Python modules
4. Introduction to sys, decimal, and fractions modules

This file explains WHY floating-point numbers behave strangely.
"""

# ---------------------- Importing Modules ----------------------

import sys
from fractions import Fraction
from decimal import Decimal

# Explanation:
# 'import' allows us to use external functionality.
#
# sys        → gives system-level information
# Fraction   → provides exact rational arithmetic
# Decimal    → provides precise decimal arithmetic

# ---------------------- Floating Point Precision Problem ----------------------

ideal_temperature = 95.5
measured_temperature = 95.49

print(f"Ideal temperature: {ideal_temperature}")
print(f"Measured temperature: {measured_temperature}")
print(f"Difference: {ideal_temperature - measured_temperature}")

# Expected difference: 0.01
# Actual output: something like 0.00999999999999801

# Why does this happen?

"""
Computers store floating-point numbers in BINARY (base-2),
but decimal fractions often cannot be represented exactly in binary.

Just like:
1/3 = 0.333333333... (infinite)

Some decimal numbers become infinite binary fractions.

So Python stores an approximation, causing small precision errors.
"""

# ---------------------- Large Decimal Precision Example ----------------------

large_decimal = 96.24411391834343
small_decimal = 3.00000000000001

print(f"Large value: {large_decimal}")
print(f"Small value: {small_decimal}")
print(f"Difference: {large_decimal - small_decimal}")

# You may notice tiny precision inaccuracies again.

# ---------------------- System Float Precision ----------------------

print(sys.float_info)

# Explanation:
# This shows the system limits for floating-point calculations.
# It tells us:
# - Max precision
# - Max/min representable float
# - Floating-point accuracy limits

# ---------------------- Why Decimal & Fraction Exist ----------------------

"""
If exact precision is REQUIRED (e.g., financial systems),
we use:

Decimal  → exact decimal arithmetic
Fraction → exact rational arithmetic

Example use cases:
- Banking systems
- Scientific measurement
- High precision calculations
"""
