# ============================================================
# File: 12_touch_on_advanced_data_types.py
# Topic: Introduction to Advanced Python Data Types & Libraries
# ============================================================

# ------------------------------------------------------------
# Purpose of This File:
# ------------------------------------------------------------
# This file is NOT meant for deep learning or full usage of
# advanced Python data types and libraries.
#
# Instead, its purpose is to:
# - Introduce the learner to the existence of advanced modules.
# - Build awareness of Python's vast ecosystem.
# - Prepare mental context for future lessons.
#
# At beginner stage, it is NOT necessary to master these topics.
# They will naturally be learned when real-world requirements arise.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 1. Working with Time Using External Libraries (arrow)
# ------------------------------------------------------------
# Python provides multiple modules for handling date and time:
# - datetime
# - time
# - calendar
# - timedelta
# - dateutil
# - arrow
#
# 'arrow' is a third-party library that simplifies date-time
# handling and timezone management.
#
# Installation (when needed):
#   pip install arrow

import arrow

# Getting the current UTC time
brewing_time = arrow.utcnow()

# Converting UTC time to a specific timezone
rome_time = brewing_time.to("Europe/Rome")

print(f"Current UTC time: {brewing_time}")
print(f"Current Rome time: {rome_time}")

# ------------------------------------------------------------
# 2. Advanced Data Structures from collections Module
# ------------------------------------------------------------
# Python's built-in 'collections' module provides specialized
# container data types that extend the capabilities of basic
# structures like lists, tuples, and dictionaries.
#
# Some important data types inside collections:
# - namedtuple
# - deque
# - Counter
# - defaultdict
# - OrderedDict

from collections import namedtuple

# ------------------------------------------------------------
# 3. namedtuple — Lightweight Object-Like Structure
# ------------------------------------------------------------
# namedtuple creates tuple-like objects with named fields.
# It combines:
# - Immutability of tuples
# - Readability of objects
#
# This makes code:
# - Cleaner
# - More readable
# - More maintainable

ChaiProfile = namedtuple("ChaiProfile", ["flavor", "aroma"])

# Creating an instance of namedtuple
chai = ChaiProfile(flavor="Masala", aroma="Strong")

print(f"Chai flavor: {chai.flavor}")
print(f"Chai aroma: {chai.aroma}")

# ------------------------------------------------------------
# Summary:
# ------------------------------------------------------------
# - Python offers powerful advanced data types and libraries.
# - Beginners do NOT need to learn everything immediately.
# - Learning happens naturally through real-world usage.
#
# Key takeaway:
#   First master fundamentals → then advanced topics become easy.
# ------------------------------------------------------------
