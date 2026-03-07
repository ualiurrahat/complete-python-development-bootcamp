# ============================================================
# File: 06_variable_scope_and_name_resolution.py
# Chapter: 04 - Functions
# Topic: Variable Scope and Name Resolution in Python
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# In Python, variables are not accessible everywhere in
# a program. Their accessibility depends on where they
# are defined. This concept is known as **variable scope**.
#
# Python resolves variable names using the **LEGB rule**:
#
# L → Local Scope
# E → Enclosing Scope
# G → Global Scope
# B → Built-in Scope
#
# This file demonstrates how Python searches for variables
# across these scopes when executing functions.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Local Scope
# ------------------------------------------------------------
# A variable defined inside a function belongs to the
# **local scope** of that function. It cannot be accessed
# outside the function.

def serve_chai():
    chai_type = "Masala"   # Local variable
    print(f"Inside function Chai type: {chai_type}")


# Global variable with the same name
chai_type = "Lemon"

serve_chai()

# This refers to the global variable, not the local one
print(f"Outside function Chai type: {chai_type}")


# ------------------------------------------------------------
# Step 2: Enclosing Scope (Nested Functions)
# ------------------------------------------------------------
# When functions are nested, the inner function can access
# variables from the outer function. This is called the
# **enclosing scope**.

def chai_counter():
    chai_order = "Lemon"   # Enclosing scope variable

    def print_order():
        chai_order = "Ginger"  # Local to inner function
        print("Inner function Chai order:", chai_order)

    print_order()

    # This still refers to the enclosing variable
    print("Outer function Chai order:", chai_order)


# ------------------------------------------------------------
# Step 3: Global Scope
# ------------------------------------------------------------
# Variables defined outside functions belong to the
# **global scope** and can be accessed anywhere unless
# shadowed by a local variable.

chai_order = "Tulsi"   # Global variable

chai_counter()

print("Global Chai order:", chai_order)


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# Python resolves variable names using the **LEGB rule**:
#
# Local:
#   Variables defined inside the current function.
#
# Enclosing:
#   Variables from outer functions when functions
#   are nested.
#
# Global:
#   Variables defined at the top level of the script.
#
# Built-in:
#   Predefined names provided by Python itself
#   (for example: print(), len(), type()).
#
# Python searches these scopes in order:
# Local → Enclosing → Global → Built-in.
#
# Understanding scope is essential for writing
# predictable and bug-free programs, especially when
# working with nested functions and large codebases.
# ------------------------------------------------------------