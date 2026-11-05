# Datheon_python_programming_Intership
Python programming internship projects including Hangman Game and File Organizer, developed using Python.
# Hangman Game

## Overview
A command-line based word guessing game developed using Python. The game selects a random word from an external text file and allows the player to guess the hidden word within six incorrect attempts.

## Key Features
- Random word selection from a word list.
- Displays hidden letters using underscores.
- Tracks previously guessed letters.
- Prevents duplicate guesses from reducing attempts.
- Allows a maximum of six incorrect attempts.
- Displays progressive ASCII art for incorrect guesses.
- Shows victory or defeat messages.

## Technologies Used
- Python 3
- Random Module
- File Handling
- ASCII Art

## Functions and Methods Used

| Function / Method | Purpose |
|---|---|
| `open()` | Opens the external word list file. |
| `read()` | Reads the contents of the file. |
| `splitlines()` | Separates the file content into individual words. |
| `random.choice()` | Selects a random word from the list. |
| `input()` | Accepts guesses from the player. |
| `lower()` | Converts input into lowercase. |
| `append()` | Adds guessed letters to a list. |
| `print()` | Displays game information, ASCII art, and results. |

## ASCII Art Implementation
ASCII characters are used to represent the Hangman structure. The illustration updates progressively with each incorrect guess to indicate the remaining attempts.

## Project Structure

```text
Task_1_Hangman/
├── hangman.py
├── words.txt
├── hangman_output1.png
├── hangman_output2.png
└── README.md
```

## How to Run
1. Make sure Python 3 is installed.
2. Keep `hangman.py` and `words.txt` in the same folder.
3. Open the terminal in the project directory.
4. Execute:

```bash
python hangman.py
```

## Outcome
Developed an interactive command-line game using Python fundamentals, random selection, file handling, loops, conditional statements, and ASCII art.
