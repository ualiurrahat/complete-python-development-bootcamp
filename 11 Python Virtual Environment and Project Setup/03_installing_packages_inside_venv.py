"""
File: 03_installing_packages_inside_venv.py
Chapter: Python Virtual Environment and Project Setup
Topic: Installing and Managing Packages inside Virtual Environment
Problem Statement:
Learn how to install, upgrade, and inspect packages inside a virtual
environment without affecting the global Python installation.
"""

# ---------------------- Step 1: Upgrading pip Inside Virtual Environment ----------------------
# Command:
# pip install --upgrade pip

# This upgrades pip ONLY inside the virtual environment.


# ---------------------- Step 2: Installing Dependencies ----------------------
# Any 'pip install package_name' command now installs the package
# inside this isolated virtual environment.


# ---------------------- Step 3: Checking Installed Dependencies ----------------------
# Command:
# pip freeze

# This shows all packages installed inside the virtual environment.