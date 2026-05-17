"""
File: 06_daily_learning_journal_logger.py
Folder: Projects/01 Utilities
Topic: File Handling, Datetime Formatting, and Appending Data

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5

The program demonstrates:
1. Opening files in append mode ('a') to add without overwriting.
2. Using datetime.datetime.now() to capture current date and time.
3. strftime() method for custom date/time string formatting.
4. Optional user input handling (rating can be skipped).
5. Writing formatted multi-line strings to files.
6. UTF-8 encoding to support emojis and special characters.

Key Concepts
------------
File Append Mode ('a')
    Opens a file for writing, but positions the cursor at the end.
    New content is added after existing content. If file doesn't exist,
    it is created automatically.

datetime.datetime.now()
    Returns a datetime object representing the current moment
    (date and time) based on system clock.

strftime() Method
    "String format time" — converts datetime object to formatted string.
    Format codes:
    • %Y → 4-digit year (2025)
    • %m → 2-digit month (06)
    • %d → 2-digit day (14)
    • %I → 12-hour hour (10)
    • %M → 2-digit minute (45)
    • %p → AM/PM

with open() Statement
    Context manager that automatically closes the file when block exits.
    Prevents resource leaks and ensures data is flushed to disk.

UTF-8 Encoding
    Supports all Unicode characters including emojis (🌟, 📅, ⭐).
    Without encoding="utf-8", some systems may raise encoding errors.
"""

import datetime


# ---------------------------------------------------------
# Step 1: Collect Learning Entry and Optional Rating
# ---------------------------------------------------------
# .strip() removes accidental leading/trailing spaces.
# Rating is optional — user can press Enter to skip.

entry = input("What did you learn today? ").strip()
rating = input("⭐ Rate your productivity today (1-5, optional): ").strip()


# ---------------------------------------------------------
# Step 2: Generate Timestamp with Custom Format
# ---------------------------------------------------------
# now() captures current date and time.
# strftime() formats it as: "2025-06-14 - 10:45 AM"

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d - %I:%M %p")


# ---------------------------------------------------------
# Step 3: Build Journal Entry as Multi-Line String
# ---------------------------------------------------------
# Using f-strings with newline characters for clean formatting.
# Each entry is visually separated from previous entries.

journal_entry = f"\n📅 {timestamp}\n{entry}"

# Add rating only if user provided one (non-empty string)
if rating:
    journal_entry += f"\n⭐ Productivity Rating: {rating}/5"

# Add separator line between entries for readability
journal_entry += "\n" + "-" * 50


# ---------------------------------------------------------
# Step 4: Append Entry to Journal File
# ---------------------------------------------------------
# Mode 'a' = append. File is created if it doesn't exist.
# encoding="utf-8" ensures emojis save correctly.

with open("learning_journal.txt", "a", encoding="utf-8") as file:
    file.write(journal_entry)


# ---------------------------------------------------------
# Step 5: Display Confirmation Message
# ---------------------------------------------------------
# User feedback confirms the operation succeeded.
# Shows filename so user knows where to find their journal.

print(f"\n✅ Your journal entry has been saved to 'learning_journal.txt'")


# ---------------------------------------------------------
# Important Notes About This Implementation
# ---------------------------------------------------------
# 1. Append Mode Safety:
#    'a' never overwrites existing content. Even if program runs
#    multiple times, all entries are preserved in chronological order.
#
# 2. strftime Format Codes:
#    %I (capital I) = 12-hour clock (01-12)
#    %H (capital H) = 24-hour clock (00-23)
#    %p = AM/PM designation
#
# 3. Optional Rating Logic:
#    if rating: checks if string is non-empty.
#    User pressing Enter gives empty string "" → condition False.
#
# 4. File Location:
#    Without path specified, file saves in current working directory
#    (same folder as the Python script).
#
# 5. Multi-Line Strings:
#    Using \n within f-strings creates line breaks.
#    Opening the .txt file in any text editor shows formatted entries.
#
# 6. Improvement Ideas:
#    • Add error handling for invalid rating values
#    • Ask for topic tags (#python, #oop) for searchability
#    • Add function to read and display past entries
#    • Export journal to PDF or CSV
#    • Add search functionality to find entries by keyword
#
# 7. Real-World Application:
#    This pattern is used in logging systems, audit trails, and
#    any application that needs to record events over time.