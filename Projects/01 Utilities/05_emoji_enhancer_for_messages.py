"""
File: 05_emoji_enhancer_for_messages.py
Folder: Projects/01 Utilities
Topic: String Manipulation, Dictionaries, and Case-Insensitive Matching

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

The program demonstrates:
1. Using a dictionary as a lookup table for keyword-emoji pairs.
2. Splitting strings into words for individual processing.
3. Stripping punctuation from words for clean matching.
4. Case-insensitive matching using .lower() method.
5. Reconstructing sentences while preserving original word formatting.
6. Dictionary .get() method with default value to avoid KeyError.

Key Concepts
------------
Dictionary as Lookup Table
    Maps keywords (keys) to their corresponding emojis (values).
    Provides O(1) average lookup time for fast matching.

.split() Method
    Splits a string into a list of words using whitespace as delimiter.
    Example: "Hello world" → ["Hello", "world"]

.strip(".,!?")
    Removes specified punctuation characters from both ends of a string.
    Essential for matching words that have punctuation attached.

.get() Method with Default
    dictionary.get(key, default) returns value if key exists,
    otherwise returns default. Prevents KeyError from crashing program.

.join() Method
    Joins list elements into a single string with specified separator.
    " ".join(list) creates space-separated sentence from words.
"""


# ---------------------------------------------------------
# Step 1: Define Keyword-Emoji Mapping Dictionary
# ---------------------------------------------------------
# Keys are trigger words (lowercase for case-insensitive matching).
# Values are the emojis to append after matched words.

emoji_map = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍕",
}


# ---------------------------------------------------------
# Step 2: Get User Input Message
# ---------------------------------------------------------
# The message can be any length and contain any punctuation.

message = input("Enter your message: ")


# ---------------------------------------------------------
# Step 3: Process Each Word Individually
# ---------------------------------------------------------
# Split message into words to examine each one separately.
# We'll build a new list of words with emojis added where needed.

updated_words = []

for word in message.split():
    # Prepare word for dictionary lookup:
    #   • Convert to lowercase for case-insensitive matching
    #   • Strip common punctuation from ends only
    cleaned = word.lower().strip(".,!?;:")
    
    # Look up emoji for cleaned word; returns "" if not found
    emoji = emoji_map.get(cleaned, "")
    
    if emoji:
        # Word matched: append original word + space + emoji
        updated_words.append(f"{word} {emoji}")
    else:
        # No match: keep original word unchanged
        updated_words.append(word)


# ---------------------------------------------------------
# Step 4: Reconstruct and Display Enhanced Message
# ---------------------------------------------------------
# Join all words back together with spaces.
# Original capitalization and punctuation are preserved.

updated_message = " ".join(updated_words)

print("\n" + "=" * 50)
print("✨ ENHANCED MESSAGE ✨")
print("=" * 50)
print(updated_message)
print("=" * 50)


# ---------------------------------------------------------
# Important Notes About This Implementation
# ---------------------------------------------------------
# 1. Case-Insensitive Matching:
#    Original word "Love" becomes "love" for lookup but output keeps "Love".
#    This preserves the user's original capitalization style.
#
# 2. Punctuation Handling:
#    "happy," → cleaned = "happy" (comma removed) → matches successfully.
#    Original "happy," becomes "happy, 😊" (punctuation preserved).
#
# 3. Limitations:
#    • Words with internal punctuation (e.g., "don't") may not match cleanly.
#    • Multiple emojis for same word not supported (only first match).
#    • Emojis added after word, not before or replacing.
#
# 4. Extending the Map:
#    Simply add new key-value pairs to emoji_map dictionary.
#    Example: "sad": "😢", "excited": "🎉"
#
# 5. Edge Cases:
#    • Empty message → empty output (no crash)
#    • Word appears multiple times → emoji added each time
#    • No matching words → original message unchanged