# ============================================================
# File: 14_function_return_values.py
# Chapter: 04 - Functions
# Topic: Function Return Values in Python
# ============================================================


# Problem Statement:

# A Python function can return different types of values.
# A function may:
# 1. Return nothing (implicitly returns None)
# 2. Return a single value
# 3. Return multiple values
# 4. Return early based on a condition



# Step 1: Function with No Explicit Return

def make_chai():
    print("Here is your masala chai")


return_value = make_chai()

print(return_value)   # None because the function has no return statement



# Step 2: Empty Function Using pass

def idle_chaiwala():
    pass


print(idle_chaiwala())   # Also returns None



# Step 3: Returning a Single Value

def sold_cups():
    return 120


total = sold_cups()

print(total)



# Step 4: Early Return from a Function

def chai_status(cups_left):

    if cups_left == 0:
        return "Sorry, chai over"

    return "Chai is ready"

    # This line will never execute because the function
    # already returned a value above
    print("chai")


print(chai_status(0))
print(chai_status(5))



# Step 5: Returning Multiple Values

def chai_report():
    return 100, 20, 10   # sold, remaining, not paid


sold, remaining, not_paid = chai_report()

print("Sold:", sold)
print("Remaining:", remaining)



# Explanation:

# If a function has no return statement, Python automatically
# returns None.

# A function can return a single value using the 'return' keyword.

# Multiple values can be returned as a tuple and unpacked
# into multiple variables.

# The 'return' statement immediately exits the function,
# which allows early termination based on conditions.