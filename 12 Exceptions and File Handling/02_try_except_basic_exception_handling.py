"""
File: 02_try_except_basic_exception_handling.py
Chapter: 12 — Exceptions and File Handling
Topic: Basic Exception Handling with try-except

Problem Statement
-----------------
When accessing dictionary keys that may not exist, Python raises a KeyError
and crashes the program. Instead of crashing, we can "catch" this exception
using a try-except block. This allows the program to continue running even
when an error occurs.

This file demonstrates:
1. Basic try-except syntax for catching exceptions.
2. Handling KeyError specifically when accessing dictionary keys.
3. How exception handling prevents program crashes.
4. Program continues execution after handled exception.

Key Concepts
------------
try Block
    Contains code that might raise an exception. Python attempts to execute
    everything inside the try block normally.

except Block
    Executes only if an exception occurs inside the try block. The specific
    exception type (like KeyError) determines which except block runs.

Exception Propagation
    When an exception occurs, Python immediately jumps to the matching
    except block. Remaining code inside try block is skipped.
"""


# Dictionary representing tea menu with prices
tea_menu = {"masala": 30, "ginger": 40}

# ---------------------------------------------------------
# Without Exception Handling (Would Crash)
# ---------------------------------------------------------
# The following line would crash the program:
# tea_menu["elaichi"]  # KeyError: 'elaichi'


# ---------------------------------------------------------
# With Exception Handling (Graceful Failure)
# ---------------------------------------------------------
# try block: attempt to access the key "elaichi"
# except block: catches KeyError specifically and prints friendly message
# Program continues to run after the except block

try:
    # This key doesn't exist in the dictionary
    tea_menu["elaichi"]
    
except KeyError:
    # This runs only if KeyError occurs inside the try block
    print("The key that is being tried to access does not exists!")

# This line always runs regardless of whether exception occurred or not
print("Hello, Pythonista")


# ---------------------------------------------------------
# How try-except Works
# ---------------------------------------------------------
# Step 1: Python enters try block
# Step 2: Tries to execute tea_menu["elaichi"]
# Step 3: KeyError occurs (key not found)
# Step 4: Python immediately exits try block (skips any remaining code in try)
# Step 5: Python looks for except KeyError block
# Step 6: Executes the except block
# Step 7: Continues with code after the try-except structure


# ---------------------------------------------------------
# Important Notes
# ---------------------------------------------------------
# 1. You can catch multiple exception types with multiple except blocks.
# 2. A bare except: (without type) catches ALL exceptions (not recommended).
# 3. Always catch specific exceptions when possible.
# 4. Code inside try block after the exception point never executes.
# 5. Exception handling makes programs robust and user-friendly.