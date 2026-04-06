"""
File: 03_role_based_access_decorator.py
Chapter: 08 — Decorators in Python
Topic: Role-Based Access Control Using Decorators

Problem Statement
-----------------
In real-world applications, certain actions or resources must be restricted
to specific users based on their role. For example, only administrators
should be able to access sensitive data or perform critical operations.

Implementing this check manually inside every protected function would
lead to repeated code across the entire codebase. Decorators solve this
problem by placing the access control logic in one reusable place.

This file demonstrates:
1. What role-based access control is and why it is needed.
2. How a decorator can act as a security gate before a function runs.
3. How to check a condition inside a wrapper and block execution if needed.
4. How the same decorator can protect multiple functions without repetition.

Key Concepts
------------
Role-Based Access Control (RBAC)
    A security approach where access to resources is granted or denied
    based on the role assigned to a user (e.g., "admin", "user", "guest").

Authorization
    The process of verifying whether a user has permission to perform
    a specific action. This is different from authentication, which only
    verifies identity.

Guard Decorator
    A decorator that checks a condition before allowing the original
    function to execute. If the condition fails, execution is blocked
    and an appropriate message is returned.

Early Return
    Stopping a function's execution early by returning before reaching
    the main logic. Used here to block unauthorized access without
    raising an exception.
"""

# ---------------------------------------------------------
# Step 1: Import Required Tool
# ---------------------------------------------------------
# `wraps` is imported from Python's built-in `functools` module.
#
# It preserves the original function's metadata (name, docstring)
# after the decorator wraps it.

from functools import wraps


# ---------------------------------------------------------
# Step 2: Define the Decorator
# ---------------------------------------------------------
# The decorator acts as a security gate.
#
# Before the original function is allowed to run, the wrapper
# checks whether the user has the required role.
#
# If the role check fails:
#   • A denial message is printed
#   • `None` is returned immediately (early return)
#   • The original function is never called
#
# If the role check passes:
#   • The original function is called normally


def requireAdmin(func):
    """
    Decorator that allows function execution only if the user role is 'admin'.

    This acts as a reusable security gate that can be applied to any
    function that requires administrator-level access.

    Parameters
    ----------
    func : function
        The original function being decorated.

    Returns
    -------
    function
        The wrapper function that performs the role check before
        allowing the original function to execute.
    """

    @wraps(func)
    def wrapper(userRole):
        """
        Checks the user's role before allowing access to the function.

        Parameters
        ----------
        userRole : str
            The role of the user attempting to access the function.
            Expected values: "admin", "user", "guest", etc.
        """

        # -------------------------------------------------
        # Step 3: Check the role before allowing execution
        # -------------------------------------------------
        # If the role is not "admin", deny access immediately.
        #
        # Returning `None` here is an early return — it stops
        # the function from continuing to the original call below.

        if userRole != "admin":
            print("Access denied: Admins only")
            return None

        # If the role check passes, call the original function
        # and pass the userRole argument along to it.
        return func(userRole)

    return wrapper


# ---------------------------------------------------------
# Step 4: Apply the Decorator
# ---------------------------------------------------------
# `@requireAdmin` is placed above `accessTeaInventory` to protect it.
#
# Now every call to `accessTeaInventory` will first pass through
# the `wrapper` inside `requireAdmin` before the actual function runs.

@requireAdmin
def accessTeaInventory(role):
    """
    Simulates accessing a protected tea inventory system.

    Parameters
    ----------
    role : str
        The role of the user who was granted access.
    """
    print("Access granted to tea inventory")


# ---------------------------------------------------------
# Step 5: Execute and Observe
# ---------------------------------------------------------
# Test 1: Passing "user" — access should be denied.
# Test 2: Passing "admin" — access should be granted.
#
# Execution flow for "user":
#   1. wrapper receives "user"
#   2. Role check fails
#   3. "Access denied: Admins only" is printed
#   4. Function returns None — original function never runs
#
# Execution flow for "admin":
#   1. wrapper receives "admin"
#   2. Role check passes
#   3. Original `accessTeaInventory` runs
#   4. "Access granted to tea inventory" is printed

accessTeaInventory("user")
accessTeaInventory("admin")