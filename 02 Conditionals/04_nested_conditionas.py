# Filename: 04_device_temperature_monitor.py
# ------------------------------------------
# Problem Statement:
# Write a program that checks the status of a device and monitors its temperature.
#
# Conditions:
# - If the device is "active":
#     - If temperature > 35 → Print "High Temperature!"
#     - Else → Print "Normal Temperature"
# - If the device is "off":
#     - Print "Device is offline."
#
# This program demonstrates:
# - Nested if-else conditions
# - Logical decision making
# - Real-world simulation using conditions


# ---------------------- Input Section ----------------------

# Current status of the device
device_status = "off"

# Current temperature of the device (in Celsius)
temperature = 38


# ---------------------- Processing & Logic ----------------------

# Check if the device is active
if device_status == "active":

    # If device is active, now check temperature condition
    if temperature > 35:
        print("High Temperature!")
    else:
        print("Normal Temperature")

# If the device is not active, check if it is off
elif device_status == "off":
    print("Device is offline.")

# If device status is neither active nor off
else:
    print("Unknown device status!")


# ---------------------- Sample Output ----------------------
# For device_status = "off" and temperature = 32
# Output:
# Device is offline.
