from turtle import Turtle, Screen

SCREEN_DIMENSION = 600
SNAKE_DIMENSION = 20
STARTING_LENGTH = 15
PLAYER = []

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(SCREEN_DIMENSION, SCREEN_DIMENSION)


def section_position():
    return PLAYER[len(PLAYER) - 1].xcor() - SNAKE_DIMENSION if len(PLAYER) > 0 else 0


def add_segments(amount):
    for n in range(amount):
        snake_segments = Turtle("square")
        snake_segments.color("white")
        snake_segments.penup()
        snake_segments.setx(section_position())
        PLAYER.append(snake_segments)
    screen.update()


def move_tail():
    for segment in range(len(PLAYER)-1, 0, -1):

        x = PLAYER[segment - 1].xcor()
        y = PLAYER[segment - 1].ycor()

        PLAYER[segment].setposition((x, y))


def turn_east():
    if PLAYER[0].heading() == 180:
        return

    move_tail()

    PLAYER[0].setheading(0)
    PLAYER[0].forward(SNAKE_DIMENSION)

    screen.update()


def turn_west():
    if PLAYER[0].heading() == 0:
        return

    move_tail()

    PLAYER[0].setheading(180)
    PLAYER[0].forward(SNAKE_DIMENSION)

    screen.update()


def turn_south():
    if PLAYER[0].heading() == 90:
        return

    move_tail()

    PLAYER[0].setheading(270)
    PLAYER[0].forward(SNAKE_DIMENSION)

    screen.update()


def turn_north():
    if PLAYER[0].heading() == 270:
        return

    move_tail()

    PLAYER[0].setheading(90)
    PLAYER[0].forward(SNAKE_DIMENSION)

    screen.update()


add_segments(STARTING_LENGTH)

screen.listen()

screen.onkeypress(turn_north, "Up")
screen.onkeypress(turn_south, "Down")
screen.onkeypress(turn_east, "Right")
screen.onkeypress(turn_west, "Left")

screen.exitonclick()
