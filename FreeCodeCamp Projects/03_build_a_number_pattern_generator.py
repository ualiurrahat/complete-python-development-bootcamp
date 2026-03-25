"""
File: 03_number_pattern_generator.py
Chapter: FreeCodeCamp Projects
Topic: Functions, Input Validation, and String Construction

Problem Statement
-----------------
Create a function that generates a number pattern as a string.

The function should:
1. Accept a single input `n`.
2. Validate the input.
3. Return a string containing numbers from 1 to n separated by spaces.

Example
-------
Input: 4  
Output: "1 2 3 4"

Rules
-----
• The input must be an integer.
• The input must be greater than 0.
• If invalid, return an appropriate error message.
"""

# ---------------------------------------------------------
# Step 1: Define the function
# ---------------------------------------------------------

def number_pattern(n):
    """
    Generates a space-separated number pattern from 1 to n.

    Parameters
    ----------
    n : int
        The upper limit of the pattern.

    Returns
    -------
    str
        A string containing numbers from 1 to n OR an error message.
    """

    # -----------------------------------------------------
    # Step 2: Input validation
    # -----------------------------------------------------

    # Check if input is an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."

    # Check if integer is positive
    if n < 1:
        return "Argument must be an integer greater than 0."

    # -----------------------------------------------------
    # Step 3: Generate the number pattern
    # -----------------------------------------------------

    # Initialize an empty string to store the result
    num_string = ""

    # Loop from 1 to n-1
    for number in range(1, n):
        # Convert number to string and add space
        num_string += str(number) + " "

    # Add the last number without trailing space
    num_string += str(n)

    # -----------------------------------------------------
    # Step 4: Return the final result
    # -----------------------------------------------------

    return num_string


# ---------------------------------------------------------
# Step 5: Example usage (testing)
# ---------------------------------------------------------

print(number_pattern(4))       # Expected Output: "1 2 3 4"
print(number_pattern(-35))     # Expected Output: Error message
print(number_pattern("rahat")) # Expected Output: Error message