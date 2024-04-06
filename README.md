Hangman Game in Python
Description

This Hangman project is a classic word guessing game implemented in Python. The game challenges players to guess a secret word by suggesting letters within a limited number of attempts. The project is structured into three main files for easy gameplay and customization.
Files

    hangman.py: The main game file. Run this file to start playing the Hangman game. It handles game logic, user input, and communicates with the other modules to manage the game flow.
    hangman_draw.py: Contains functions to draw the hangman figure. It visually represents the player's remaining guesses and updates with each incorrect guess.
    hangman_words.py: This file includes a list of words from which the secret word is chosen. You can modify this list to add more words or change the game's difficulty.

Installation

Ensure you have Python 3.6 or newer installed on your machine. Clone or download this project, navigate to its directory, and run the following command:

python hangman.py

How to Play

    After starting the game, you're prompted to guess a letter.
    Enter a single letter and press Enter.
    Correct guesses will reveal the letter in the word.
    Incorrect guesses will add to the hangman drawing.
    The game ends when you correctly guess the word or run out of attempts.
