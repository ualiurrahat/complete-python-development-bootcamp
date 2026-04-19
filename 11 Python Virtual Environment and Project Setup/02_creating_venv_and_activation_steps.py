"""
File: 02_creating_venv_and_activation_steps.py
Chapter: Python Virtual Environment and Project Setup
Topic: Creating and Activating Virtual Environment using venv
Problem Statement:
Learn how to create a virtual environment using the built-in venv module
and how to activate and deactivate it from the terminal.
"""

# ---------------------- Step 1: Create a Project Folder ----------------------
# Suppose an example folder name: testenv
# Right click the folder -> Open in Integrated Terminal (VS Code)


# ---------------------- Step 2: Create Virtual Environment ----------------------
# Command used in terminal:

# python -m venv venv
# OR (standard naming convention)
# python -m venv .venv

# This command creates many files and folders inside the project directory.
# These files represent an isolated Python environment.


# ---------------------- Step 3: Activate Virtual Environment ----------------------
# On Windows:
# venv\Scripts\activate

# After activation, you will see (venv) at the beginning of terminal path.
# This indicates that the virtual environment is active.


# ---------------------- Step 4: Deactivate Virtual Environment ----------------------
# To deactivate, simply run:
# deactivate