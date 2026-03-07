# ============================================================
# File: 04_improving_readability_using_functions.py
# Chapter: 04 - Functions
# Topic: Improving Readability Using Functions with Return Values
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# You run a chai shop that sells different sizes of tea.
#
# Customers may order different numbers of cups, and each
# type of chai can have a different price per cup.
#
# Instead of writing the multiplication formula repeatedly
# throughout the code, we create a function that calculates
# the total bill.
#
# This improves:
# - Code readability
# - Code reusability
# - Code maintainability
#
# Task:
# • Create a function calculate_bill(cups, price_per_cup)
# • The function should return the total bill
# • Use the function for multiple customer orders
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Define the Function
# ------------------------------------------------------------
# calculate_bill() takes two parameters:
#
# cups → number of chai cups ordered
# price_per_cup → price of one cup of chai
#
# The function returns the total bill amount.

def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


# ------------------------------------------------------------
# Step 2: Use the Function for a Customer Order
# ------------------------------------------------------------
# Here we calculate the bill for a personal order.

my_bill = calculate_bill(4, 20)
print("My bill for chai:", my_bill)


# ------------------------------------------------------------
# Step 3: Use the Same Function for Another Order
# ------------------------------------------------------------
# The same function can be reused for different tables
# or customers.

print("Bill for table 2:", calculate_bill(3, 45))


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# The function calculate_bill() performs the billing logic
# and returns the result using the return keyword.
#
# return → sends the calculated value back to the caller.
#
# This allows the result to be:
# - stored in a variable
# - printed directly
# - reused in other calculations
#
# By moving the billing logic into a function, we avoid
# repeating formulas throughout the code and make the
# program easier to read and maintain.
# ------------------------------------------------------------