# ============================================================
# File: 09_passing_mutable_and_immutable_objects.py
# Chapter: 04 - Functions
# Topic: Passing Mutable and Immutable Objects to Functions
# ============================================================


# Problem Statement:

# Python handles mutable and immutable objects differently
# when they are passed to functions.


# Step 1: Passing Immutable Objects (Strings)

chai = "Ginger chai"
print("Initial String chai:", chai)

def prepare_chai(order):
    print("Preparing", order)

prepare_chai(chai)

print("Final String chai:", chai)


# Step 2: Passing Mutable Objects (Lists)

chai = [1, 2, 3]
print("\nInitial chai list:", chai)

def edit_chai(cup):
    cup[1] = 35

edit_chai(chai)

print("Chai list after using as function parameter:", chai)


# Explanation:

# Immutable objects (like strings) cannot be modified
# inside functions.

# Mutable objects (like lists) can be modified and
# the changes are reflected outside the function.