from turtle import Turtle, Screen
from random import random, randint


def choose_turtle():
    chosen_turtle = screen.numinput("Turtle Race", f"Choose your turtle number (1 - {AMOUNT})", 1)
    if chosen_turtle <= 0 or chosen_turtle > AMOUNT:
        choose_turtle()
    return chosen_turtle


def set_turtles(turtle_list):
    for i, turtle in enumerate(turtle_list):
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


def move_turtles(turtle_list):
    for n, turtle in enumerate(turtle_list):
        turtle.forward(randint(0, 20))
        if turtle.xcor() >= GOAL:
            return n + 1
    return move_turtles(turtle_list)


screen = Screen()

w, h = screen.window_width()/2, screen.window_height()/2

AMOUNT = 8

GOAL = w - 100

turtles = [Turtle(visible=False) for turtle in range(AMOUNT)]

choice = choose_turtle()

set_turtles(turtles)

winner = move_turtles(turtles)

print(f"The winner is Turtle #{winner}!")
print(f"{"You won" if choice == winner else "You lost"}!")

screen.exitonclick()
