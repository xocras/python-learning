from turtle import Turtle, Screen
from random import choice
import colorgram

colors = colorgram.extract('rsc/space.jpg', 6)

colors = list(map(lambda c: (c.rgb.r, c.rgb.g, c.rgb.b), colors))

screen = Screen()
screen.colormode(255)

dots, size, gap = 10, 20, 50

turtle = Turtle()
turtle.penup()
turtle.speed(100)
turtle.hideturtle()

turtle.sety(screen.window_height() / 2 - 100)

for y in range(dots):

    turtle.setx(-screen.window_width() / 2 + 150)

    for x in range(dots):
        turtle.dot(size, choice(colors))
        turtle.setx(turtle.xcor() + gap)

    turtle.sety(turtle.ycor() - gap)

screen.exitonclick()
