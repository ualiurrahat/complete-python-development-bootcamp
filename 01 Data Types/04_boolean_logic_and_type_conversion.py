"""
Topic: Boolean Logic, Type Conversion & Logical Operators

Core Concepts Covered:
----------------------
1. Boolean values (True / False)
2. Type conversion (int → bool)
3. Logical operators:
   - and
   - or
   - not
4. Implicit type casting (upcasting)

This file demonstrates how Python evaluates logical expressions.
"""

# ---------------------- Boolean & Integer Interaction ----------------------

is_water_hot = True
stirring_steps = 6

total_steps = stirring_steps + is_water_hot
print(f"Total preparation steps: {total_steps}")

# Explanation:
# True is treated as 1
# False is treated as 0
# So:
# 6 + True = 6 + 1 = 7
#
# This automatic conversion is called:
# → Implicit Type Casting / Upcasting

# ---------------------- Boolean Conversion using bool() ----------------------

milk_quantity = 0  # No milk present

print(f"Is milk present? {bool(milk_quantity)}")

# Explanation:
# bool(0) → False
# bool(non-zero) → True
#
# General Rule:
# 0, None, empty strings, empty lists → False
# Everything else → True

# ---------------------- Logical AND Operator ----------------------

water_ready = True
tea_leaves_added = True

can_serve_tea = water_ready and tea_leaves_added
print(f"Can serve tea? {can_serve_tea}")

# Explanation:
# AND operator returns True only if BOTH conditions are True.
#
# True and True → True
# True and False → False
# False and True → False
# False and False → False

# This is widely used in:
# - Condition checks
# - Permission validation
# - Control flow logic
