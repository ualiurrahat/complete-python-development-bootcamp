"""
File: 02_classes_and_object_namespace.py
Chapter: Object Oriented Programming In Python
Topic: Class Namespace vs Object Namespace
Problem Statement:
Understand how class properties and object properties live in different namespaces.
Learn how modifying a property on an object does not affect the class,
and how objects can have their own independent properties.
"""

# ---------------------- Step 1: Defining a Class with a Class Property ----------------------
# A class property (equivale to regular variable) belongs to the class itself.
# All objects created from this class can access this property.

class Tea:
    origin = "China"  # Class property


# Accessing class property directly using the class name
print(Tea.origin)


# ---------------------- Step 2: Adding a Property to Class Outside the Class ----------------------
# Python allows adding properties to a class even after it is defined.

Tea.is_hot = True
print(Tea.is_hot)


# ---------------------- Step 3: Creating an Object from the Class ----------------------
# Now creating an object (instance) from Tea class.

gingerTea = Tea()

print(f"Origin of Ginger Tea: {gingerTea.origin}")
print(f"Is Ginger Tea hot? {gingerTea.is_hot}")


# ---------------------- Step 4: Modifying Object Property (Object Namespace) ----------------------
# When we change a property using the object,
# Python creates/uses that property in the object's own namespace.

gingerTea.is_hot = False

# This change DOES NOT affect the class property.
# The class still holds the original value.

print(f"Class is_hot property value: {Tea.is_hot}")
print(f"Ginger tea is_hot property value: {gingerTea.is_hot}")


# ---------------------- Step 5: Adding a New Property Only to the Object ----------------------
# We can add completely new properties to an object.
# These properties exist ONLY inside that object.

gingerTea.flavor = "Mixed spice"
print(gingerTea.flavor)

# NOTE:
# 'flavor' is NOT added to the Tea class.
# It exists only inside the gingerTea object.