# ============================================================
# File: 07_tuple_unpacking_and_membership.py
# Topic: Tuples, Unpacking, Swapping, and Membership Testing
# ============================================================

# ------------------------------------------------------------
# 1. Creating a Tuple
# ------------------------------------------------------------
# A tuple is an ordered collection of elements.
# Tuples are IMMUTABLE, meaning once created, their values
# cannot be changed, added, or removed.

masala_spices = ("cardamom", "cloves", "cinnamon")

# ------------------------------------------------------------
# 2. Tuple Unpacking (Multiple Assignment)
# ------------------------------------------------------------
# Tuple unpacking allows assigning multiple variables at once
# from a tuple. Each variable gets the corresponding value
# based on position (index).

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

# ------------------------------------------------------------
# 3. Implicit Tuple Packing (Without Parentheses)
# ------------------------------------------------------------
# Python allows creating tuples without explicitly using ()
# This is known as tuple packing.

ginger_ratio, cardamom_ratio = 2, 1
# Internally, Python treats this as:
# (ginger_ratio, cardamom_ratio) = (2, 1)

print(f"Initial ratio -> Ginger: {ginger_ratio}, Cardamom: {cardamom_ratio}")

# ------------------------------------------------------------
# 4. Swapping Values Using Tuple Unpacking (Pythonic Way)
# ------------------------------------------------------------
# Python provides a clean and elegant way to swap values
# without using a temporary variable.

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio

print(f"After swapping -> Ginger: {ginger_ratio}, Cardamom: {cardamom_ratio}")

# ------------------------------------------------------------
# 5. Membership Testing Using 'in' Operator
# ------------------------------------------------------------
# The 'in' keyword checks whether a value exists inside a
# sequence (tuple, list, string, etc.).
# It always returns a Boolean: True or False.

print(f"Is 'cinnamon' in masala_spices? {'cinnamon' in masala_spices}")

# ------------------------------------------------------------
# 6. Case Sensitivity in Membership Testing
# ------------------------------------------------------------
# Python is CASE-SENSITIVE.
# That means 'cinnamon' and 'Cinnamon' are treated as
# completely different strings.

print(f"Is 'Cinnamon' in masala_spices? {'Cinnamon' in masala_spices}")

# ------------------------------------------------------------
# Summary:
# - Tuples are immutable ordered collections.
# - Tuple unpacking allows multiple assignment in one line.
# - Python supports elegant value swapping using tuples.
# - Membership testing using 'in' is simple and powerful.
# - String comparisons are case-sensitive.
# ------------------------------------------------------------
