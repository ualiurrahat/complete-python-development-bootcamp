"""
File: 08_method_resolution_order_mro.py
Chapter: 09 — Object Oriented Programming in Python
Topic: Method Resolution Order (MRO)

Problem Statement
-----------------
When a class inherits from multiple parent classes (multiple inheritance),
and multiple parents define the same attribute or method, Python must
decide which parent's version to use. This decision follows a specific
order called the Method Resolution Order (MRO).

This file demonstrates:
1. How Python resolves attribute lookups in multiple inheritance.
2. The role of inheritance order in determining MRO.
3. How to view MRO using the __mro__ attribute.
4. Python's C3 linearization algorithm (what powers MRO).

Key Concepts
------------
Method Resolution Order (MRO)
    The sequence Python follows when searching for an attribute or method
    in an inheritance hierarchy. Python checks classes in MRO order and
    returns the first match found.

C3 Linearization
    The algorithm Python uses to compute MRO. It ensures:
    • Child classes come before parent classes
    • Parent classes maintain their relative order
    • No class appears twice in the MRO

__mro__
    A class attribute that returns a tuple showing the MRO. Useful for
    debugging multiple inheritance.
"""


class A:
    """Base class with generic tea label."""
    label = "A : Base class"


class B(A):
    """First child class - Masala tea blend."""
    label = "B : Masala blend"


class C(A):
    """Second child class - Herbal tea blend."""
    label = "C : Herbal blend"


# ---------------------------------------------------------
# Multiple Inheritance Example
# ---------------------------------------------------------
# class D(B, C) means: D inherits from B first, then C
# Python builds MRO: D → B → C → A
# When searching for `label`, Python checks:
#   1. Class D (not found)
#   2. Class B (found → returns "B : Masala blend")

class D(B, C):
    """Class inheriting from both B and C, with B first."""
    pass


# ---------------------------------------------------------
# Demonstration
# ---------------------------------------------------------
cup = D()
print(cup.label)  # Output: B : Masala blend

# View the complete MRO tuple
print(D.__mro__)
# Output: (__main__.D, __main__.B, __main__.C, __main__.A, object)

# ---------------------------------------------------------
# What If We Change the Inheritance Order?
# ---------------------------------------------------------
# If we defined: class D(C, B) instead
# MRO would be: D → C → B → A
# Then `cup.label` would print "C : Herbal blend"


# ---------------------------------------------------------
# Important Notes
# ---------------------------------------------------------
# 1. Python checks child classes before parent classes in MRO.
# 2. The order in parentheses determines parent priority.
# 3. MRO prevents duplicate searches - each class appears once.
# 4. Multiple inheritance is powerful but use it carefully.
# 5. The `super()` function follows MRO, not just the immediate parent.