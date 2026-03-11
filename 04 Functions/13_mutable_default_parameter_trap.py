# ============================================================
# File: 13_mutable_default_parameter_trap.py
# Chapter: 04 - Functions
# Topic: Mutable Default Parameter Trap
# ============================================================


# Problem Statement:

# Using mutable objects like lists as default parameters
# can cause unexpected behavior because the same object
# is reused across function calls.



# Step 1: Mutable Default Parameter Trap

def chai_order_default_trap(order=[]):
    order.append("Masala")
    print(order)


chai_order_default_trap()   # ['Masala']
chai_order_default_trap()   # ['Masala', 'Masala']



# Step 2: Correct Solution

def chai_order_default_solved(order=None):

    if order is None:
        order = []

    print(order)


chai_order_default_solved()  # []
chai_order_default_solved()  # []



# Explanation:

# Mutable default arguments are shared across function calls.

# The recommended pattern is to use None as the default value
# and create a new object inside the function.