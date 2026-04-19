"""
File: 04_requirements_txt_and_dependency_management.py
Chapter: Python Virtual Environment and Project Setup
Topic: requirements.txt and Dependency Reproducibility
Problem Statement:
Understand how to generate a requirements.txt file and why it is critical
for reproducing the same environment across different machines.
"""

# ---------------------- Step 1: Creating requirements.txt ----------------------
# Command used:
# pip freeze > requirements.txt

# The '>' symbol is NOT Python behavior.
# It is a Linux shell operator used to redirect output into a file.
# This works on Windows, macOS, and Linux terminals.


# ---------------------- Step 2: Why requirements.txt is Important ----------------------
# This file lists all installed dependencies and their versions.
# Anyone can recreate the same environment using this file.


# ---------------------- Step 3: Deleting Virtual Environment Folder ----------------------
# You can delete the entire testenv folder after demonstration.
# This is safe because virtual environments can be recreated anytime
# using the requirements.txt file.