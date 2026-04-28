"""
File: 10_class_methods_alternative_constructors.py
Chapter: 09 — Object Oriented Programming in Python
Topic: Class Methods as Alternative Constructors

Problem Statement
-----------------
A class typically has one constructor (__init__) that creates objects in a
specific way. But what if you need to create objects from different data
formats? For example, creating a TeaOrder from a dictionary, from a
hyphen-separated string, or from individual arguments.

Class methods provide a solution. They act as alternative constructors —
different ways to create the same object type from various data sources.

This file demonstrates:
1. Regular constructor (__init__) for standard object creation.
2. Class method as alternative constructor from dictionary.
3. Class method as alternative constructor from formatted string.
4. Static method for validation (reused across constructors).
5. How class methods receive the class (cls) and return cls(...).

Key Concepts
------------
Class Method
    A method bound to the class, not the instance. Receives cls as first
    parameter. Can create and return new objects of that class.

Alternative Constructor
    A class method that provides a different way to instantiate objects.
    Common naming convention: from_dict(), from_string(), from_csv(), etc.

cls Parameter
    The class itself (like self but for class-level). Used to create
    instances: cls(...) instead of ClassName(...).
"""


class TeaOrder:
    """Represents a tea order with type, sweetness level, and size."""
    
    def __init__(self, tea_type, sweetness, size):
        """
        Standard constructor for creating a tea order.
        
        Parameters
        ----------
        tea_type : str
            Type of tea (e.g., "masala", "ginger", "black")
        sweetness : str
            Sweetness level (e.g., "low", "medium", "high")
        size : str
            Cup size ("Small", "Medium", or "Large")
        """
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
    
    @classmethod
    def from_dict(cls, order_data):
        """
        Alternative constructor: creates TeaOrder from a dictionary.
        
        Parameters
        ----------
        order_data : dict
            Dictionary with keys "tea_type", "sweetness", "size"
        
        Returns
        -------
        TeaOrder
            New TeaOrder instance created from dictionary data.
        
        Example
        -------
        >>> data = {"tea_type": "masala", "sweetness": "medium", "size": "Large"}
        >>> order = TeaOrder.from_dict(data)
        """
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        """
        Alternative constructor: creates TeaOrder from hyphen-separated string.
        
        Parameters
        ----------
        order_string : str
            String formatted as "tea_type-sweetness-size"
        
        Returns
        -------
        TeaOrder
            New TeaOrder instance parsed from the string.
        
        Example
        -------
        >>> order = TeaOrder.from_string("Ginger-Low-Small")
        """
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)


class TeaUtils:
    """Utility class with validation helpers."""
    
    @staticmethod
    def is_valid_size(size):
        """
        Validate if a size string is among accepted values.
        
        Parameters
        ----------
        size : str
            Size to validate
        
        Returns
        -------
        bool
            True if size is "Small", "Medium", or "Large", False otherwise.
        """
        return size in ["Small", "Medium", "Large"]


# ---------------------------------------------------------
# Demonstration: Creating Objects Three Different Ways
# ---------------------------------------------------------

# Test the static validation method
print(TeaUtils.is_valid_size("Medium"))  # True

# Way 1: Create from dictionary using class method
order1 = TeaOrder.from_dict({
    "tea_type": "masala",
    "sweetness": "medium",
    "size": "Large"
})

# Way 2: Create from hyphenated string using class method
order2 = TeaOrder.from_string("Ginger-Low-Small")

# Way 3: Create using regular constructor with direct arguments
order3 = TeaOrder("Large", "Low", "Large")

# Display all three objects (__dict__ shows instance attributes)
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)


# ---------------------------------------------------------
# Important Notes
# ---------------------------------------------------------
# 1. Class methods receive cls, instance methods receive self.
# 2. Use cls(...) inside class methods, not the class name directly.
# 3. Alternative constructors make code more flexible and readable.
# 4. Common naming: from_json, from_csv, from_file, from_tuple.
# 5. Class methods can be inherited and overridden by child classes.
# 6. Use @classmethod decorator, not @staticmethod, when you need to create objects.