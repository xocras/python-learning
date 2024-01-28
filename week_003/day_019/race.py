from turtle import Turtle, Screen
from random import random, randint


def choose_turtle():
    chosen_turtle = screen.numinput(
        "Turtle Race",
        f"Choose your turtle number (1 - {AMOUNT})",
        1
    )

    chosen_turtle = chosen_turtle or 1

    if chosen_turtle <= 0 or chosen_turtle > AMOUNT:
        choose_turtle()
    return chosen_turtle


def set_turtles():
    for i, turtle in enumerate(turtles):
        turtle.penup()
        turtle.shape("turtle")
        turtle.setx(-w + 50)
        turtle.sety(h - 60 - 75 * i)
        turtle.color((
            random(),
            random(),
            random()
        ))
        turtle.showturtle()
        turtle.pendown()


def set_goal():
    finish_line = Turtle(visible=False)
    finish_line.penup()
    finish_line.setposition((GOAL, h - 40))
    finish_line.pendown()
    finish_line.setposition((GOAL, -h + 40))


def move_turtles():
    for n, turtle in enumerate(turtles):
        turtle.forward(randint(0, 20))
        if turtle.xcor() >= GOAL:
            return n + 1
    return move_turtles()


screen = Screen()

w = screen.window_width()/2
h = screen.window_height()/2

AMOUNT = 8

GOAL = w - 100

turtles = [Turtle(visible=False) for turtle in range(AMOUNT)]

choice = choose_turtle()

screen.tracer(0)

set_goal()
set_turtles()

screen.tracer(1)

winner = move_turtles()
message = "You won" if choice == winner else "You lost"

print(f"The winner is Turtle #{winner}!")
print(f"{message}!")

screen.exitonclick()
