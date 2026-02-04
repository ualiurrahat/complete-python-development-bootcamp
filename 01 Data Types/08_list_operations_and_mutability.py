# ============================================================
# File: 08_list_operations_and_mutability.py
# Topic: Lists, Mutability, and Common List Operations
# ============================================================

# ------------------------------------------------------------
# 1. Creating a List
# ------------------------------------------------------------
# A list is an ordered collection of elements.
# In Python, lists behave very similarly to arrays in
# C, C++, and JavaScript — but with much more flexibility.
#
# Key feature:
# - Lists are MUTABLE, meaning we can modify, add, or remove
#   elements after creation.

ingredients = ["water", "milk", "black tea"]

# ------------------------------------------------------------
# 2. Adding an Element Using append()
# ------------------------------------------------------------
# append() adds a new element to the END of the list.

ingredients.append("sugar")
print(f"Ingredients after adding sugar: {ingredients}")

# ------------------------------------------------------------
# 3. Removing an Element Using remove()
# ------------------------------------------------------------
# remove(value) deletes the FIRST occurrence of the given value.
# If the value does not exist, Python raises an error.

ingredients.remove("water")
print(f"Ingredients after removing water: {ingredients}")

# ------------------------------------------------------------
# 4. Combining Two Lists Using extend()
# ------------------------------------------------------------
# extend() merges elements of one list into another list.
# Unlike append(), extend() does NOT insert the list itself,
# instead it inserts each element individually.

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai ingredients after extending spices: {chai_ingredients}")

# ------------------------------------------------------------
# 5. Inserting an Element at a Specific Index Using insert()
# ------------------------------------------------------------
# insert(index, value) places an element at a specific position.
# Existing elements are shifted to the right.

chai_ingredients.insert(2, "black tea")
print(f"Chai ingredients after inserting black tea: {chai_ingredients}")

# ------------------------------------------------------------
# 6. Removing the Last Element Using pop()
# ------------------------------------------------------------
# pop() removes and RETURNS the last element by default.
# This is useful when we need both removal and the removed value.

last_added_item = chai_ingredients.pop()
print(f"Removed element from chai ingredients: {last_added_item}")
print(f"Chai ingredients after pop(): {chai_ingredients}")

# ------------------------------------------------------------
# 7. Reversing a List Using reverse()
# ------------------------------------------------------------
# reverse() modifies the list in-place and reverses the order
# of all elements.

chai_ingredients.reverse()
print(f"Chai ingredients after reversing: {chai_ingredients}")

# ------------------------------------------------------------
# 8. Sorting a List Using sort()
# ------------------------------------------------------------
# sort() arranges elements in ascending order by default.
# For strings, this means lexicographical (alphabetical) order.

chai_ingredients.sort()
print(f"Chai ingredients after sorting: {chai_ingredients}")

# ------------------------------------------------------------
# Summary:
# - Lists are mutable sequences.
# - append() → adds element at the end.
# - remove() → deletes a specific element.
# - extend() → merges two lists.
# - insert() → inserts element at a specific index.
# - pop() → removes and returns last element.
# - reverse() → reverses the list order.
# - sort() → sorts list elements in ascending order.
# ------------------------------------------------------------
