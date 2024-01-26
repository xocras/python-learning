from turtle import Turtle, Screen
from random import random

turtle = Turtle()
turtle.shape('turtle')
turtle.color('green')

turtle.hideturtle()
turtle.penup()
turtle.goto(turtle.xcor() - 75, turtle.ycor() + 100)
turtle.pendown()
turtle.showturtle()

for i in range(4):
    turtle.color((
        random(),
        random(),
        random()
    ))

    turtle.forward(150)
    turtle.right(90)

screen = Screen()
screen.exitonclick()
