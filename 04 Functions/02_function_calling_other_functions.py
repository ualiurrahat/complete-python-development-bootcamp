# ============================================================
# File: 02_function_calling_other_functions.py
# Chapter: 04 - Functions
# Topic: Splitting Complex Tasks Using Multiple Functions
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# You are creating a monthly sales report for a café.
#
# Instead of writing all the logic in one large block of code,
# we break the task into smaller functions.
#
# This approach makes code:
# - Easier to read
# - Easier to debug
# - Easier to maintain
#
# Main task:
# Create a function generate_report() that calls
# three helper functions:
#   • fetch_sales()
#   • filter_valid_sales()
#   • summarize_data()
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Function to Fetch Sales Data
# ------------------------------------------------------------
# This function simulates retrieving sales data from
# a database, file, or external system.

def fetch_sales():
    print("Fetching the sales data")


# ------------------------------------------------------------
# Step 2: Function to Filter Valid Sales
# ------------------------------------------------------------
# In real systems, this step removes invalid or
# corrupted records before processing.

def filter_valid_sales():
    print("Filtering valid sales data")


# ------------------------------------------------------------
# Step 3: Function to Summarize the Data
# ------------------------------------------------------------
# This step would normally calculate totals,
# averages, or other useful statistics.

def summarize_data():
    print("Summarizing sales data")


# ------------------------------------------------------------
# Step 4: Main Function to Generate the Report
# ------------------------------------------------------------
# This function acts as a controller.
# It calls the other functions in the correct order
# to complete the full reporting process.

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")


# ------------------------------------------------------------
# Step 5: Execute the Report Process
# ------------------------------------------------------------
# Calling this function runs the entire workflow.

generate_report()


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# Instead of writing one long function, we divided the
# process into smaller functions.
#
# Each function has a single responsibility:
#
# fetch_sales()        → retrieves data
# filter_valid_sales() → cleans the data
# summarize_data()     → processes the data
#
# generate_report() coordinates the entire process
# by calling the other functions in sequence.
#
# This design is called modular programming.
# ------------------------------------------------------------