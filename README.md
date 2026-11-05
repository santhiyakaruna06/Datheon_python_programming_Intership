# Datheon_python_programming_Intership
Python programming internship projects including Hangman Game and File Organizer, developed using Python.
# Python Programming Internship Projects

## Overview
This repository contains Python projects developed as part of the Datheon Python Programming Internship. These projects demonstrate practical implementation of Python programming concepts, problem-solving, file handling, and automation.

---

# Task 1 – Hangman Game

## Overview
A command-line word guessing game developed using Python. The game selects a random word from an external text file and allows the player to guess the hidden word within six incorrect attempts.

## Key Features
- Random word selection from a word list.
- Displays hidden letters using underscores.
- Tracks previously guessed letters.
- Prevents duplicate guesses from reducing attempts.
- Allows a maximum of six incorrect attempts.
- Progressive ASCII art gallows display.
- Victory and defeat messages.

## ASCII Art Implementation
The game uses ASCII characters to represent the Hangman gallows. The gallows illustration updates progressively with each incorrect guess. Each stage visually represents the player's mistakes and remaining attempts.

## Functions and Methods Used

| Function / Method | Purpose |
|---|---|
| `open()` | Opens the external word list file. |
| `read()` | Reads the file contents. |
| `splitlines()` | Separates file content into individual words. |
| `random.choice()` | Selects a random word. |
| `input()` | Accepts guesses from the player. |
| `lower()` | Converts input into lowercase. |
| `append()` | Stores guessed letters in a list. |
| `print()` | Displays game information, ASCII art, and results. |

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

**Step 1:** Install Python 3 on your system.

**Step 2:** Keep `hangman.py` and `words.txt` in the same project folder.

**Step 3:** Open the project folder in Visual Studio Code.

**Step 4:** Open the terminal and execute:

```bash
python hangman.py
```

**Step 5:** Enter one alphabet at a time when prompted. Continue guessing until you win or use all six incorrect attempts.

## Expected Output

The program displays:
- Welcome message.
- Hidden word represented by underscores.
- ASCII Hangman gallows.
- Guessed letters and remaining attempts.
- Winning or losing message.

## Output Screenshots

### Game Execution – Screenshot 1

![Hangman Output 1](hangman_output1.png)

### Game Execution – Screenshot 2

![Hangman Output 2](hangman_output2.png)

---

# Task 2 – File Organizer

## Overview
A Python-based file management utility that automatically organizes files into separate directories based on their file extensions.

## Key Features
- Identifies files using their extensions.
- Categorizes documents, images, videos, archives, and code files.
- Creates destination folders automatically.
- Moves files into their respective folders.
- Checks for existing files.
- Handles file-related exceptions.
- Displays the total number of relocated files.

## File Classification

| Extensions | Category |
|---|---|
| `.txt`, `.pdf`, `.docx` | Documents |
| `.jpg`, `.jpeg`, `.png` | Images |
| `.mp4`, `.mkv` | Videos |
| `.zip`, `.rar` | Archives |
| `.py`, `.html`, `.css` | Code |

## Functions and Methods Used

| Function / Method | Purpose |
|---|---|
| `os.path.join()` | Combines folder and file paths. |
| `os.path.dirname()` | Retrieves the script directory. |
| `os.listdir()` | Lists files in a directory. |
| `os.path.splitext()` | Extracts file extensions. |
| `dict.get()` | Retrieves the destination category. |
| `os.makedirs()` | Creates destination directories. |
| `os.path.exists()` | Checks whether a destination file exists. |
| `shutil.move()` | Moves files to destination folders. |
| `print()` | Displays file movement details and summary. |

## Project Structure

```text
Task_2_File_Organizer/
├── organizer.py
├── Test_Files/
└── README.md
```

## How to Run

**Step 1:** Install Python 3 on your system.

**Step 2:** Place the files you want to organize inside the `Test_Files` folder.

**Step 3:** Open the project folder in Visual Studio Code.

**Step 4:** Open the terminal and execute:

```bash
python organizer.py
```

**Step 5:** The program identifies the file extensions and moves files into their respective category folders.

## Expected Output

Example:

```text
photo.jpg moved to Images
sample.txt moved to Documents
test.py moved to Code

Total files relocated: 3
```

## Output Screenshots

Add your File Organizer execution screenshot here after uploading it to this project folder.

---

## Technologies Used
- Python 3
- Visual Studio Code
- Random Module
- OS Module
- Shutil Module
- File Handling
- Exception Handling

## Internship Details
- **Organization:** Datheon
- **Domain:** Python Programming
- **Duration:** 4 Weeks

## Conclusion
These projects provided practical experience in Python programming, logical problem-solving, file management, and automation while strengthening fundamental programming concepts.
