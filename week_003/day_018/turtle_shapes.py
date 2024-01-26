from turtle import Turtle, Screen
from random import random

screen = Screen()
turtle = Turtle()
turtle.shape('turtle')
turtle.color('green')

turtle.hideturtle()
turtle.penup()
turtle.goto(turtle.xcor() - 50, turtle.ycor() + 100)
turtle.pendown()
turtle.showturtle()

for sides in range(3, 11):
    turtle.color((
        random(),
        random(),
        random()
    ))
    for side in range(sides):
        turtle.forward(100)
        turtle.right(360/sides)


screen.exitonclick()
