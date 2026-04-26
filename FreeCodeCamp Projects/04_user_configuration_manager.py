"""
File: 04_user_configuration_manager.py
Chapter: FreeCodeCamp Projects
Topic: User Configuration Manager - Dictionary Operations

Problem Statement
-----------------
Applications often need to store and manage user preferences like theme,
language, notification settings, and volume levels. This configuration
data is typically stored as key-value pairs, making Python dictionaries
the perfect data structure for the job.

This project implements a complete configuration management system that
allows users to add, update, delete, and view settings. Each operation
includes proper error handling, case-insensitive key management, and
formatted output messages.

This project demonstrates:
1. Dictionary operations: add, update, delete, and iterate through items.
2. Case-insensitive key handling by converting everything to lowercase.
3. String formatting with f-strings for user-friendly output messages.
4. Error handling for duplicate keys and missing settings.
5. Dictionary emptiness checking and formatted display with capitalization.

Key Concepts
------------
Dictionary
    A mutable collection that stores key-value pairs. Keys must be unique
    and immutable (strings, numbers, tuples). This project uses string keys
    for configuration settings.

Case Insensitivity
    User input may come in any case (e.g., "Theme", "THEME", "theme").
    By converting all keys and values to lowercase, we ensure consistent
    behavior regardless of how the user types the setting name.

Formatting with f-strings
    Python's formatted string literals allow embedding variables directly
    into strings using curly braces: f"Hello {name}"

rstrip() Method
    Removes trailing characters from a string. Used here to remove the
    final newline character so the output doesn't end with a blank line.
"""


# ---------------------------------------------------------
# Test Data: Initial User Configuration
# ---------------------------------------------------------
# This dictionary stores the initial settings for testing.
# In a real application, this might be loaded from a file or database.

test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}


# ---------------------------------------------------------
# Function 1: Add a New Setting
# ---------------------------------------------------------
# Purpose: Add a key-value pair to the settings dictionary.
# Behavior:
#   1. Convert key and value to lowercase for case-insensitive storage.
#   2. Check if the key already exists.
#   3. If exists → return error message (no modification).
#   4. If doesn't exist → add to dictionary and return success message.

def add_setting(settings, pair):
    """
    Add a new key-value pair to the settings dictionary.

    Parameters
    ----------
    settings : dict
        The configuration dictionary to modify.
    pair : tuple
        A tuple containing (key, value) for the new setting.

    Returns
    -------
    str
        Success message if setting was added, error message if key exists.
    """
    # Extract key and value from the tuple and convert to lowercase
    key = pair[0].lower()
    value = pair[1].lower()
    
    # Check if the setting already exists
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        # Add the new key-value pair to the dictionary
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


# ---------------------------------------------------------
# Function 2: Update an Existing Setting
# ---------------------------------------------------------
# Purpose: Change the value of an existing setting.
# Behavior:
#   1. Convert key and value to lowercase.
#   2. Check if the key exists in the dictionary.
#   3. If exists → update the value and return success message.
#   4. If doesn't exist → return error message (no modification).

def update_setting(settings, pair):
    """
    Update an existing setting with a new value.

    Parameters
    ----------
    settings : dict
        The configuration dictionary to modify.
    pair : tuple
        A tuple containing (key, new_value) for the setting to update.

    Returns
    -------
    str
        Success message if setting was updated, error message if key doesn't exist.
    """
    # Extract key and value and convert to lowercase
    key = pair[0].lower()
    value = pair[1].lower()
    
    # Check if the setting exists before updating
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


# ---------------------------------------------------------
# Function 3: Delete a Setting
# ---------------------------------------------------------
# Purpose: Remove a key-value pair from the settings dictionary.
# Behavior:
#   1. Convert the key to lowercase.
#   2. Check if the key exists in the dictionary.
#   3. If exists → delete the key-value pair and return success message.
#   4. If doesn't exist → return error message.

def delete_setting(settings, key):
    """
    Remove a setting from the configuration dictionary.

    Parameters
    ----------
    settings : dict
        The configuration dictionary to modify.
    key : str
        The key of the setting to delete.

    Returns
    -------
    str
        Success message if setting was deleted, error message if key not found.
    """
    # Convert key to lowercase for case-insensitive lookup
    key = key.lower()
    
    # Check if the key exists before deletion
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"


