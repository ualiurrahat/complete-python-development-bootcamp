"""
File: 05_constructor_and_init_method.py
Chapter: 09 — Object Oriented Programming in Python
Topic: Constructor and the __init__ Method

Problem Statement
-----------------
In Object Oriented Programming, when an object is created from a class,
it often needs to be set up with some initial data right away. For example,
a tea order should know its type and size the moment it is created.

This initial setup process is handled by a special function called a
constructor. In most programming languages like C++ and Java, the
constructor has the same name as the class and has no return type.

Python works differently. Instead of naming the constructor after the
class, Python uses a special built-in method called `__init__` as its
constructor. This method is automatically called by Python every time
a new object is created from the class.

This file demonstrates:
1. What a constructor is and why it is needed.
2. How Python's `__init__` method works as a constructor.
3. How `__init__` differs from constructors in other languages.
4. How instance attributes are created and assigned inside `__init__`.
5. How multiple objects can hold different data independently.

Key Concepts
------------
Constructor
    A special method that is automatically called when a new object is
    created from a class. Its purpose is to initialize the object with
    data so it is ready to use immediately after creation.

__init__ Method
    Python's constructor. The double underscores on both sides indicate
    that this is a special built-in method recognized by Python itself.
    These are called "dunder" (double underscore) methods or magic methods.
    Unlike other languages, the constructor is not named after the class —
    Python always uses `__init__` for this purpose.

Instance Attribute
    A variable that is assigned to a specific object inside `__init__`
    using `self.attributeName = value`. Unlike class attributes, instance
    attributes are unique to each object and are created fresh every time
    a new object is instantiated.

Dunder / Magic Method
    Methods with double underscores on both sides (e.g., `__init__`,
    `__str__`). Python calls these automatically in specific situations.
    They are not meant to be called manually in most cases.

type_ (Trailing Underscore Convention)
    When a desired parameter name conflicts with a Python built-in keyword
    or built-in function (like `type`), a trailing underscore is added
    by convention to avoid the conflict: `type_` instead of `type`.
"""

# ---------------------------------------------------------
# Step 1: Defining a Class with a Constructor
# ---------------------------------------------------------
# The `__init__` method is defined like any other method inside
# a class, but Python calls it automatically the moment a new
# object is created.
#
# Parameters after `self` are the values the caller must pass
# when creating the object.
#
# Comparison with other languages:
#   C++  → MyClass() { ... }       (same name as class, no return type)
#   Java → MyClass() { ... }       (same name as class, no return type)
#   Python → def __init__(self):   (always named __init__, no return type)
#
# In Python, `__init__` must never use a `return` statement with a value.
# It always implicitly returns None.


class TeaOrder:

    def __init__(self, type_, size):
        """
        Constructor that initializes a TeaOrder object with its type and size.

        This method is called automatically by Python when a new TeaOrder
        object is created. It sets up the instance attributes for that object.

        Parameters
        ----------
        type_ : str
            The variety of tea (e.g., "Black", "Ginger").
            Named `type_` with a trailing underscore to avoid conflict
            with Python's built-in `type` function.

        size : int
            The size of the tea order in millilitres (e.g., 150, 250).
        """

        # -------------------------------------------------
        # Step 2: Creating Instance Attributes
        # -------------------------------------------------
        # `self.type` and `self.size` are instance attributes.
        #
        # They are created fresh for every new object and stored
        # in that object's own namespace.
        #
        # The right-hand side (type_, size) are the values passed
        # in by the caller. The left-hand side (self.type, self.size)
        # are the attribute names stored on the object.
        #
        # Each object gets its own independent copy of these attributes.

        self.type = type_
        self.size = size

    def summary(self):
        """
        Returns a human-readable summary of the tea order.

        Returns
        -------
        str
            A formatted string describing the order's size and type.
        """
        return f"{self.size} ml of {self.type} tea"


# ---------------------------------------------------------
# Step 3: Creating Objects Using the Constructor
# ---------------------------------------------------------
# When `TeaOrder("Black", 150)` is called:
#   1. Python creates a new empty object
#   2. Python automatically calls `__init__(self, "Black", 150)`
#   3. `self.type` is set to "Black" and `self.size` is set to 150
#   4. The fully initialized object is returned and stored in `order`

order = TeaOrder("Black", 150)
print(order.summary())


# ---------------------------------------------------------
# Step 4: Creating a Second Independent Object
# ---------------------------------------------------------
# Each object created from TeaOrder gets its own separate
# instance attributes. Changing one object's data never
# affects another object's data.
#
# `order_two` has its own `type` and `size` completely
# independent from `order`.

order_two = TeaOrder("Ginger", 250)
print(order_two.summary())