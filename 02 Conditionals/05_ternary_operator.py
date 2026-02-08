# Task:
# You run an online tea store.
# If the order amount is more than $300, delivery is free.
# Otherwise, delivery charge is $30.
# Use the ternary operator to decide the delivery fee.

# ---------------------- Taking User Input ----------------------

order_amount = int(input("Enter the order amount: "))

# ---------------------- Using Ternary Operator ----------------------

# Syntax of ternary operator in Python:
# value_if_true if condition else value_if_false

delivery_fees = 0 if order_amount > 300 else 30

# ---------------------- Output ----------------------

print(f"Delivery fees is: ${delivery_fees}")
