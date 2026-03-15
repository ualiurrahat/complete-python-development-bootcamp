"""
File: travel_transportation_decision.py
Chapter: FreeCodeCamp Projects
Topic: Conditional Logic and Decision Making

Problem Statement
-----------------
Create a simple decision system that determines whether
a person can travel based on several conditions.

Inputs
------
distance_mi          : Distance to destination in miles
is_raining           : Whether it is raining
has_bike             : Whether the person has a bike
has_car              : Whether the person has a car
has_ride_share_app   : Whether the person can use a ride sharing app

Rules
-----
1. If distance is 0 → travel is not required.
2. If distance ≤ 1 mile:
      Walk if it is not raining.
3. If distance is between 1 and 6 miles:
      Bike if the user has a bike and it is not raining.
4. If distance > 6 miles:
      Travel if the user has a car OR ride share access.

Output
------
Print "True" if travel is possible.
Print "False" otherwise.
"""

# ---------------------------------------------------------
# Step 1: Define the travel conditions
# ---------------------------------------------------------

distance_mi = 1
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True


# ---------------------------------------------------------
# Step 2: Decision logic for transportation
# ---------------------------------------------------------

# Case 1: Distance is zero
if not bool(distance_mi):

    # No travel needed
    print("False")


# Case 2: Walking distance
elif distance_mi <= 1:

    # Walking is allowed only if it is not raining
    if not is_raining:
        print("True")
    else:
        print("False")


# Case 3: Medium distance (bike option)
elif 1 < distance_mi <= 6:

    # Can bike only if the user owns a bike and it is not raining
    if has_bike and not is_raining:
        print("True")
    else:
        print("False")


# Case 4: Long distance (vehicle required)
else:

    # Travel possible if car OR ride share is available
    if has_car or has_ride_share_app:
        print("True")
    else:
        print("False")