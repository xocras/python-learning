from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.speed(100)


def move_forward():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_left():
    turtle.left(15)


def turn_right():
    turtle.right(15)


screen.listen()

screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backwards, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(turtle.reset, "space")

screen.exitonclick()
