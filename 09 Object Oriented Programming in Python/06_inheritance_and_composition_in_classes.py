"""
File: 06_inheritance_and_composition_in_classes.py
Chapter: 09 — Object Oriented Programming in Python
Topic: Inheritance and Composition

Problem Statement
-----------------
When building object-oriented systems, classes need to relate to each other.
Two fundamental ways exist: inheritance (is-a relationship) and composition
(has-a relationship). Inheritance means a child class extends a parent class.
Composition means a class holds a reference to another class.

This file demonstrates:
1. Inheritance syntax and method inheritance from parent to child.
2. Composition by storing a class reference as an attribute.
3. The difference between storing a class (no parentheses) vs creating an object (with parentheses).
4. How composition allows swapping behavior by overriding class attributes.

Key Concepts
------------
Inheritance
    A child class automatically gains all methods and attributes from its
    parent class. Defined as `class Child(Parent):`.

Composition
    A class stores a reference to another class as an attribute. This creates
    a "has-a" relationship instead of an "is-a" relationship.

Class Attribute
    An attribute belongs to the class itself, not to instances. Can be
    overridden in subclasses.

type_ (Trailing Underscore)
    Parameter name with trailing underscore avoids conflict with Python's
    built-in `type` function.
"""


class BaseTea:
    """Parent class for all tea types."""
    
    def __init__(self, type_):
        self.type = type_
    
    def prepare(self):
        print(f"Preparing {self.type} tea....")


class MasalaTea(BaseTea):
    """Child class inheriting from BaseTea."""
    
    def add_spices(self):
        print(f"Adding cardamom, ginger, cloves")


# ---------------------------------------------------------
# Step 1: Composition - Storing a Class Reference
# ---------------------------------------------------------
# TeaShop HAS a reference to a tea class. Note: no parentheses after BaseTea.
# This stores the CLASS itself, not an object.
#
# With parentheses: obj = BaseTea("Regular")  # Creates an object
# Without parentheses: cls = BaseTea          # Stores the class

class TeaShop:
    tea_cls = BaseTea  # Class attribute storing a reference to BaseTea
    
    def __init__(self):
        # Create an object by adding parentheses to the stored class reference
        self.tea = self.tea_cls("Regular")
    
    def serve(self):
        print(f"Serving {self.tea.type} tea in the shop")
        self.tea.prepare()


# ---------------------------------------------------------
# Step 2: Overriding the Composed Class in a Child
# ---------------------------------------------------------
# FancyTeaShop inherits from TeaShop but replaces tea_cls with MasalaTea.
# When __init__ runs, it creates self.tea = MasalaTea("Regular").

class FancyTeaShop(TeaShop):
    tea_cls = MasalaTea  # Override the parent's class attribute


# ---------------------------------------------------------
# Step 3: Demonstration
# ---------------------------------------------------------
shop = TeaShop()          # Uses BaseTea internally
fancy = FancyTeaShop()    # Uses MasalaTea internally

shop.serve()              # Output: Serving Regular tea... Preparing Regular tea....
fancy.serve()             # Output: Serving Regular tea... Preparing Regular tea....

# Access child-specific method (only works because fancy.tea is MasalaTea object)
fancy.tea.add_spices()    # Output: Adding cardamom, ginger, cloves


# ---------------------------------------------------------
# Important Notes
# ---------------------------------------------------------
# 1. Without parentheses = storing the class. With parentheses = creating an object.
# 2. Composition (has-a) is often more flexible than inheritance (is-a).
# 3. Class attributes can be overridden in subclasses to swap behavior.