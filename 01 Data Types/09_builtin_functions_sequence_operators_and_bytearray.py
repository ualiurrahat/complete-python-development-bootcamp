# ============================================================
# File: 09_builtin_functions_sequence_operators_and_bytearray.py
# Topic: Built-in Functions, Sequence Operators, and Bytearray
# ============================================================

# ------------------------------------------------------------
# 1. Built-in Functions: max() and min()
# ------------------------------------------------------------
# Python provides powerful built-in functions to operate on
# collections such as lists, tuples, sets, etc.
#
# max() → returns the largest element
# min() → returns the smallest element

measurement_values = [18, 1, 8, 1, 20, 1, 13, 1971, 2441139, -1122]

print(f"Maximum value in list: {max(measurement_values)}")
print(f"Minimum value in list: {min(measurement_values)}")

# ------------------------------------------------------------
# 2. Sequence Concatenation Using + Operator
# ------------------------------------------------------------
# The + operator can concatenate (join) two sequences
# such as lists, tuples, or strings.
#
# Important:
# + does NOT modify original lists — it creates a new list.

base_liquids = ["water", "milk"]
extra_flavors = ["ginger"]

complete_liquid_mix = base_liquids + extra_flavors
print(f"Combined liquid mixture: {complete_liquid_mix}")

# ------------------------------------------------------------
# 3. Sequence Repetition Using * Operator
# ------------------------------------------------------------
# The * operator repeats a sequence multiple times.
# This is extremely useful for creating repeated patterns.

brewing_cycle = ["black tea", "water"]

strong_brew_sequence = brewing_cycle * 3
print(f"Repeated brewing sequence: {strong_brew_sequence}")

# ------------------------------------------------------------
# 4. Bytearray — Mutable Byte Sequences
# ------------------------------------------------------------
# bytearray represents a sequence of bytes.
# Unlike 'bytes', bytearray is MUTABLE, meaning:
# → its contents can be changed after creation.
#
# bytearray is commonly used in:
# - Low-level data handling
# - File processing
# - Network programming
# - Binary protocols
# - Embedded systems

raw_spice_label = bytearray(b"CINNAMON")
print(f"Original bytearray data: {raw_spice_label}")

# ------------------------------------------------------------
# 5. Replacing Data Inside bytearray
# ------------------------------------------------------------
# replace(old, new) searches for a byte pattern
# and replaces it with another.
#
# Note:
# byte literals must start with prefix 'b'

raw_spice_label = raw_spice_label.replace(b"CINNA", b"CARD")
print(f"Modified bytearray data: {raw_spice_label}")

# ------------------------------------------------------------
# Summary:
# - max() and min() provide quick statistical operations.
# - + operator concatenates sequences.
# - * operator repeats sequences.
# - bytearray provides mutable byte-level data manipulation.
# ------------------------------------------------------------
