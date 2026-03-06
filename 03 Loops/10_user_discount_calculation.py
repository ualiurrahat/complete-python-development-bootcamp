# -------------------------------------------------------------
# File: 10_user_discount_calculation.py
# Chapter: 03 Loops
#
# Topic:
# Using Lists, Dictionaries, and Loops to Process Real Data
#
# This example demonstrates a realistic scenario where a system
# processes user purchases and calculates discounts for their
# next visit based on coupon codes.
#
# Concepts covered:
# - List of dictionaries
# - Dictionary lookup
# - Tuple unpacking
# - Default values with dict.get()
# - Looping through structured data
# -------------------------------------------------------------


# -------------------------------------------------------------
# USERS DATA
# -------------------------------------------------------------
# 'users' is a LIST of dictionaries.
#
# Each dictionary represents a user purchase record.
#
# Structure of each user dictionary:
# {
#     "id": <unique user id>,
#     "total": <amount the user paid>,
#     "coupon": <coupon code used by the user>
# }
#
# Example:
# {"id": 1, "total": 100, "coupon": "P20"}
#
# Meaning:
# User 1 paid $100 and used coupon "P20".
# -------------------------------------------------------------

users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]


# -------------------------------------------------------------
# DISCOUNT RULES
# -------------------------------------------------------------
# 'discounts' is a DICTIONARY that stores the rules for each
# coupon code.
#
# Key   -> Coupon code
# Value -> A tuple (percentage_discount, fixed_discount)
#
# Example:
# "P20": (0.2, 0)
#
# Meaning:
# 20% percentage discount
# $0 fixed discount
#
# Another example:
# "P50": (0, 10)
#
# Meaning:
# 0% percentage discount
# $10 fixed discount
#
# This flexible structure allows coupons to provide either:
# - percentage discounts
# - fixed discounts
# - or both
# -------------------------------------------------------------

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10),
}


# -------------------------------------------------------------
# PROCESS EACH USER
# -------------------------------------------------------------
# We loop through the list of users and calculate their discount.
#
# For each user:
# 1. Get the coupon code
# 2. Look up the discount rule from the discounts dictionary
# 3. Calculate the final discount
# -------------------------------------------------------------

for user in users:

    # ---------------------------------------------------------
    # DICTIONARY LOOKUP WITH DEFAULT VALUE
    #
    # discounts.get(key, default)
    #
    # If the coupon exists → return its value
    # If the coupon does NOT exist → return default value
    #
    # Here the default value is (0, 0)
    #
    # (0, 0) means:
    # percentage discount = 0
    # fixed discount = 0
    #
    # This ensures the program does not crash if a coupon
    # code is unknown.
    # ---------------------------------------------------------

    percentage, fixed = discounts.get(user["coupon"], (0, 0))


    # ---------------------------------------------------------
    # DISCOUNT CALCULATION
    #
    # total_discount =
    #       (percentage discount from purchase)
    #     + (fixed bonus discount)
    #
    # Example:
    # total = 100
    # percentage = 0.2
    # fixed = 0
    #
    # discount = (100 * 0.2) + 0
    # discount = 20
    # ---------------------------------------------------------

    discount = user["total"] * percentage + fixed


    # ---------------------------------------------------------
    # PRINT RESULT
    #
    # We access dictionary values using:
    # user["id"]
    # user["total"]
    # ---------------------------------------------------------

    print(
        f"ID {user['id']} paid ${user['total']} "
        f"and got discount for next visit of ${discount}"
    )