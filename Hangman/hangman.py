import random
with open("words.txt","r")as file:
    words=file.read().splitlines()
    secret_word=random.choice(words)
print("welcome to hangman")
print("_"*len(secret_word))
guessed_letters=[]
hangman_art = [
    """
     +---+
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]
wrong_guesses=0
while wrong_guesses<6:
    guess = input("Guess a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
       print("Warning: Please enter only one alphabet (A-Z)!")
       continue
    if guess in guessed_letters:
        print("Already guessed")
    else:
        guessed_letters.append(guess)
        if guess in secret_word:
           print("correct guess!")
        else:
           print("wrong guess!")
           wrong_guesses=wrong_guesses+1
           print(hangman_art[wrong_guesses])
    for letter in secret_word:
       if letter in guessed_letters:
           print(letter, end=" ")
       else:
           print("_", end=" ")

    print()
    if all(letter in guessed_letters for letter in secret_word):
        print("You Win!")
        print("The word was:",secret_word)
        break
    if wrong_guesses==6:
        print("game over!")
        print("The word was:",secret_word)
        break


