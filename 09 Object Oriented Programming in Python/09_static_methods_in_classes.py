"""
File: 09_static_methods_in_classes.py
Chapter: 09 — Object Oriented Programming in Python
Topic: Static Methods - Utility Functions Inside Classes

Problem Statement
-----------------
Sometimes a class needs functions that perform utility tasks related to the
class concept but don't need access to any instance data (self) or class
data (cls). For example, a TeaUtils class might need to clean and parse
ingredient lists. These functions work perfectly fine without creating an
object first.

Regular methods require an instance (object) to be called. Static methods
can be called directly on the class itself. They behave just like regular
functions but are grouped inside the class for organization and namespace
management.

This file demonstrates:
1. What static methods are and when to use them.
2. The @staticmethod decorator syntax.
3. How to call static methods through the class (preferred) vs through instances.
4. Real-world use case: data cleaning and parsing utilities.

Key Concepts
------------
Static Method
    A method that belongs to a class but doesn't receive any automatic
    first parameter (neither self nor cls). It behaves exactly like a
    regular function but lives inside the class's namespace.

    Use static methods when the function logic relates to the class concept
    but doesn't need to access or modify instance or class state.

@staticmethod Decorator
    The syntax that tells Python this method should not receive self or cls.
    Without this decorator, Python would pass the instance as first argument.

Instance Method vs Static Method
    Instance method: def method(self): → needs object, receives self
    Static method: @staticmethod def method(): → needs no object, receives nothing
    Class method: @classmethod def method(cls): → receives class, not instance
"""


# ---------------------------------------------------------
# Step 1: Defining a Class with a Static Method
# ---------------------------------------------------------
# The @staticmethod decorator tells Python this method does NOT need
# access to self (instance) or cls (class). It's just a utility function
# organized inside the class.

class TeaUtils:
    """
    Utility class for tea-related string and data processing.
    
    All methods in this class are static because they perform generic
    transformations that don't require any stored state.
    """
    
    @staticmethod
    def clean_ingredients(text):
        """
        Parse a comma-separated ingredient string into a clean list.
        
        Converts a raw ingredient string like "water , milk, ginger" into
        a list of cleaned items with spaces removed from both ends.
        
        Parameters
        ----------
        text : str
            Raw ingredient string with commas and possible extra spaces.
        
        Returns
        -------
        list
            List of cleaned ingredient strings with no leading/trailing spaces.
        
        Example
        -------
        >>> TeaUtils.clean_ingredients("  water  , milk,  ginger  ")
        ['water', 'milk', 'ginger']
        """
        # Split by comma, then strip whitespace from each resulting item
        # List comprehension: [item.strip() for item in text.split(",")]
        #   • text.split(",") breaks string at each comma
        #   • .strip() removes spaces from start and end of each item
        return [item.strip() for item in text.split(",")]


# ---------------------------------------------------------
# Step 2: Raw Data to Process
# ---------------------------------------------------------
# This string contains extra spaces around items that need cleaning.
# A real application might read this from a file, database, or user input.

raw_ingredients = "   water   , milk,    ginger,    honey   "


# ---------------------------------------------------------
# Step 3: Two Ways to Call a Static Method
# ---------------------------------------------------------
# Way 1: Through an instance (object) — works but unnecessary
# ---------------------------------------------------------
# Creating an object just to call a static method is wasteful.
# You don't need an object because the method doesn't use self.

utils_object = TeaUtils()
result_from_object = utils_object.clean_ingredients(raw_ingredients)
print("Called through object:")
print(result_from_object)


# ---------------------------------------------------------
# Way 2: Through the class directly (PREFERRED)
# ---------------------------------------------------------
# This is cleaner, more efficient, and clearly communicates that this
# method doesn't need instance data. No object creation required.

result_from_class = TeaUtils.clean_ingredients(raw_ingredients)
print("\nCalled through class:")
print(result_from_class)


# ---------------------------------------------------------
# Step 4: Understanding the Output Format
# ---------------------------------------------------------
# The function returns a list of cleaned strings. Notice:
#   • 'water' has no spaces before or after
#   • 'milk' is clean
#   • 'ginger' has no spaces
#   • 'honey' has no trailing spaces

print("\nIndividual items after cleaning:")
for item in result_from_class:
    print(f"  • '{item}'")


# ---------------------------------------------------------
# Important Notes About Static Methods
# ---------------------------------------------------------
# 1. No self parameter: Static methods cannot access or modify instance
#    attributes because they don't receive self.
#
# 2. No cls parameter: Static methods cannot access or modify class
#    attributes either. For that, use @classmethod.
#
# 3. Organization benefit: Even though static methods work like regular
#    functions, grouping them inside a class shows they are related to
#    that concept (e.g., all tea utilities live in TeaUtils).
#
# 4. Calling convention: Always prefer ClassName.method() over creating
#    an instance. The instance works but is misleading and inefficient.
#
# 5. Common use cases:
#    • Data validation (check if input matches expected format)
#    • Data transformation (convert between units, parse strings)
#    • Factory methods (when combined with @classmethod)
#    • Mathematical utilities related to the class concept
#
# 6. When NOT to use static methods:
#    • If you need to access instance attributes → use instance method
#    • If you need to access class attributes → use class method
#    • If the function has no logical connection to the class → make it a regular function