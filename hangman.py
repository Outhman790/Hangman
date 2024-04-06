import random
from hangman_words import words
from hangman_draw import stages
from hangman_draw import logo
lifes = 6
print(words)
print(logo)
print(f"Hey buddy, welcome to the hangman game. You have {lifes} lifes.")
print("You have to guess the word correctly before running out of your lifes, otherwise the hangman will die!")

chosen_word = random.choice(words)
chosen_word_len = len(chosen_word)

correct_user_guessing = ['_' for _ in range(chosen_word_len)]
guessed_letters = []

while lifes > 0:
    print(" ".join(correct_user_guessing))
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in guessed_letters:
        # Check if all occurrences of the letter have already been revealed
        if all(chosen_word[i] != guess or correct_user_guessing[i] == guess for i in range(chosen_word_len)):
            print("You've already fully guessed that letter. Try a different one.")
            continue
    
    guessed_letters.append(guess)  # Keep track of all guessed letters
    
    if guess in chosen_word:
        letter_found = False
        for i in range(chosen_word_len):
            if chosen_word[i] == guess and correct_user_guessing[i] == '_':
                correct_user_guessing[i] = guess
                letter_found = True
                print("You guessed it right!")
                break  # Only reveal the next unrevealed occurrence

        if not letter_found:
            print("No more unrevealed occurrences of that letter. Guess another.")
        
        if ''.join(correct_user_guessing) == chosen_word:
            print("Congratulations! You saved the hangman.")
            print(stages[lifes])
            break
    else:
        lifes -= 1
        print(f"Wrong guess! {lifes} lifes left.")
        print(stages[lifes])

    
    if lifes == 0:
        print("You lost! The hangman is dead.")
        print(stages[lifes])
        print(f"The word was: {chosen_word}")