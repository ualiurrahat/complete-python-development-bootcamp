"""
File: 03_try_except_else_finally_complete_handling.py
Chapter: 12 — Exceptions and File Handling
Topic: Complete Exception Handling with else and finally

Problem Statement
-----------------
Sometimes you need to run code regardless of whether an exception occurred
(cleanup operations like closing files). Other times, you want code to run
ONLY if no exception occurred (success confirmation messages).

Python provides two additional blocks for these scenarios:
• else: runs only if try block executes WITHOUT any exception
• finally: runs ALWAYS — whether exception occurred or not

This file demonstrates:
1. try-except: catch and handle specific exceptions.
2. else block: execute code only when try block succeeds.
3. finally block: execute cleanup code in all circumstances.
4. How to manually raise exceptions using the raise keyword.

Key Concepts
------------
else Block
    Executes only if the try block completes without raising any exception.
    Useful for code that should run only on success.

finally Block
    Executes ALWAYS — whether an exception occurred or was caught. Used for
    cleanup operations like closing files, releasing resources, or printing
    final messages. The finally block runs even if except block runs.

raise Keyword
    Manually triggers an exception. Used when your code detects an error
    condition that Python wouldn't automatically catch.

Exception Object (as e)
    Captures the exception instance, allowing access to error details like
    the error message string.
"""


def serve_tea(flavor):
    """
    Attempts to serve tea of specified flavor with full exception handling.
    
    Demonstrates try-except-else-finally structure in action.
    
    Parameters
    ----------
    flavor : str
        Type of tea flavor to prepare and serve.
    
    Workflow
    --------
    1. try block: attempt to prepare the tea
    2. if flavor is "unknown", manually raise ValueError
    3. except block: only if ValueError occurs, print error message
    4. else block: only if NO exception occurred, confirm tea is served
    5. finally block: ALWAYS executes — signals next customer
    """
    
    try:
        # Code that might raise an exception
        print(f"Preparing {flavor} tea...")
        
        # Manually raise an exception for invalid input
        # IMPORTANT: This check happens INSIDE the try block
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
        
    except ValueError as e:
        # Runs ONLY if ValueError occurs in try block
        # 'as e' captures the exception object to access its message
        print("Error:", e)
    
    else:
        # Runs ONLY if NO exception occurred in try block
        # This code is skipped if except block executes
        print(f"{flavor} tea is served")
    
    finally:
        # Runs ALWAYS — whether exception occurred or not
        # Even if except block runs, this still executes
        # Even if there's a return statement, this runs before returning
        print("Next customer please!")
    
    # NOTE: The if-else blocks in this function are NOT related.
    # The 'if flavor == "unknown"' is inside the try block.
    # The 'else' is at the try-except level (not connected to the if).


# ---------------------------------------------------------
# Demonstration: Successful Tea Service
# ---------------------------------------------------------
# When flavor is "masala" (valid):
#   • try block: prints preparing message, no exception raised
#   • except block: skipped (no exception)
#   • else block: runs → "masala tea is served"
#   • finally block: always runs → "Next customer please!"
#
print("=== Serving Valid Tea ===")
serve_tea("masala")


print("\n=== Serving Invalid Tea ===")
# ---------------------------------------------------------
# Demonstration: Failed Tea Service
# ---------------------------------------------------------
# When flavor is "unknown":
#   • try block: prints preparing, then raises ValueError
#   • except block: runs → prints error message
#   • else block: skipped (exception occurred)
#   • finally block: always runs → "Next customer please!"
#
serve_tea("unknown")


# ---------------------------------------------------------
# Understanding Block Relationships
# ---------------------------------------------------------
# IMPORTANT: In this code, the 'if' and 'else' are NOT related.
# 
#   • The 'if flavor == "unknown"' is INSIDE the try block
#   • The 'else' belongs to the try-except structure
#
# This is correct and intentional. The if checks for a condition
# to manually raise an exception. The else handles success case
# after the try block completes without exceptions.


# ---------------------------------------------------------
# Execution Flow Summary
# ---------------------------------------------------------
# No Exception Scenario:
#   try → (complete) → else → finally → continue
#
# Exception Caught Scenario:
#   try → (exception) → except → finally → continue
#
# Exception NOT Caught Scenario:
#   try → (exception) → finally → program crashes (if no except matches)
#
# finally always runs in ALL scenarios — even if:
#   • except block has return statement
#   • try block has return statement
#   • exception is raised but not caught


# ---------------------------------------------------------
# Important Notes
# ---------------------------------------------------------
# 1. else only runs when try completes without ANY exceptions.
# 2. finally runs even if there's a return statement in try or except.
# 3. finally is ideal for cleanup: closing files, database connections.
# 4. Order matters: try → except → else → finally (else before finally).
# 5. You can have except without else, or else without finally.
# 6. You cannot have else without except (syntax error).
# 7. You can have finally without except.