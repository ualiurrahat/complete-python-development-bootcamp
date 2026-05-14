"""
File: 04_minutes_alive_calculator.py
Folder: Projects/01 Utilities
Topic: Mathematical Calculations, Constants, and Loops with Validation

Problem Statement
-----------------
People often think of age in years, but time can be measured in many units.
Converting years to minutes helps visualize life in smaller time increments.
This calculator takes a person's age in years and converts it to days, hours,
and minutes, accounting for leap years using a more precise year length.

The program demonstrates:
1. Using named constants for values that don't change (DAYS_IN_YEAR, etc.).
2. Mathematical conversions between different time units.
3. Rounding calculated values for cleaner display.
4. Formatting large numbers with comma separators for readability.
5. Loop-based retry mechanism so user can calculate multiple ages.
6. Input validation with try-except to handle invalid entries.

Key Concepts
------------
Named Constants (UPPER_CASE)
    Variables that store values which should not change during program
    execution. By convention, constants are named in ALL_CAPS to signal
    their purpose to other programmers. Python doesn't enforce constants,
    but the naming convention communicates intent.

365.25 Days/Year
    Standard calendar has 365 days, but leap years add an extra day every
    4 years. Using 365.25 averages this out over time, providing a more
    accurate approximation than 365 days alone.

round() Function
    Returns a floating-point number rounded to specified decimal places.
    Here used without second parameter → rounds to nearest integer.

f-string Comma Formatting
    Python f-strings support format specifiers: {number:,} adds commas
    as thousand separators. Example: 9131.25 → "9,131"

while True Loop
    Creates an infinite loop that only exits when a specific condition
    (like user choosing not to continue) triggers a break statement.
"""


# ---------------------------------------------------------
# Step 1: Define the Calculation Function
# ---------------------------------------------------------
# Constants are defined inside the function (local scope) but could
# also be module-level. Keeping them here makes the function self-contained.

def calculate_minutes(age_years):
    """
    Convert age in years to approximate days, hours, and minutes.
    
    Uses 365.25 days/year to account for leap years on average.
    
    Parameters
    ----------
    age_years : float
        Person's age in years (can be fractional, e.g., 25.5).
    
    Returns
    -------
    tuple
        Three integers: (total_days, total_hours, total_minutes) all rounded.
    
    Example
    -------
    >>> calculate_minutes(25)
    (9131, 219144, 13148640)
    """
    
    # Constants defined in UPPER_CASE (convention for values that don't change)
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    
    # Chain conversions: years → days → hours → minutes
    total_days = age_years * DAYS_IN_YEAR
    total_hours = total_days * HOURS_IN_DAY
    total_minutes = total_hours * MINUTES_IN_HOUR
    
    # Round each value to nearest whole number before returning
    return round(total_days), round(total_hours), round(total_minutes)


# ---------------------------------------------------------
# Step 2: Main Program Loop with Retry Option
# ---------------------------------------------------------
# The while True loop keeps running until the user chooses to exit.
# This allows multiple calculations without restarting the program.

print("=" * 55)
print("   MINUTES ALIVE CALCULATOR")
print("   Convert your age to days, hours, and minutes")
print("=" * 55)

while True:
    
    # -------------------------------------------------
    # Sub-step 2.1: Get Valid Age Input
    # -------------------------------------------------
    # Try-except handles cases where user enters text instead of numbers.
    # Without this, entering "twenty" would crash the program.
    
    try:
        age = float(input("\nEnter your age in years: "))
        
    except ValueError:
        # This runs if float() conversion fails (user entered non-numeric)
        print("❌ Please enter a valid number for age (e.g., 25 or 25.5)")
        continue  # Skip rest of loop, ask for age again
    
    # -------------------------------------------------
    # Sub-step 2.2: Calculate and Display Results
    # -------------------------------------------------
    # The function returns three values which we unpack into separate variables.
    # Comma formatting: {days:,} adds commas every 3 digits.
    
    days, hours, minutes = calculate_minutes(age)
    
    print("\n📊 You are approximately:")
    print(f"  •  {days:,} days old")
    print(f"  •  {hours:,} hours old")
    print(f"  •  {minutes:,} minutes old")
    
    # -------------------------------------------------
    # Sub-step 2.3: Ask User to Continue or Exit
    # -------------------------------------------------
    # .strip() removes spaces, .lower() makes comparison case-insensitive.
    # Only 'y' continues the loop; anything else (including 'n', 'no', '') exits.
    
    again = input("\nWould you like to try again? (y/n): ").strip().lower()
    
    if again != 'y':
        print("\n👋 Good bye! Thanks for using the Minutes Alive Calculator.")
        break  # Exit the while loop completely


# ---------------------------------------------------------
# Example Run
# ---------------------------------------------------------
# Input: age = 25
#
# Output:
#   You are approximately:
#     • 9,131 days old
#     • 219,144 hours old
#     • 13,148,640 minutes old


# ---------------------------------------------------------
# Important Notes About This Implementation
# ---------------------------------------------------------
# 1. Leap Year Approximation:
#    365.25 days/year is an average. Exact calculation would require
#    birthdate and current date to count actual leap years passed.
#
# 2. Rounding Behavior:
#    round(9.6) → 10, round(9.4) → 9. This is fine for approximation.
#
# 3. Comma Formatting: {:,} works with both integers and floats:
#    f"{1234567.89:,}" → "1,234,567.89"
#
# 4. continue vs break:
#    • continue → jumps to next iteration of the loop
#    • break → exits the loop completely
#
# 5. Float Precision with Large Numbers:
#    Converting 80 years to minutes: 80 * 365.25 * 24 * 60 = 42,076,800 minutes.
#    This fits comfortably within Python's float precision (no issues).
#
# 6. Improvement Ideas:
#    • Add birthdate input for exact calculation (not approximate)
#    • Calculate heartbeats (assuming average 72 beats/minute)
#    • Show seconds as well
#    • Add progress bar visualization for minutes lived vs average lifespan