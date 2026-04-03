"""
File: 03_attribute_shadowing_and_fallback.py
Chapter: Object Oriented Programming In Python
Topic: Attribute Shadowing, Object Namespace, and Fallback to Class Namespace
Problem Statement:
Understand how attribute shadowing works in Python. Learn how an object
can override (shadow) a class attribute, and how deleting the object’s
attribute makes Python fall back to the class attribute. Also observe
what happens when no fallback exists.
"""

# ---------------------- Step 1: Defining a Class with Class Attributes ----------------------
# These attributes belong to the class namespace.
# All objects created from this class can access them.

class Tea:
    temperature = "hot"
    strength = "Strong"


# ---------------------- Step 2: Creating an Object ----------------------
cutting = Tea()

# The object does NOT have its own 'temperature' yet.
# So Python looks into the class namespace and finds it there.
print(cutting.temperature)  # hot


# ---------------------- Step 3: Shadowing the Class Attribute ----------------------
# Now changing the temperature using the object.
# This does NOT change the class attribute.
# Instead, Python creates a NEW attribute in the object's namespace.
# This is called ATTRIBUTE SHADOWING.

cutting.temperature = "Mild"
cutting.cup = "small"  # adding a completely new attribute to the object

print(f"After changing value: {cutting.temperature}")
print(f"Direct look into the class for temperature value: {Tea.temperature}")


# ---------------------- Step 4: Deleting the Shadowed Attribute ----------------------
# When deleting 'temperature' from the object,
# only the object's own version is deleted.
# The class attribute still exists.

del cutting.temperature

# Now when accessing 'temperature', Python cannot find it in the object.
# So it FALLS BACK to the class namespace.
# This fallback behavior is part of attribute lookup order in Python.
print(cutting.temperature)  # Falls back to Tea.temperature


# ---------------------- Step 5: Behavior When No Fallback Exists ----------------------
# The 'cup' attribute was created ONLY inside the object.
# It does NOT exist in the class.

print(f"Cup size is: {cutting.cup}")

# Deleting the object-only attribute
del cutting.cup

# Now trying to access 'cup' will raise an error.
# Because Python searches:
# 1) Object namespace -> Not found
# 2) Class namespace  -> Not found
# So Python raises AttributeError.

# Uncommenting the line below will produce:
# AttributeError: 'Tea' object has no attribute 'cup'
# print(cutting.cup)