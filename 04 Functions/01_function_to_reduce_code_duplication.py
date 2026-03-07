# ============================================================
# File: 01_function_to_reduce_code_duplication.py
# Chapter: 04 - Functions
# Topic: Using Functions to Reduce Code Duplication
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# You are managing a busy tea stall.
# Many customers place orders, and for each order you need to
# print the customer's name along with the chai type they ordered.
#
# If we wrote separate print statements for every order,
# the code would quickly become repetitive.
#
# To avoid repeating the same logic, we create a function
# that handles printing the order information.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Define the Function
# ------------------------------------------------------------
# def → keyword used to define a function
#
# print_order → name of the function
#
# (name, chai_type) → parameters
# These parameters allow the function to accept different
# values each time it is called.

def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai!")


# ------------------------------------------------------------
# Step 2: Call the Function Multiple Times
# ------------------------------------------------------------
# Each time the function is called, we pass different values
# for the parameters.

print_order("Rahat", "milked")
print_order("Shahnur", "garlic")
print_order("Nabila", "green")


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - The function 'print_order' contains reusable logic.
# - Instead of writing multiple print statements manually,
#   we call the function with different arguments.
#
# Parameters:
# name → customer name
# chai_type → type of chai ordered
#
# This approach keeps code cleaner, shorter, and easier
# to maintain.
# ------------------------------------------------------------