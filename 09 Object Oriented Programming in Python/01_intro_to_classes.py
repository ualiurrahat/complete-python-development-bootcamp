"""
File: 01_intro_to_classes.py
Chapter: Object Oriented Programming In Python
Topic: Basic Class Creation and Object Instantiation
Problem Statement:
Understand the basic syntax of creating classes in Python and learn how
objects (instances) are created from those classes. Also observe how
Python treats classes and objects using the built-in type() function.
"""

# ---------------------- Step 1: Defining Classes ----------------------
# A class is a blueprint for creating objects.
# It defines a new user-defined data type.

class Chai:
    # 'pass' is used when a block is syntactically required
    # but no code needs to be written yet.
    pass


class ChaiTime:
    # Another empty class to compare types later
    pass


# ---------------------- Step 2: Creating an Object (Instance) ----------------------
# An object is created by calling the class like a function.
# This process is called "instantiation".

gingerTea = Chai()


# ---------------------- Step 3: Understanding type() with Classes and Objects ----------------------
# type() returns the type of the object passed to it.

# When we pass the class name itself, Python says the type is 'type'
# because in Python, classes themselves are objects of type 'type'.
print(type(Chai))  # <class 'type'>

# When we pass the instance, Python says the type is the class it belongs to.
print(type(gingerTea))  # <class '__main__.Chai'>

# Checking if the object's type is exactly Chai
print(type(gingerTea) is Chai)  # True

# Checking if the object's type is ChaiTime
print(type(gingerTea) is ChaiTime)  # False