"""
File: 02_classes_and_object_namespace.py
Chapter: 09 — Object Oriented Programming in Python
Topic: Class Namespace vs Object Namespace

Problem Statement
-----------------
When working with classes and objects in Python, properties (variables)
can exist at two different levels: the class level and the object level.
These two levels are called namespaces.

Understanding the difference between these two namespaces is critical
because modifying a property on an object does not affect the class,
and properties added to one object do not appear on other objects or
on the class itself.

This file demonstrates:
1. What a class property is and how it is shared across all objects.
2. How to add a property to a class from outside the class definition.
3. How objects access class properties through inheritance of namespace.
4. What happens when a property is modified on an object.
5. How object-level properties are independent from class-level properties.
6. How to add a property that exists only on a specific object.

Key Concepts
------------
Class Namespace
    The space where all properties and methods defined inside a class
    are stored. These are shared and accessible by all objects created
    from that class.

Object Namespace
    The space where properties specific to a single object are stored.
    When a property is modified or added on an object, it lives here —
    completely independent from the class namespace.

Class Property
    A variable defined directly inside the class body (but outside any
    method). It belongs to the class and is shared across all instances.

Instance Property
    A variable that belongs to a specific object. It is created when
    a property is assigned directly on an object using dot notation.

Namespace Lookup Order
    When accessing a property on an object, Python first checks the
    object's own namespace. If not found there, it looks in the class
    namespace. This is why objects can access class properties without
    having their own copy.
"""

# ---------------------------------------------------------
# Step 1: Defining a Class with a Class Property
# ---------------------------------------------------------
# A class property is defined directly inside the class body,
# outside of any method.
#
# It belongs to the class itself — not to any specific object.
# All objects created from this class can access it because
# Python's namespace lookup checks the class when the object
# does not have its own copy of the property.


class Tea:
    origin = "China"  # Class property — shared by all instances of Tea


# Accessing the class property directly using the class name.
# No object needs to be created for this.
print(Tea.origin)


# ---------------------------------------------------------
# Step 2: Adding a Property to the Class Outside Its Definition
# ---------------------------------------------------------
# Python allows adding new properties to a class even after
# the class has already been defined.
#
# This is possible because classes in Python are mutable objects.
# The new property is added to the class namespace and becomes
# accessible to all existing and future objects of that class.

Tea.is_hot = True
print(Tea.is_hot)


# ---------------------------------------------------------
# Step 3: Creating an Object and Accessing Class Properties
# ---------------------------------------------------------
# When an object is created, it does not immediately get its
# own copy of class properties.
#
# Instead, Python looks up the class namespace when the object
# tries to access a property it does not own itself.
#
# This is why gingerTea can access `origin` and `is_hot`
# even though they were never assigned to gingerTea directly.

gingerTea = Tea()

print(f"Origin of Ginger Tea: {gingerTea.origin}")
print(f"Is Ginger Tea hot? {gingerTea.is_hot}")


# ---------------------------------------------------------
# Step 4: Modifying a Property on the Object (Object Namespace)
# ---------------------------------------------------------
# When we assign a new value to a property using the object,
# Python does NOT modify the class property.
#
# Instead, Python creates a new entry in the object's own
# namespace with the same property name and the new value.
#
# From this point forward:
#   • gingerTea.is_hot → reads from the object's own namespace
#   • Tea.is_hot       → still reads from the class namespace
#
# The two are now completely independent of each other.

gingerTea.is_hot = False

print(f"Class is_hot property value: {Tea.is_hot}")        # Still True
print(f"Ginger tea is_hot property value: {gingerTea.is_hot}")  # Now False


# ---------------------------------------------------------
# Step 5: Adding a New Property Only to the Object
# ---------------------------------------------------------
# A completely new property can be added directly to an object.
#
# This property lives exclusively in the object's namespace.
# It is NOT added to the Tea class and will NOT be accessible
# on any other object created from Tea.
#
# IMPORTANT:
#   gingerTea.flavor = "Mixed spice"
#   → exists only inside gingerTea
#
#   Tea.flavor         → would raise AttributeError
#   anotherTea.flavor  → would also raise AttributeError

gingerTea.flavor = "Mixed spice"
print(gingerTea.flavor)