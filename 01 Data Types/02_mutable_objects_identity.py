"""
Topic: Mutable Objects, Identity, and In-place Modification in Python

Core Concepts Covered:
----------------------
1. Mutable objects can be changed after creation.
2. Their identity remains the same even after modification.
3. Example: set, list, dictionary

This example demonstrates how mutable objects behave using a set.
"""

# ---------------------- Step 1: Create Empty Set ----------------------

spice_mix = set()

print(f"Initial spice mix: {spice_mix}")
print(f"Initial spice mix ID: {id(spice_mix)}")


# ---------------------- Step 2: Modify the Object ----------------------

# Adding elements to the same set object
spice_mix.add("Ginger")
spice_mix.add("Cardamom")
spice_mix.add("Lemon")

print(f"Updated spice mix: {spice_mix}")
print(f"Updated spice mix ID: {id(spice_mix)}")


# ---------------------- Explanation ----------------------
"""
Key Understanding:

1. 'set' is a MUTABLE object:
   - We modified the same object by adding elements.
   - No new object was created.

2. Identity Check:
   - The ID before and after modification is SAME.
   - This proves that the same object was modified in memory.

3. Why identity check is important:
   - We CANNOT determine mutability using values.
   - We MUST check object identity using id().

Conclusion:
-----------
If modification keeps the object's identity unchanged,
then the object type is MUTABLE.
"""
