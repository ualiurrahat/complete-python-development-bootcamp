# ============================================================
# File: 05_improving_traceability_using_functions.py
# Chapter: 04 - Functions
# Topic: Improving Traceability Using Functions
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# Your chai shop applies a 10% VAT (Value Added Tax) on every
# customer order.
#
# Instead of calculating VAT manually every time, you want
# a consistent and traceable way to apply this tax.
#
# By creating a dedicated function, the VAT logic stays
# centralized and easy to update if tax rules change.
#
# Task:
# • Write a function add_vat(price, vat_rate)
# • The function should return the final price after VAT
# • Use the function to compute final prices for several orders
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Define the VAT Calculation Function
# ------------------------------------------------------------
# price → original bill amount
# vat_rate → percentage of VAT applied
#
# Formula used:
# final_price = price * (100 + vat_rate) / 100
#
# Example:
# If price = 100 and VAT = 10%
# final_price = 100 * 110 / 100 = 110

def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100


# ------------------------------------------------------------
# Step 2: List of Customer Orders
# ------------------------------------------------------------
# These represent the original bill amounts before VAT.

orders = [100, 150, 200, 300, 450]


# ------------------------------------------------------------
# Step 3: Apply VAT to Each Order
# ------------------------------------------------------------
# We loop through each order price and calculate the
# final amount including VAT.

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original bill: {price}, Final with VAT: {final_amount}")


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# The function add_vat() encapsulates the tax calculation
# logic in one place.
#
# Benefits of this approach:
#
# • Consistency:
#   Every order uses the same VAT calculation.
#
# • Traceability:
#   If VAT rules change, only this function needs updating.
#
# • Reusability:
#   The same function can be reused anywhere in the program.
#
# This is a practical example of using functions to keep
# business logic centralized and maintainable.
# ------------------------------------------------------------