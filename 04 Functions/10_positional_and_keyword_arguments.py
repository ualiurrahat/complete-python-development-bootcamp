# ============================================================
# File: 10_positional_and_keyword_arguments.py
# Chapter: 04 - Functions
# Topic: Positional and Keyword Arguments
# ============================================================


# Problem Statement:

# Python allows functions to receive arguments in two ways:
# 1. Positional arguments (based on order)
# 2. Keyword arguments (based on parameter names)



# Step 1: Define a Function

def make_chai(tea, milk, sugar):
    print("Tea:", tea, "| Milk:", milk, "| Sugar:", sugar)



# Step 2: Positional Arguments

# Values are assigned based on their order.

make_chai("Milked", "Sugar", "Low")



# Step 3: Keyword Arguments

# Arguments are matched using parameter names.
# Order does not matter.

make_chai(tea="Green", sugar="Medium", milk="No")



# Explanation:

# Positional arguments depend on the order of parameters.

# Keyword arguments explicitly specify parameter names,
# allowing arguments to be passed in any order.