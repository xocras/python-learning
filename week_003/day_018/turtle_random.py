from turtle import Turtle, Screen
from random import random, randint

screen = Screen()
turtle = Turtle()
turtle.width(10)
turtle.speed(100)

turtle.hideturtle()

for i in range(250):
    turtle.color((
        random(),
        random(),
        random()
    ))

    turtle.setheading(randint(0, 3) * 90)
    turtle.forward(30)

screen.exitonclick()
