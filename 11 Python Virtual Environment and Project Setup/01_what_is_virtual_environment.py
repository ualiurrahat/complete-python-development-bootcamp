"""
File: 01_what_is_virtual_environment.py
Chapter: Python Virtual Environment and Project Setup
Topic: Global Environment vs Virtual Environment
Problem Statement:
Understand the difference between global Python environment and virtual
environment, and learn why virtual environments are essential for
professional Python project development.
"""

# ---------------------- Step 1: Understanding Global Environment ----------------------
# The global environment is the default Python installation on your system.
# Any package installed using 'pip install package_name' without a virtual
# environment goes into this global space.

# Problem:
# If multiple projects require different versions of the same package,
# they will conflict with each other in the global environment.


# ---------------------- Step 2: Understanding Virtual Environment ----------------------
# A virtual environment is an isolated Python environment created for
# a specific project. It has its own Python interpreter and its own
# site-packages directory.

# This isolation ensures:
# - No dependency conflicts between projects
# - Clean and reproducible project setup
# - Professional project structure


# ---------------------- Step 3: Tools to Create Virtual Environments ----------------------
# There are multiple tools available:
# - venv (built-in with Python)
# - uv
# - poetry
# - virtualenv

# In this lesson, we focus only on 'venv' as shown by the instructor.