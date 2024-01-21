# Number Guessing Game Objectives:

import random

answer = random.randint(1, 100)

guess = 0

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

difficulty = input("Choose a difficulty level (Easy/Hard): ").upper()

# Track the number of turns remaining.

lives = 5 if difficulty[0] == "H" else 10


# Allow the player to submit a guess for a number between 1 and 100.

def guess_number():
    return int(input("\nGuess a number between 1 and 100: "))


def correct_guess(guess_check, answer_check):
    return guess_check == answer_check


# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
while lives:

    guess = guess_number()

    if correct_guess(guess, answer):
        break

    lives -= 1

    print("\nToo high." if guess > answer else "\nToo low.")
    print(f"\nYou have {lives} {'tries' if lives != 1 else 'try'} remaining.")

# If they run out of turns, provide feedback to the player.
# If they got the answer correct, show the actual answer to the player.
print(f"\n{'Correct!' if lives else 'You lost!'} The answer was {answer}.")
