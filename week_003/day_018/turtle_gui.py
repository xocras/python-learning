from turtle import Turtle, Screen
from random import random

turtle = Turtle()
turtle.shape('turtle')
turtle.color('green')

for i in range(50):
    turtle.color((
        random(),
        random(),
        random()
    ))
    turtle.forward(10 + i)
    turtle.right(30)

screen = Screen()
screen.exitonclick()
