from turtle import Turtle, Screen

SCREEN_DIMENSION = 600
SNAKE_DIMENSION = 20
STARTING_LENGTH = 3
PLAYER = []

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(SCREEN_DIMENSION, SCREEN_DIMENSION)


def section_position(snake):
    return snake[len(snake) - 1].xcor() + SNAKE_DIMENSION if len(snake) > 0 else 0


def add_sections(snake, amount):
    for n in range(amount):
        snake_section = Turtle("square")
        snake_section.color("white")
        snake_section.setx(section_position(snake))
        snake.append(snake_section)


add_sections(PLAYER, STARTING_LENGTH)

screen.exitonclick()
