import string
import sys
import os
from collections import Counter

STOP_WORDS = {
    "the", "and", "is", "of", "to", "in", "a", "it", "that", "for", 
    "on", "with", "as", "this", "was", "at", "by", "an", "be", "from", 
    "or", "are", "but", "not", "have", "has", "had", "they", "we", "you",
    "i", "my", "me", "he", "she", "his", "her", "which", "their", "so"
}

def load_and_clean_text(filepath):
    if not os.path.exists(filepath):
        print(f"Error: Could not find '{filepath}'")
        sys.exit(1)

    with open(filepath, 'r', encoding='utf-8') as file:
        raw_text = file.read().lower()

    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    return raw_text.translate(translator).split()

def count_word_frequencies(words_list):
    meaningful_words = [word for word in words_list if word not in STOP_WORDS and len(word) > 1]
    return Counter(meaningful_words)

def generate_ascii_chart(counts, top_n=20):
    """Prints a scaled ASCII bar chart to the terminal."""
    top_words = counts.most_common(top_n)
    if not top_words:
        print("No words to display.")
        return

    max_freq = top_words[0][1]
    max_bar_length = 40 # Max characters for the visual bar
    
    print(f"\n TOP {top_n} WORD FREQUENCIES")
    print("-" * 55)
    for word, freq in top_words:
        bar_length = int((freq / max_freq) * max_bar_length)
        bar = "█" * bar_length
        # Formatting: pad word to 12 chars, print bar, then frequency
        print(f"{word:<12} | {bar} ({freq})")
    print("-" * 55)

def export_report(counts, target_file, top_n=20):
    """Saves the structured list to a text document."""
    report_path = "frequency_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"Word Frequency Report for: {target_file}\n")
        f.write("=" * 40 + "\n")
        for word, freq in counts.most_common(top_n):
            f.write(f"{word}: {freq}\n")
    print(f" Report successfully saved to '{report_path}'")

if __name__ == "__main__":
    # Allow command-line file targeting, fallback to sample.txt
    target = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"
    
    print(f"Initializing Analysis Pipeline for '{target}'...")
    words = load_and_clean_text(target)
    
    if words:
        counts = count_word_frequencies(words)
        generate_ascii_chart(counts, top_n=20)
        export_report(counts, target)
