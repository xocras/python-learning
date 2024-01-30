from game_over import GameOver
from state import State
import turtle
import pandas

# Notes:
# Series.item(): Returns the first item
# Series.to_list(): Converts series into a list
# ~ Can be used as a not operator


def end_game():
    # Create States to Learn CSV
    complement = states['state'][~states['state'].isin(pandas.Series(answers.keys()))]
    complement.to_csv("states_to_learn.csv", index=False)

    # Clear Answers
    for answer in answers.values():
        answer.clear()

    # Display Game Over
    GameOver()


WIDTH = 725
HEIGHT = 491

game_over = False

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("U.S. States Game")
screen.bgpic("blank_states.gif")

states = pandas.read_csv("50_states.csv")

answers = {}

while len(answers) < 50:

    guess = turtle.textinput(f"Guess the State - {len(answers)}/50", "Name another state:")

    if not len(guess):
        end_game()
        break

    guess = guess.title()

    if guess in answers.keys():
        continue

    match = states[states['state'] == guess]

    if not len(match):
        end_game()
        break

    # Display State
    answers[guess] = State(*[match.iloc[0, n] for n in range(3)])

turtle.mainloop()

