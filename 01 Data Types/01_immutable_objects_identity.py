"""
Topic: Immutable Objects, Identity, and Reassignment in Python

Core Concepts Covered:
----------------------
1. Everything in Python is an object.
2. Every object has:
   - Identity  -> memory address (checked using id())
   - Type      -> data type (int, float, string, list, set, etc.)
   - Value     -> stored data
3. Immutable objects:
   - Their value cannot be changed after creation.
   - If you "change" the value, Python actually creates a new object.

This example demonstrates how immutable objects behave using integers.
"""

# ---------------------- Step 1: Variable Assignment ----------------------

# Assigning integer value 2 to variable 'sugar_amount'
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

# Assigning a new value (12) to the same variable name
# Since integers are IMMUTABLE, Python creates a NEW object for value 12
sugar_amount = 12
print(f"Second sugar: {sugar_amount}")


# ---------------------- Step 2: Object Identity ----------------------

# id() returns the unique identity (memory address) of an object

print(f"ID of integer object 2: {id(2)}")
print(f"ID of integer object 12: {id(12)}")


# ---------------------- Explanation ----------------------
"""
Key Understanding:

1. Everything in Python is an object:
   - 2 is an object
   - 12 is an object
   - sugar_amount is just a label (reference) pointing to an object

2. Integer objects are IMMUTABLE:
   - You cannot modify the value 2 to become 12.
   - Instead, Python creates a new object with value 12.
   - Then, the variable 'sugar_amount' is redirected to point to this new object.

3. Identity check:
   - The IDs of 2 and 12 are different.
   - This proves that Python created two separate objects.

Conclusion:
-----------
If reassignment changes the object's identity (id),
then the object type is IMMUTABLE.
"""
