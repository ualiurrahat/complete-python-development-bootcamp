"""
File: 03_attribute_shadowing_and_fallback.py
Chapter: 09 — Object Oriented Programming in Python
Topic: Attribute Shadowing, Object Namespace, and Fallback to Class Namespace

Problem Statement
-----------------
In Python, when an object and its class both have an attribute with the
same name, the object's version takes priority. This is called attribute
shadowing — the object's attribute shadows (hides) the class attribute
during lookup.

However, if the object's shadowing attribute is deleted, Python does not
raise an error immediately. Instead, it falls back to the class namespace
and returns the class attribute if one exists there.

Understanding this lookup order is essential for working confidently
with classes and objects in Python.

This file demonstrates:
1. How an object accesses a class attribute when it has no own copy.
2. How assigning a value to an object creates a shadow attribute.
3. How the class attribute remains unchanged after shadowing.
4. How deleting the shadow attribute triggers fallback to the class.
5. What happens when no fallback exists and an AttributeError is raised.

Key Concepts
------------
Attribute Shadowing
    When an object has its own attribute with the same name as a class
    attribute, the object's version takes priority during lookup.
    The class attribute is not deleted — it is simply hidden (shadowed).

Attribute Lookup Order
    When accessing an attribute on an object, Python searches in this order:
    1. The object's own namespace (instance namespace)
    2. The class namespace
    3. Parent class namespaces (inheritance chain)
    If not found anywhere, Python raises an AttributeError.

Fallback
    When the object's attribute is deleted, Python can no longer find it
    in the object namespace and automatically falls back to the class
    namespace to find the attribute there.

AttributeError
    An exception raised when Python cannot find an attribute in either
    the object's namespace or the class namespace.

del
    A Python keyword used to delete a variable, attribute, or object
    from its namespace.
"""

# ---------------------------------------------------------
# Step 1: Defining a Class with Class Attributes
# ---------------------------------------------------------
# These attributes are defined directly inside the class body.
# They belong to the class namespace and are shared across
# all objects created from this class.


class Tea:
    temperature = "hot"
    strength = "Strong"


# ---------------------------------------------------------
# Step 2: Creating an Object and Accessing a Class Attribute
# ---------------------------------------------------------
# The object `cutting` is created but has no attributes of its own yet.
#
# When `cutting.temperature` is accessed, Python first checks
# the object's own namespace — nothing is found there.
# Python then falls back to the class namespace and finds
# `temperature = "hot"` defined there.

cutting = Tea()

print(cutting.temperature)  # hot — read from class namespace


# ---------------------------------------------------------
# Step 3: Shadowing the Class Attribute
# ---------------------------------------------------------
# Assigning a new value to `cutting.temperature` does NOT
# modify the class attribute.
#
# Instead, Python creates a brand new entry called `temperature`
# inside the object's own namespace with the value "Mild".
#
# From this point:
#   • cutting.temperature → reads "Mild" from object namespace
#   • Tea.temperature     → still reads "hot" from class namespace
#
# The class attribute is hidden (shadowed), not overwritten.
#
# A completely new attribute `cup` is also added directly to
# the object — this exists only in the object's namespace.

cutting.temperature = "Mild"
cutting.cup = "small"

print(f"After changing value: {cutting.temperature}")            # Mild
print(f"Direct look into the class for temperature value: {Tea.temperature}")  # hot


# ---------------------------------------------------------
# Step 4: Deleting the Shadowed Attribute — Fallback Behavior
# ---------------------------------------------------------
# `del cutting.temperature` removes only the object's own copy.
# The class attribute `Tea.temperature` is completely unaffected.
#
# After deletion, Python follows the lookup order again:
#   1. Object namespace → `temperature` not found (just deleted)
#   2. Class namespace  → `temperature = "hot"` found here
#
# So Python falls back and returns the class attribute value.

del cutting.temperature

print(cutting.temperature)  # Falls back to Tea.temperature → hot


# ---------------------------------------------------------
# Step 5: Behavior When No Fallback Exists
# ---------------------------------------------------------
# The `cup` attribute was added only to the object.
# It was never defined in the Tea class.

print(f"Cup size is: {cutting.cup}")  # small — found in object namespace

# Deleting the object-only attribute
del cutting.cup

# Now accessing `cutting.cup` will raise an AttributeError.
#
# Python searches:
#   1. Object namespace → `cup` not found (just deleted)
#   2. Class namespace  → `cup` not found (never defined here)
#
# No fallback exists, so Python raises:
# AttributeError: 'Tea' object has no attribute 'cup'

# Uncommenting the line below will produce the error described above:
# print(cutting.cup)