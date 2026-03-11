# ============================================================
# File: 12_default_function_parameters.py
# Chapter: 04 - Functions
# Topic: Default Function Parameters
# ============================================================


# Problem Statement:

# Python allows functions to define default values for
# parameters. If an argument is not provided when calling
# the function, the default value is used.



# Step 1: Define a Function with Default Parameters

def make_chai(tea="Regular", milk="Yes", sugar="Medium"):
    print("Tea:", tea, "| Milk:", milk, "| Sugar:", sugar)



# Step 2: Call the Function Without Arguments

make_chai()



# Step 3: Override Some Default Values

make_chai(tea="Green")



# Explanation:

# Default parameters provide fallback values when arguments
# are not supplied.

# This helps make functions more flexible and easier to use.