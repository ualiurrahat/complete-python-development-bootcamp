# ============================================================
# File: 16_function_documentation_and_docstrings.py
# Chapter: 04 - Functions
# Topic: Function Documentation and Docstrings in Python
# ============================================================


# Problem Statement:

# Good programs are not only written for computers but also
# for humans to read and understand. Python provides a
# built-in way to document functions using **Docstrings**.
#
# A Docstring (Documentation String) is a string written
# inside triple quotes that explains what a function does.
#
# It helps developers understand:
# - What the function does
# - What parameters it expects
# - What values it returns



# ============================================================
# 1. WRITING A BASIC DOCSTRING
# ============================================================

def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""
    chai = "ginger"
    return flavor


# Explanation:
#
# The string written in triple quotes is called a **Docstring**.
#
# Important rule:
# A docstring must appear as the **first statement inside the
# function body**. Otherwise Python will not treat it as the
# function documentation.


print("Docstring of chai_flavor():")
print(chai_flavor.__doc__)

print("Function name:")
print(chai_flavor.__name__)


# Explanation:
#
# __doc__  -> Returns the documentation string of the function
# __name__ -> Returns the name of the function
#
# The "__" prefix and suffix are called **dunder**
# which stands for **Double UNDERscore**.
#
# Example pronunciation:
# __doc__  -> "dunder doc"
# __name__ -> "dunder name"



# ============================================================
# 2. DOCUMENTATION OF BUILT-IN FUNCTIONS
# ============================================================

# Python provides a built-in function called help()
# which displays documentation for any object.


# Example:
# help(len)

# Running this command will show detailed information about
# the built-in len() function including:
# - What it does
# - What arguments it accepts
# - What it returns



# ============================================================
# 3. DOCUMENTING A USER-DEFINED FUNCTION
# ============================================================

def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa.

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosas (15 rupees each)
    :return: (total amount, thank you message as string)
    """

    total = chai * 10 + samosa * 15
    return total, "Thank you for visiting visiting us!"


bill, message = generate_bill(3, 2)

print("Total Bill:", bill)
print(message)


# Explanation:
#
# In this function we wrote a more detailed docstring.
#
# The docstring describes:
#
# :param chai:
#     Explains the parameter 'chai'
#
# :param samosa:
#     Explains the parameter 'samosa'
#
# :return:
#     Explains what the function returns
#
# This structured documentation style is commonly used
# in professional Python projects and helps tools like
# documentation generators automatically create API docs.
