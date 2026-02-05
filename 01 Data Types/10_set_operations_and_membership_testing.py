# ============================================================
# File: 10_set_operations_and_membership_testing.py
# Topic: Set Data Type, Set Algebra, and Membership Testing
# ============================================================

# ------------------------------------------------------------
# 1. Creating Sets
# ------------------------------------------------------------
# A set is an unordered collection of UNIQUE elements.
#
# Key characteristics of sets:
# - No duplicate values allowed
# - Unordered (no indexing)
# - Highly optimized for fast membership testing
# - Supports mathematical set operations

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# ------------------------------------------------------------
# 2. Union of Sets ( | Operator )
# ------------------------------------------------------------
# Union returns ALL unique elements from both sets.
#
# Syntax:
#   setA | setB
#
# Mathematical meaning:
#   A ∪ B

all_spices = essential_spices | optional_spices
print(f"All spices (union): {all_spices}")

# ------------------------------------------------------------
# 3. Intersection of Sets ( & Operator )
# ------------------------------------------------------------
# Intersection returns ONLY the elements common to both sets.
#
# Syntax:
#   setA & setB
#
# Mathematical meaning:
#   A ∩ B

common_spices = essential_spices & optional_spices
print(f"Common spices (intersection): {common_spices}")

# ------------------------------------------------------------
# 4. Difference of Sets ( - Operator )
# ------------------------------------------------------------
# Difference returns elements that exist in the first set
# but NOT in the second set.
#
# Syntax:
#   setA - setB
#
# Mathematical meaning:
#   A − B

unique_essential_spices = essential_spices - optional_spices
print(f"Only in essential spices (difference): {unique_essential_spices}")

# ------------------------------------------------------------
# 5. Membership Testing Using 'in'
# ------------------------------------------------------------
# Sets are extremely fast for membership testing.
#
# Syntax:
#   element in set
#
# Returns:
#   True  → if element exists
#   False → if element does not exist

print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}")
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")

# ------------------------------------------------------------
# Summary:
# - Sets store unique elements.
# - | → union
# - & → intersection
# - - → difference
# - 'in' → membership testing (very fast in sets)
# ------------------------------------------------------------
