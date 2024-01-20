# Hangman

import random

# Possible Answers

word_list = ["aardvark", "baboon", "camel"]

lives = 5

choice = random.choice(word_list)

placeholder = list(map(lambda _: '_', choice))

message = 'You win!'

# Debugging: Display Answer
print(f'Pssst... {choice}')


def replace_letter():
    for i, c in enumerate(choice):
        if c == letter:
            placeholder[i] = c


while lives and '_' in placeholder:

    print(f'\n {placeholder} \n')

    letter = input("Choose a letter: ")

    if letter in choice:
        print("\nCorrect!")
        replace_letter()
        message = 'You win!'
    else:
        print("\nWrong choice!")
        lives -= 1
        print(f"\n{lives} {('lives' if lives > 1 or not lives else 'life')} left.")
        message = 'You lose!'

print(f"\n{message}")