# ============================================================
# File: 02_for_loop_with_controlled_iterations.py
# Chapter: 03 Loops
# Topic: Controlling Number of Iterations using range()
# ============================================================

# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# A chai shop prepares tea in batches every 15 minutes.
#
# Task:
# Simulate 4 production batches and print:
#
#     "Preparing chai for batch #[number]"
#
# Note:
# The basic concept of for-loop and range() was introduced
# in the previous file. Here, we focus on controlling
# the exact number of repetitions.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Key Concept Introduced:
# ------------------------------------------------------------
# We can use range(start, stop) to control exactly
# how many times a loop runs.
#
# In this case:
# range(1, 5) → generates 4 iterations
#
# This is useful when:
# - Simulating fixed cycles
# - Running scheduled tasks
# - Processing limited batches
# ------------------------------------------------------------


for batch in range(1, 5):
    print(f"Preparing chai for batch #{batch}")


# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - The loop runs exactly 4 times.
# - Each iteration represents one batch.
# - 'batch' stores the current batch number.
#
# This demonstrates controlled and predictable repetition.
# ------------------------------------------------------------
