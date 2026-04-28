"""
File: 11_property_decorator_getters_setters.py
Chapter: 09 — Object Oriented Programming in Python
Topic: Property Decorator - Getters and Setters

Problem Statement
-----------------
Directly exposing instance attributes (self.age) is simple but dangerous.
Nothing prevents invalid values from being assigned. Traditional solution
in other languages (Java/C++) is to write getter and setter methods:
get_age() and set_age().

Python offers a more elegant solution: the @property decorator. It allows
you to define methods that act like attributes. Users can read and write
.property syntax, but behind the scenes, your validation logic runs.

This file demonstrates:
1. Encapsulation: hiding internal _age attribute from direct access.
2. @property getter: controls reading with computed or validated returns.
3. @age.setter: controls writing with validation logic.
4. How property methods are called like attributes (no parentheses).

Key Concepts
------------
Property Decorator (@property)
    Converts a method into a read-only attribute. When user accesses
    object.age, this method runs and returns the value.

Setter Decorator (@attribute_name.setter)
    Converts a method into a writeable attribute. When user assigns
    object.age = value, this method runs with the new value.

Name Mangling Convention (_age)
    Underscore prefix indicates "protected" attribute — meant for internal
    use. Users should access through the property, not directly.
"""


class TeaLeaf:
    """
    Represents a tea leaf with aging properties.
    
    The _age attribute is protected (internal). Users interact with the
    age property, which applies validation and business logic.
    """
    
    def __init__(self, age):
        """
        Initialize a tea leaf with given age.
        
        Parameters
        ----------
        age : int
            Age of tea leaf in years (1-5 range expected)
        """
        # Directly use the setter logic by assigning to property
        # This reuses validation logic from @age.setter
        self.age = age
    
    @property
    def age(self):
        """
        Getter: Returns tea leaf age plus 2 years of processing.
        
        This demonstrates that properties can transform data when reading.
        The stored _age is 2, but reported age is 4.
        
        Returns
        -------
        int
            Processed age (internal _age + 2)
        """
        # Business rule: add 2 years of processing time to actual age
        return self._age + 2
    
    @age.setter
    def age(self, age):
        """
        Setter: Validates age before storing internally.
        
        Parameters
        ----------
        age : int
            Age in years to set
        
        Raises
        ------
        ValueError
            If age is not between 1 and 5 (inclusive)
        """
        # Validation logic: only accept ages 1 through 5
        if 1 <= age <= 5:
            # Store the raw age internally (prefixed with underscore)
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")


# ---------------------------------------------------------
# Demonstration: Property in Action
# ---------------------------------------------------------

# Create a tea leaf with age 2
leaf = TeaLeaf(2)
print(leaf.age)  # Output: 4 (2 internal + 2 processing)

# Try to set invalid age (6)
# This will raise ValueError with the custom message
try:
    leaf.age = 6
    print(leaf.age)  # This line won't execute due to exception
except ValueError as e:
    print(f"Error: {e}")

# Valid age update (works correctly)
leaf.age = 3
print(leaf.age)  # Output: 5 (3 internal + 2 processing)


# ---------------------------------------------------------
# Important Notes
# ---------------------------------------------------------
# 1. Properties look like attributes but behave like methods.
# 2. No parentheses needed: obj.age (not obj.age()).
# 3. Underscore prefix (_age) convention means "protected - don't touch".
# 4. Properties allow validation, logging, computed values, or deprecation.
# 5. Without @age.setter, the property is read-only.
# 6. Property names and internal storage names should be different (age vs _age).
# 7. Advantages over traditional getter/setter methods:
#    • Cleaner syntax (obj.age vs obj.get_age())
#    • Backward compatible (attribute can become property without breaking code)
#    • Encapsulation without verbosity