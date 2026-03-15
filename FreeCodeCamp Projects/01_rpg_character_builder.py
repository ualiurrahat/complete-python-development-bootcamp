"""
File: 01_rpg_character_builder.py
Chapter: FreeCodeCamp Projects
Topic: Functions, Input Validation, and String Formatting

Problem Statement
-----------------
Create a function that builds a role-playing game (RPG) character.

The function should:
1. Validate the character name.
2. Validate the character stats.
3. Display the stats visually using filled and empty dots.

Rules
-----
• Character name must be a string.
• Character name cannot be empty.
• Character name cannot exceed 10 characters.
• Character name cannot contain spaces.

Stats Rules
-----------
• Strength, Intelligence, and Charisma must be integers.
• Each stat must be between 1 and 4.
• The total stat points must equal 7.

Output Format
-------------
Name
STR ●●●○○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
"""

# ---------------------------------------------------------
# Step 1: Define symbols used for visual stat display
# ---------------------------------------------------------

# Filled circle represents a stat point
FULL_DOT = "●"

# Empty circle represents unused stat capacity
EMPTY_DOT = "○"


# ---------------------------------------------------------
# Step 2: Create the character building function
# ---------------------------------------------------------

def create_character(name, strength, intelligence, charisma):
    """
    Creates an RPG character after validating all inputs.

    Parameters
    ----------
    name : str
        Name of the character.
    strength : int
        Strength stat (1–4).
    intelligence : int
        Intelligence stat (1–4).
    charisma : int
        Charisma stat (1–4).

    Returns
    -------
    str
        A formatted character sheet OR an error message.
    """

    # -----------------------------------------------------
    # Step 2.1: Validate the character name
    # -----------------------------------------------------

    # Check if the name is a string
    if not isinstance(name, str):
        return "The character name should be a string"

    # Check if the name is empty
    if not name:
        return "The character should have a name"

    # Check name length
    if len(name) > 10:
        return "The character name is too long"

    # Check for spaces in the name
    if " " in name:
        return "The character name should not contain spaces"

    # -----------------------------------------------------
    # Step 2.2: Validate the stats data types
    # -----------------------------------------------------

    # Ensure all stats are integers
    if not all(isinstance(stat, int) for stat in (strength, intelligence, charisma)):
        return "All stats should be integers"

    # -----------------------------------------------------
    # Step 2.3: Validate stat ranges
    # -----------------------------------------------------

    # Each stat must be at least 1
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    # Each stat must be at most 4
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    # Total stat points must equal 7
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # -----------------------------------------------------
    # Step 3: Build the formatted character sheet
    # -----------------------------------------------------

    # Character name line
    line1 = f"{name}"

    # Visual stat bars using multiplication of strings
    # Example: "●" * 3 → "●●●"
    line2 = f"STR {FULL_DOT * strength}{EMPTY_DOT * (10 - strength)}"
    line3 = f"INT {FULL_DOT * intelligence}{EMPTY_DOT * (10 - intelligence)}"
    line4 = f"CHA {FULL_DOT * charisma}{EMPTY_DOT * (10 - charisma)}"

    # Combine all lines using newline characters
    character_sheet = f"{line1}\n{line2}\n{line3}\n{line4}"

    return character_sheet


# ---------------------------------------------------------
# Step 4: Example usage (testing the function)
# ---------------------------------------------------------

print(create_character("ren", 4, 2, 1))