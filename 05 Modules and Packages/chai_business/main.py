# ============================================================
# File: main.py
# Project: chai_business
# Topic: Python Imports and Modules
# ============================================================


# Problem Statement:
#
# In Python, large programs are divided into smaller
# reusable files called **modules**.
#
# Modules can be organized inside folders called
# **packages**.
#
# This file demonstrates several ways to import
# functions from another module.


# ============================================================
# METHOD 1: Import the Entire Module
# ============================================================

# This method imports the complete module.
# To access any function, we must use the module name.

# import recipes.flavors
#
# print(recipes.flavors.elaichi_chai())


# Explanation:
#
# Here we import the full module:
#
# recipes.flavors
#
# recipes -> folder (package)
# flavors -> module (Python file)
#
# To access the function we write:
#
# recipes.flavors.elaichi_chai()



# ============================================================
# METHOD 2: Import Specific Functions
# ============================================================

# Instead of importing the entire module, we can import
# only the functions we need.

# from recipes.flavors import elaichi_chai, ginger_chai
#
# print(ginger_chai())


# Explanation:
#
# This imports only the specified functions.
#
# Advantage:
# - Shorter code
# - No need to write module name every time
#
# Example usage:
#
# ginger_chai()



# ============================================================
# METHOD 3: Relative Import
# ============================================================

# Relative imports are used when working inside a package.

# from .recipes.flavors import elaichi_chai, ginger_chai
#
# print(elaichi_chai())


# Explanation:
#
# The dot (.) means:
#
# "start importing from the current package location".
#
# This style is commonly used when building
# large Python applications.



# ============================================================
# BAD PRACTICE: Using *
# ============================================================

# from recipes.flavors import *
#
# This imports EVERYTHING from the module.


# Why this is bad practice:
#
# 1. It pollutes the namespace
# 2. It becomes unclear where functions came from
# 3. It can cause name conflicts
#
# Therefore professional Python code avoids using * imports.
