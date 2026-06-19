# Word Frequency Analyzer 

A local Python utility that parses plain text documents, filters out common "stop words" (like 'the', 'and', 'is'), and generates a visual ASCII bar chart of the most frequently used words.
This is pretty much something I built to test out my python skills a little bit after learning some things in class.

## How to Use

Open your terminal in this directory and run the script using Python.

### 1. Run with the default sample text

```bash
python analyzer.py
```

### 2. Run with your own custom text file

Simply pass the name of your text file as a command-line argument.

```bash
python analyzer.py "my_custom_book.txt"
```

## Output

- **Terminal:** Displays a ASCII bar chart of the top 20 words directly in your console.
- **File Export:** Automatically saves a structured report to `frequency_report.txt` in the same directory.
