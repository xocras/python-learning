from game_over import GameOver
from state import State
import turtle
import pandas


def end_game():
    print("Wrong guess!")

    global game_over
    game_over = True

    # Clear Answers
    for answer in answers:
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

answers = []

while not game_over:

    guess = turtle.textinput("Guess the State", "Name another state:")

    match = states[states['state'] == guess]

    if not len(match):
        end_game()
        continue

    # Display State
    answers.append(State(*[match.iloc[0, n] for n in range(3)]))

turtle.mainloop()

