"""
File: 07_accessing_base_class_methods.py
Chapter: 09 — Object Oriented Programming in Python
Topic: Three Ways to Access Base Class Methods

Problem Statement
-----------------
When a child class inherits from a parent class, it often needs to call
the parent's methods. The most common scenario is the child's __init__
method needing to run the parent's __init__ to set up inherited attributes.
Python provides three approaches to do this, ranging from worst to best.

This file demonstrates:
1. Code duplication (worst practice - do NOT use)
2. Explicit parent class call (acceptable but inflexible)
3. super() function (best practice - recommended)

Key Concepts
------------
super()
    A built-in function that returns a temporary object of the parent class.
    It automatically handles method resolution order (MRO) and works with
    multiple inheritance. This is the Pythonic way to call parent methods.

Explicit Parent Call
    Calling the parent class method directly: Parent.method(self, args).
    Works but breaks easily with multiple inheritance or class name changes.

Code Duplication
    Copying parent class code into child class. Creates maintenance problems
    and defeats the purpose of inheritance. Never use this approach.
"""


class Tea:
    """Parent class representing basic tea."""
    
    def __init__(self, type_, strength):
        """
        Initialize a tea with type and strength.
        
        Parameters
        ----------
        type_ : str
            Variety of tea (e.g., "Ginger", "Black")
        strength : int
            Tea strength on scale 1-10
        """
        self.type = type_
        self.strength = strength


# ---------------------------------------------------------
# Way 1: Code Duplication (WRONG - Do Not Use)
# ---------------------------------------------------------
# This approach manually repeats all parent class initialization code.
# Problems:
#   • Violates DRY (Don't Repeat Yourself) principle
#   • If Tea.__init__ changes, GingerTea becomes outdated
#   • Defeats the purpose of inheritance

class GingerTeaWrong(Tea):
    def __init__(self, type_, strength, spice_level):
        # WRONG: Duplicating parent class code
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level


# ---------------------------------------------------------
# Way 2: Explicit Parent Class Call
# ---------------------------------------------------------
# Call the parent class __init__ directly using ClassName.__init__(self, ...)
# 
# Advantages:
#   • No code duplication
#   • Clear which parent class is being called
#
# Disadvantages:
#   • Must explicitly pass `self`
#   • Breaks with multiple inheritance (skips other parents)
#   • If parent class name changes, must update all child classes

class GingerTeaExplicit(Tea):
    def __init__(self, type_, strength, spice_level):
        # Explicit call to Tea's __init__ method
        Tea.__init__(self, type_, strength)
        self.spice_level = spice_level


# ---------------------------------------------------------
# Way 3: super() Function (BEST PRACTICE)
# ---------------------------------------------------------
# super() returns a proxy object that delegates method calls to the parent
# class. Python automatically handles which parent class to call.
#
# Advantages:
#   • No need to pass `self` explicitly
#   • Works correctly with multiple inheritance
#   • Parent class can be renamed without breaking child classes
#   • This is the Pythonic way

class GingerTea(Tea):
    def __init__(self, type_, strength, spice_level):
        # super() automatically finds and calls the parent class __init__
        super().__init__(type_, strength)
        self.spice_level = spice_level


# ---------------------------------------------------------
# Demonstration
# ---------------------------------------------------------
ginger = GingerTea("Ginger", 7, "High")
print(f"Tea type: {ginger.type}")
print(f"Strength: {ginger.strength}")
print(f"Spice level: {ginger.spice_level}")


# ---------------------------------------------------------
# Important Notes
# ---------------------------------------------------------
# 1. Always use super() to call parent class methods. It's the Python standard.
# 2. super() works in any method, not just __init__.
# 3. In single inheritance, super() is simpler than explicit calls.
# 4. Never duplicate parent class code - it defeats inheritance's purpose.
# 5. super() requires no arguments in modern Python (Python 3+).