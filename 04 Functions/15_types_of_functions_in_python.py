# ============================================================
# File: 15_types_of_functions_in_python.py
# Chapter: 04 - Functions
# Topic: Types of Functions in Python
# ============================================================


# Problem Statement:

# Python supports different styles of functions depending on
# how they behave and how they interact with data.
#
# In this file we demonstrate four important types of functions:
#
# 1. Pure Function
# 2. Impure Function
# 3. Recursive Function
# 4. Lambda (Anonymous) Function
#
# Each type is useful in different programming scenarios.



# ============================================================
# 1. PURE FUNCTION
# ============================================================

# A Pure Function:
# - Depends ONLY on its input parameters
# - Does NOT modify any external/global state
# - Always produces the same output for the same input
#
# Pure functions are predictable and easier to test.


def pure_chai(cups):
    return cups * 10


print("Pure function result:", pure_chai(5))


# Explanation:
#
# If we pass cups = 5:
#
# 5 * 10 = 50
#
# The function simply returns the result and does not
# modify anything outside the function.
#
# Therefore it is a PURE function.



# ============================================================
# 2. IMPURE FUNCTION
# ============================================================

# An Impure Function:
# - Depends on or modifies external variables
# - Changes the program state
# - Can produce different results even with the same inputs
#
# Impure functions are generally discouraged unless necessary.


total_chai = 0   # Global variable


def impure_chai(cups):
    global total_chai
    total_chai += cups


impure_chai(5)

print("Total chai after impure function:", total_chai)


# Explanation:
#
# This function modifies a GLOBAL variable.
#
# The keyword "global" tells Python that we want to use
# and modify the global variable instead of creating a
# new local variable.
#
# Because this function changes the external state of
# the program, it is considered an IMPURE function.



# ============================================================
# 3. RECURSIVE FUNCTION
# ============================================================

# A Recursive Function is a function that calls itself.
#
# Recursion is useful for solving problems that can be
# broken down into smaller versions of the same problem.
#
# Every recursive function must have:
#
# 1. Base Case      -> stops recursion
# 2. Recursive Case -> calls itself with smaller input


def pour_chai(n):

    # Base Case
    if n == 0:
        return "All cups poured"

    # Recursive Case
    else:
        print(f"Pouring cup number {n}")
        return pour_chai(n - 1)


print(pour_chai(3))


# Execution Flow for pour_chai(3):
#
# pour_chai(3)
# -> prints "Pouring cup number 3"
# -> calls pour_chai(2)
#
# pour_chai(2)
# -> prints "Pouring cup number 2"
# -> calls pour_chai(1)
#
# pour_chai(1)
# -> prints "Pouring cup number 1"
# -> calls pour_chai(0)
#
# pour_chai(0)
# -> returns "All cups poured"



# ============================================================
# 4. LAMBDA FUNCTION (ANONYMOUS FUNCTION)
# ============================================================

# A Lambda Function:
# - Is a small anonymous function
# - Does not have a name
# - Is usually written in one line
#
# Syntax:
#
# lambda parameters : expression
#
# Lambda functions are commonly used with functions like:
# map(), filter(), and sorted().


chai_types = ["light", "kadak", "ginger", "milked", "kadak", "special"]



# ------------------------------------------------------------
# Using filter() with a Lambda Function
# ------------------------------------------------------------

# filter(function, iterable)
#
# filter() applies a function to every element of an iterable
# and keeps only the elements where the function returns True.


strong_chai = list(
    filter(lambda chai: chai == "kadak", chai_types)
)

print("Strong Chai:", strong_chai)


# Explanation:
#
# The lambda function is:
#
# lambda chai : chai == "kadak"
#
# Here:
#
# "chai" is just a variable name representing each element
# in the chai_types list during iteration.
#
# The name could be anything:
# lambda tea : tea == "kadak"
# lambda item : item == "kadak"
#
# Python internally does something like this:
#
# chai = "light"   -> False
# chai = "kadak"   -> True
# chai = "ginger"  -> False
# chai = "milked"  -> False
# chai = "kadak"   -> True
# chai = "special" -> False
#
# Only the elements that return True are kept.
#
# Result:
# ['kadak', 'kadak']



# ------------------------------------------------------------
# Filtering Other Chai Types
# ------------------------------------------------------------

other_chai = list(
    filter(lambda tea: tea != "kadak", chai_types)
)

print("Other Chais:", other_chai)


# Explanation:
#
# lambda tea : tea != "kadak"
#
# This condition keeps every chai that is NOT "kadak".
#
# The variable name "tea" is simply a placeholder
# representing each element in the list during iteration.
#
# Result:
# ['light', 'ginger', 'milked', 'special']
