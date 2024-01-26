from turtle import Turtle, Screen
from random import random

turtle = Turtle()
turtle.shape('turtle')
turtle.color('green')

turtle.hideturtle()
turtle.penup()
turtle.goto(turtle.xcor() + 100, turtle.ycor() + 100)
turtle.pendown()
turtle.showturtle()

for i in range(80):
    turtle.right(0) if i % 20 else turtle.right(90)

    turtle.color((
        random(),
        random(),
        random()
    ))

    turtle.pendown() if i % 2 else turtle.penup()

    turtle.forward(10)


screen = Screen()
screen.exitonclick()
