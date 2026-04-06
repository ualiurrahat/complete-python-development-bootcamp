"""
File: 01_intro_to_classes.py
Chapter: 09 — Object Oriented Programming in Python
Topic: Basic Class Creation and Object Instantiation

Problem Statement
-----------------
In Python, everything is an object. Object Oriented Programming (OOP)
is a programming paradigm that organizes code around objects rather than
functions and logic alone.

To create objects, we first need a blueprint — and that blueprint is
called a class. A class defines the structure and behavior that every
object created from it will have.

This file demonstrates:
1. What a class is and how to define one in Python.
2. How to create objects (instances) from a class.
3. What the `pass` keyword does inside an empty class.
4. How Python's built-in `type()` function works with classes and objects.
5. The difference between the type of a class and the type of an instance.

Key Concepts
------------
Class
    A blueprint or template for creating objects. It defines a new
    user-defined data type with its own structure and behavior.

Object (Instance)
    A specific realization of a class. Each object is created from
    a class and has its own independent identity in memory.

Instantiation
    The process of creating an object from a class by calling the
    class like a function: `objectName = ClassName()`.

pass
    A keyword used as a placeholder when a code block is syntactically
    required but no code needs to be written yet.

type()
    A built-in function that returns the type of the object passed to it.
    Classes themselves are objects of type `type` in Python.
"""

# ---------------------------------------------------------
# Step 1: Defining Classes
# ---------------------------------------------------------
# A class is defined using the `class` keyword followed by
# the class name and a colon.
#
# In Python, classes themselves are objects — specifically,
# they are instances of a built-in metaclass called `type`.
#
# The `pass` keyword is used here because the class body
# is syntactically required, but we have no attributes or
# methods to define yet.


class Chai:
    # `pass` acts as a placeholder — it does nothing,
    # but prevents Python from raising an IndentationError
    # due to an empty class body.
    pass


class ChaiTime:
    # Another empty class defined to compare types later
    pass


# ---------------------------------------------------------
# Step 2: Creating an Object (Instance)
# ---------------------------------------------------------
# An object is created by calling the class like a function.
# This process is called instantiation.
#
# Syntax:
#   objectName = ClassName()
#
# Python internally calls a special method called `__init__`
# during this step (even if we have not defined one ourselves).
# When no `__init__` is defined, Python uses a default empty one.

gingerTea = Chai()


# ---------------------------------------------------------
# Step 3: Understanding type() with Classes and Objects
# ---------------------------------------------------------
# `type()` is a built-in function that returns the type of
# whatever is passed to it.
#
# There is an important distinction between:
#   • Passing the class name itself  → returns 'type'
#   • Passing an instance (object)   → returns the class it belongs to
#
# This is because in Python, classes are themselves objects,
# and every class is an instance of the built-in metaclass `type`.

# Passing the class name itself:
# Python reports that Chai's type is 'type' — the metaclass
print(type(Chai))       # <class 'type'>

# Passing the instance:
# Python reports that gingerTea belongs to the Chai class
print(type(gingerTea))  # <class '__main__.Chai'>

# ---------------------------------------------------------
# Step 4: Comparing Types Using the `is` Operator
# ---------------------------------------------------------
# The `is` operator checks whether two objects are exactly
# the same object in memory — not just equal in value.
#
# Here, we use it to verify which class an object belongs to.

# Checking if gingerTea's type is exactly Chai — should be True
print(type(gingerTea) is Chai)      # True

# Checking if gingerTea's type is ChaiTime — should be False
# because gingerTea was created from Chai, not ChaiTime
print(type(gingerTea) is ChaiTime)  # False