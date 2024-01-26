from turtle import Turtle, Screen
from random import random, randint

screen = Screen()
turtle = Turtle()

turtle.speed(100)

turtle.hideturtle()

circles = 48

for i in range(circles):
    turtle.left(360 / circles * i)
    turtle.color((
        random(),
        random(),
        random()
    ))

    turtle.circle(100)

screen.exitonclick()
