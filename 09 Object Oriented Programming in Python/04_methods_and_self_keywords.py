"""
File: 04_methods_and_self_keyword.py
Chapter: 09 — Object Oriented Programming in Python
Topic: Instance Methods and the Role of 'self'

Problem Statement
-----------------
In Object Oriented Programming, a class not only holds data through
attributes but also defines behaviors through methods. A method is
simply a function defined inside a class that operates on the object
it belongs to.

However, for a method to know which object it is operating on, Python
requires a special first parameter called `self`. Understanding how
`self` works — and what happens when a method is called through an
object versus directly through the class — is fundamental to working
with OOP in Python.

This file demonstrates:
1. How to define an instance method inside a class.
2. What `self` is and why it is required as the first parameter.
3. How Python automatically passes the object as `self` during a method call.
4. How to call a method using the class name by passing the object explicitly.
5. How object-specific attribute changes affect method output.

Key Concepts
------------
Instance Method
    A function defined inside a class that operates on a specific object.
    It always takes `self` as its first parameter, which refers to the
    object calling the method.

self
    A reference to the current object (instance) that is calling the method.
    Through `self`, the method can access and modify the object's own
    attributes and call other methods on the same object.
    The name `self` is a convention — Python does not enforce this name,
    but using anything else is strongly discouraged.

Bound Method Call
    Calling a method through an object: `object.method()`
    Python automatically passes the object as the first argument (`self`).

Unbound Method Call
    Calling a method through the class name: `ClassName.method(object)`
    Python does NOT pass the object automatically — it must be passed
    explicitly as the first argument.
"""

# ---------------------------------------------------------
# Step 1: Defining a Class with an Instance Method
# ---------------------------------------------------------
# `size` is a class attribute — it belongs to the class
# and is shared across all instances by default.
#
# `describe` is an instance method — it is a function defined
# inside the class that operates on a specific object.
#
# `self` must always be the first parameter of an instance method.
# When the method is called on an object, Python automatically
# passes that object as the value of `self`.
#
# Inside the method, `self.size` accesses the `size` attribute
# of whichever object is calling the method.


class Teacup:
    size = 150  # ml — class attribute shared by all Teacup instances

    def describe(self):
        """
        Returns a description of the teacup using its size attribute.

        `self.size` first checks the object's own namespace.
        If not found there, it falls back to the class namespace.

        Returns
        -------
        str
            A formatted string describing the teacup's size.
        """
        return f"A {self.size} ml chai cup"


# ---------------------------------------------------------
# Step 2: Calling a Method Using an Object (Bound Method Call)
# ---------------------------------------------------------
# When a method is called on an object using dot notation,
# Python automatically passes the object as the first argument.
#
# So `cup.describe()` is internally equivalent to:
#   Teacup.describe(cup)
#
# Python binds the object `cup` to the `self` parameter
# without requiring us to pass it manually.

cup = Teacup()

print(cup.describe())


# ---------------------------------------------------------
# Step 3: Calling a Method Using the Class (Unbound Method Call)
# ---------------------------------------------------------
# When a method is called using the class name instead of
# an object, Python does NOT automatically pass any object.
#
# Calling `Teacup.describe()` without an argument would raise:
# TypeError: describe() missing 1 required positional argument: 'self'
#
# The correct approach is to pass the object explicitly
# as the first argument so that `self` receives it.

print(Teacup.describe(cup))  # Explicitly passing `cup` as `self`


# ---------------------------------------------------------
# Step 4: Object-Specific Attribute Change Affecting Method Output
# ---------------------------------------------------------
# Creating a second object from the same class.
# By default, it inherits the class attribute `size = 150`.
#
# Assigning `cupTwo.size = 100` creates a new attribute in
# the object's own namespace (attribute shadowing).
#
# Now when `describe()` is called with `cupTwo` as `self`,
# `self.size` finds `100` in the object namespace first —
# so the method output reflects the object-specific value.

cupTwo = Teacup()
cupTwo.size = 100  # Shadows the class attribute for this object only

print(Teacup.describe(cupTwo))  # Uses cupTwo.size = 100, not Tea.size = 150