# ---------------------------------------------------------
# Function 4: View All Settings
# ---------------------------------------------------------
# Purpose: Display all current settings in a formatted, readable way.
# Behavior:
#   1. Check if the dictionary is empty.
#   2. If empty → return "No settings available."
#   3. If not empty → build a formatted string with capitalized keys.
#   4. Capitalize the first letter of each setting name for display.
#   5. Use "Key: value" format (colon with space after, no space before).
#   6. End each line with newline, including the last line.

def view_settings(settings):
    """
    Return a formatted string of all current settings.

    Parameters
    ----------
    settings : dict
        The configuration dictionary to display.

    Returns
    -------
    str
        Formatted settings string with capitalized keys, or "No settings available."
    """
    # Check if there are any settings to display
    if not settings:
        return "No settings available."
    
    # Start with the header line (includes a newline at the end)
    display_msg = "Current User Settings:\n"
    
    # Iterate through each key-value pair
    for key, value in settings.items():
        # Capitalize only the first letter of the key for display
        key = key.capitalize()
        # IMPORTANT: Format is "Key: value" (space after colon, no space before)
        display_msg += f"{key}: {value}\n"
    
    # Return with trailing newline intact (as required by tests)
    return display_msg


# ---------------------------------------------------------
# Demonstration and Testing
# ---------------------------------------------------------
# The following code tests all four functions with various scenarios.
# Each test case verifies both success and error conditions.

print("=" * 50)
print("Testing add_setting function:")
print("=" * 50)

# Test 1: Try to add a setting that already exists (should fail)
print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
# Expected: Setting 'theme' already exists! Cannot add a new setting with this name.

# Test 2: Add a completely new setting (should succeed)
print(add_setting({'theme': 'light'}, ('volume', 'high')))
# Expected: Setting 'volume' added with value 'high' successfully!

print("\n" + "=" * 50)
print("Testing update_setting function:")
print("=" * 50)

# Test 3: Update an existing setting (should succeed)
print(update_setting({'theme': 'light'}, ('theme', 'dark')))
# Expected: Setting 'theme' updated to 'dark' successfully!

# Test 4: Try to update a non-existent setting (should fail)
print(update_setting({'theme': 'light'}, ('volume', 'high')))
# Expected: Setting 'volume' does not exist! Cannot update a non-existing setting.

print("\n" + "=" * 50)
print("Testing delete_setting function:")
print("=" * 50)

# Test 5: Delete an existing setting (should succeed)
print(delete_setting({'theme': 'light'}, 'theme'))
# Expected: Setting 'theme' deleted successfully!

print("\n" + "=" * 50)
print("Testing view_settings function:")
print("=" * 50)

# Test 6: View settings with empty dictionary
print(view_settings({}))
# Expected: No settings available.

# Test 7: View settings with populated dictionary
print(view_settings(test_settings))
# Expected:
# Current User Settings:
# Theme: dark
# Notifications: enabled
# Volume: high
# (with a blank line at the end due to trailing newline)


# ---------------------------------------------------------
# Important Notes About This Implementation
# ---------------------------------------------------------
# 1. Case Insensitivity: All keys are stored in lowercase. This means
#    'Theme', 'THEME', and 'theme' all refer to the same setting.
#
# 2. Key Capitalization: Display uses .capitalize() which only capitalizes
#    the first letter. Multi-word keys like "notification_preferences"
#    become "Notification_preferences" (underscore preserved).
#
# 3. Tuple Parameters: Both add_setting and update_setting receive a tuple
#    containing (key, value). This enforces that both parts are provided
#    together as a single unit.
#
# 4. No Print Inside Functions: All functions return strings rather than
#    printing directly. This follows the single responsibility principle
#    and makes the functions more reusable.
#
# 5. Dictionary Mutation: Functions modify the dictionary in-place when
#    operations succeed. No new dictionary is created, which is efficient
#    for large configuration objects.