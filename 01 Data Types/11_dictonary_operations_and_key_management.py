# ============================================================
# File: 11_dictionary_operations_and_key_management.py
# Topic: Dictionary Creation, Modification, and Safe Access
# ============================================================

# ------------------------------------------------------------
# 1. Creating a Dictionary Using dict()
# ------------------------------------------------------------
# A dictionary stores data in KEY → VALUE pairs.
#
# Key properties of dictionaries:
# - Keys must be unique.
# - Values can be of any data type.
# - Dictionaries are MUTABLE.
# - Optimized for fast lookup operations.

chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Initial chai order: {chai_order}")

# ------------------------------------------------------------
# 2. Creating an Empty Dictionary and Adding Keys
# ------------------------------------------------------------
# Dictionaries can grow dynamically by assigning new keys.

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Chai recipe: {chai_recipe}")
print(f"Recipe base ingredient: {chai_recipe['base']}")

# ------------------------------------------------------------
# 3. Deleting a Key Using del
# ------------------------------------------------------------
# del removes a specific key-value pair from a dictionary.
# If the key does not exist, Python raises a KeyError.

del chai_recipe["liquid"]
print(f"Chai recipe after deleting liquid: {chai_recipe}")

# ------------------------------------------------------------
# 4. Membership Testing Using 'in'
# ------------------------------------------------------------
# Checks whether a specific key exists in the dictionary.

print(f"Is 'sugar' in the order? {'sugar' in chai_order}")

# ------------------------------------------------------------
# 5. Creating a New Dictionary Literal
# ------------------------------------------------------------
# Using curly braces is the most common way to define dictionaries.

chai_order = {
    "type": "Ginger Chai",
    "size": "Medium",
    "sugar": 1,
    "isHot": "Very hot"
}
print(f"Updated chai order: {chai_order}")

# ------------------------------------------------------------
# 6. Accessing Keys, Values, and Items
# ------------------------------------------------------------
# keys()   → returns all keys
# values() → returns all values
# items()  → returns (key, value) pairs as tuples

print(f"Order keys: {chai_order.keys()}")
print(f"Order values: {chai_order.values()}")
print(f"Order items: {chai_order.items()}")

# ------------------------------------------------------------
# 7. Removing the Last Inserted Item Using popitem()
# ------------------------------------------------------------
# popitem() removes and returns the LAST inserted key-value pair.
# Useful when dynamically managing dictionaries.

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

# ------------------------------------------------------------
# 8. Updating Dictionary Using update()
# ------------------------------------------------------------
# update() merges one dictionary into another.
# If keys already exist, values get overwritten.

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

# ------------------------------------------------------------
# 9. Safe Key Access Using get()
# ------------------------------------------------------------
# Direct access:
#   chai_order["note"]
# would raise KeyError if key does not exist.
#
# get() prevents runtime crashes by returning a default value.

customer_note = chai_order.get("note", "No note provided")
print(f"Customer note: {customer_note}")

# If key exists, get() returns its actual value
customer_note2 = chai_order.get("size", "No note")
print(f"Customer note 2: {customer_note2}")

# ------------------------------------------------------------
# Summary:
# - Dictionaries store key-value pairs.
# - Mutable data structure.
# - Fast lookups using keys.
# - get() ensures safe access.
# - update() merges dictionaries.
# ------------------------------------------------------------
