import string
import os

def load_and_clean_text(filepath):
    """Reads a text file, normalizes case, and strips punctuation."""
    if not os.path.exists(filepath):
        print(f"Error: Could not find '{filepath}'")
        return []

    print(f"Reading and cleaning '{filepath}'...")
    with open(filepath, 'r', encoding='utf-8') as file:
        raw_text = file.read().lower()

    # Create a translator that replaces all punctuation with spaces
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    clean_text = raw_text.translate(translator)
    
    # Split by whitespace into a list of words
    words = clean_text.split()
    return words

if __name__ == "__main__":
    print("--- Word Frequency Analyzer (Phase 1) ---")
    words_list = load_and_clean_text("sample.txt")
    if words_list:
        print(f"Successfully extracted {len(words_list)} words!")
        print(f"Preview: {words_list[:10]}...")
