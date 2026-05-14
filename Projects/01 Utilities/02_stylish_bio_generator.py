"""
File: 02_stylish_bio_generator.py
Folder: Projects/01 Utilities
Topic: String Formatting, User Choice, and File Writing Project

Problem Statement
-----------------
Social media profiles need concise, visually appealing bios that capture
attention quickly. Users want to create stylish bios without manual
formatting. This utility automates bio generation by collecting user
details and offering multiple layout styles.

The program demonstrates:
1. Collecting optional user inputs (emoji, website handle).
2. Offering multiple formatting styles for user to choose from.
3. Using conditional logic (if-elif) to select different output formats.
4. Writing generated content to a text file for permanent storage.
5. String manipulation with emojis and special characters.

Key Concepts
------------
textwrap.dedent()
    Removes common leading whitespace from multi-line strings. Useful when
    writing strings with indentation in code but wanting output without
    that indentation.

with open() Statement
    Context manager that automatically closes the file after the block
    executes. Prevents resource leaks and ensures data is written properly.

encoding="utf-8"
    Specifies Unicode encoding to properly handle emojis and special
    characters. Without this, some systems may raise encoding errors.

.replace() Method
    Returns a new string with specified replacements. Used here to replace
    spaces with underscores for clean filenames.

.lower() Method
    Converts entire string to lowercase for consistent filename formatting.
"""

import textwrap


# ---------------------------------------------------------
# Step 1: Collect User Information
# ---------------------------------------------------------
# .strip() removes accidental spaces from all inputs.
# Website and emoji are optional — user can press Enter to skip.

name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your passion in one line: ").strip()
emoji = input("Enter your favourite emoji (optional): ").strip()
website = input("Enter your website or handle (optional): ").strip()


# ---------------------------------------------------------
# Step 2: Display Style Options and Get User Choice
# ---------------------------------------------------------
# Providing multiple layout options gives users control over the final look.
# Each style formats the same information differently.

print("\nChoose your bio style:")
print("1. Simple lines")
print("2. Vertical flair")
print("3. Emoji sandwich")

style = input("Enter 1, 2, or 3: ").strip()


# ---------------------------------------------------------
# Step 3: Define Bio Generation Function
# ---------------------------------------------------------
# Each style returns a differently formatted string using the same inputs.
# The function keeps the generation logic organized and reusable.

def generate_bio(style):
    """
    Generate a styled bio based on user's selected layout preference.
    
    Parameters
    ----------
    style : str
        User's choice: "1", "2", or "3" representing different layouts.
    
    Returns
    -------
    str
        Formatted bio string ready for display or saving.
    """
    
    if style == "1":
        # Simple lines style: name and profession on one line with separator
        return f"{emoji} {name} | {profession}\n💡 {passion}\n{website}"
    
    elif style == "2":
        # Vertical flair style: each piece on its own line with fire emojis
        return f"{emoji} {name}\n{profession} 🔥\n{passion}\n{website} 🔥"
    
    elif style == "3":
        # Emoji sandwich style: emojis bookend the entire bio
        return f"{emoji * 3}\n{name} - {profession}\n{passion}\n{website}\n{emoji * 3}"
    
    else:
        # Default fallback for invalid input
        return f"{emoji} {name} | {profession}\n{passion}\n{website}"


# ---------------------------------------------------------
# Step 4: Generate and Display the Bio
# ---------------------------------------------------------
# textwrap.dedent() removes indentation so the bio starts at column 0.
# Without dedent(), multi-line strings would include the code's indentation.

bio = generate_bio(style)

print("\nYour stylish bio:\n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)


# ---------------------------------------------------------
# Step 5: Offer to Save to File
# ---------------------------------------------------------
# User can choose whether to persist the generated bio.
# .lower() makes the comparison case-insensitive (accepts Y, y, YES, yes).

save = input("\nDo you want to save this bio to a text file? (y/n): ").lower()

if save == 'y':
    # Create filename from user's name: replace spaces with underscores
    # Example: "Riya Das" becomes "riya_das_bio.txt"
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    
    # Write the bio to file with UTF-8 encoding for emoji support
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    
    print(f"✅ Bio saved to {filename}")
else:
    print("Bio not saved.")


# ---------------------------------------------------------
# Important Notes About This Implementation
# ---------------------------------------------------------
# 1. Emoji Support: Python 3 handles emojis as Unicode characters.
#    The encoding="utf-8" parameter ensures they save correctly to files.
#
# 2. Optional Inputs: User can press Enter to leave emoji or website blank.
#    In style 1, an empty emoji results in just " | Profession" (leading space).
#
# 3. String Multiplication with Emojis: {emoji * 3} repeats the emoji
#    three times. If emoji is empty, this produces an empty string.
#
# 4. No Input Validation: This program assumes valid input. Adding validation
#    would make it more robust (e.g., checking style is 1, 2, or 3).
#
# 5. File Naming: .replace(' ', '_') handles multi-word names like
#    "John Doe" → "john_doe_bio.txt". Single word names remain unchanged.
#
# 6. textwrap.dedent() is necessary because multi-line strings in the
#    function maintain indentation. Compare with/without to see difference.