# Task:
# Build a simple seat selection system for a train ticket booking platform.
# Based on user input, display the seat features using match-case.

# ---------------------- Taking User Input ----------------------

seat_type = input("Enter seat type (Sleeper/AC/General/Luxury): ").lower()

# ---------------------- Using match-case ----------------------

# match-case is similar to switch-case in other languages.
# It allows clean and readable multi-condition branching.
# The '_' case works like the 'else' condition.
# It runs when none of the above cases match the input.
# This is called the default case in match-case statements.


match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")

    case "ac":
        print("AC - Air conditioned, comfortable ride")

    case "general":
        print("General - Cheapest option, no reservation")

    case "luxury":
        print("Luxury - Premium seats with meals")

    case _:
        print("Invalid seat type")
