# ============================================================
# File: 11_variable_length_arguments_args_kwargs.py
# Chapter: 04 - Functions
# Topic: Variable-Length Arguments (*args and **kwargs)
# ============================================================


# Problem Statement:

# Sometimes a function needs to accept a variable number
# of arguments. Python provides two mechanisms for this:
#
# *args  → collects positional arguments
# **kwargs → collects keyword arguments



# Step 1: Define a Function with *args and **kwargs

def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)



# Step 2: Call the Function

special_chai(
    "Cinnamon",
    "Cardamom",
    sweetener="Honey",
    foam="Yes"
)



# Explanation:

# *args collects additional positional arguments into a tuple.

# **kwargs collects additional keyword arguments into a dictionary.

# This allows functions to handle flexible numbers of inputs.