
"""
File: 06_strings_indexing_slicing_encoding.py
Topic: Python String Fundamentals

This script demonstrates:
1. Basic string usage and formatted printing
2. String indexing and slicing techniques
3. Step-based slicing
4. String reversal using slicing
5. UTF-8 encoding and decoding of strings

"""

# ---------------------- Basic String Usage ----------------------

# Declaring string variables
chai_type = "Ginger chai"
customer_name = "Nabila"

# Using f-string for formatted output
print(f"Order for {customer_name}: {chai_type} please!")


# ---------------------- String Indexing & Slicing ----------------------

# String to demonstrate slicing operations
chai_description = "Aromatic and Bold"

# Extracting substring from index 0 to 7 (8 is excluded)
print(f"First word: {chai_description[0:8:1]}")
# Explanation:
# - Start index = 0
# - End index = 8 (exclusive)
# - Step = 1 → take every character


# Same slicing without explicitly specifying the step
print(f"First word: {chai_description[0:8]}")
# Default step value is 1


# Omitting the starting index defaults it to 0
print(f"First word: {chai_description[:8]}")
# Cleaner and more pythonic approach


# Taking every second character from index 0 to 7
print(f"First word (every 2nd char): {chai_description[0:8:2]}")
# Step = 2 → skips every alternate character


# Extracting substring from index 12 till the end
print(f"Last word: {chai_description[12:]}")
# If end index is omitted, slicing continues till the end of the string


# Reversing the entire string using negative step slicing
print(f"Reversed string: {chai_description[::-1]}")
# Step = -1 → traverses the string backwards


# ---------------------- Encoding & Decoding ----------------------

# String containing special Unicode characters
label_text = "Chai Spécial"

# Encoding the string into UTF-8 byte format
encoded_label = label_text.encode("utf-8")

print(f"Original label: {label_text}")
print(f"Encoded label: {encoded_label}")

# Decoding the UTF-8 encoded bytes back into string
decoded_label = encoded_label.decode("utf-8")

print(f"Decoded label: {decoded_label}")
