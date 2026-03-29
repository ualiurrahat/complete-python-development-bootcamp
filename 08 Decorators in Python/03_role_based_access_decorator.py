"""
File: 03_role_based_access_decorator.py
Chapter: 08 — Decorators in Python
Topic: Role-Based Access Control Using Decorators

Problem Statement:
Demonstrate how a decorator can be used to restrict access to a function
based on user role, simulating a simple role-based authorization system.
"""

# ---------------------- Step 1: Import Required Tool ----------------------
from functools import wraps


# ---------------------- Step 2: Define the Decorator ----------------------
def requireAdmin(func):
    """
    Decorator that allows function execution only if the user role is 'admin'.

    Parameters:
    func (function): The original function to be decorated.

    Returns:
    function: Wrapped function with access control.
    """

    @wraps(func)
    def wrapper(userRole):
        """
        Checks the role before allowing access to the function.
        """
        if userRole != "admin":
            print("Access denied: Admins only")
            return None
        return func(userRole)

    return wrapper


# ---------------------- Step 3: Apply the Decorator ----------------------
@requireAdmin
def accessTeaInventory(role):
    """
    Simulates accessing a protected tea inventory system.
    """
    print("Access granted to tea inventory")


# ---------------------- Step 4: Execute and Observe ----------------------
accessTeaInventory("user")
accessTeaInventory("admin")