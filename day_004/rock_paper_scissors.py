import random

from day_004.rsc import hands

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

cpu_choice = random.randint(0, 2)

conditions = {0: 2, 1: 0, 2: 1}

hands = [hands.rock, hands.paper, hands.scissors]

print(hands[user_choice])

print('Computer chose:')

print(hands[cpu_choice])

if user_choice == cpu_choice:
    print('Draw!')
elif conditions[user_choice] == cpu_choice:
    print('You win!')
else:
    print('You lose!')
