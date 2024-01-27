from turtle import Turtle, Screen

SCREEN_DIMENSION = 600
SNAKE_DIMENSION = 20
SNAKE_SPEED = 10
STARTING_LENGTH = 3
PLAYER = []

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(SCREEN_DIMENSION, SCREEN_DIMENSION)


def section_position(snake):
    return snake[len(snake) - 1].xcor() - SNAKE_DIMENSION if len(snake) > 0 else 0


def add_segments(snake, amount):
    for n in range(amount):
        snake_segments = Turtle("square")
        snake_segments.color("white")
        snake_segments.penup()
        snake_segments.setx(section_position(snake))
        snake.append(snake_segments)


def move_snake():
    for snake_section in PLAYER:
        snake_section.forward(SNAKE_SPEED)


add_segments(PLAYER, STARTING_LENGTH)

screen.listen()
screen.onkeypress(move_snake, "Right")

screen.exitonclick()
