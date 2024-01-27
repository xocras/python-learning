from turtle import Screen
from snake import Snake
from time import sleep

SCREEN_SIZE = 600

screen = Screen()

snake = Snake(screen)


def run_game():
    sleep(0.1)
    snake.move()
    run_game()


def setup_screen():
    screen.tracer(0)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.setup(SCREEN_SIZE, SCREEN_SIZE)

    screen.listen()

    screen.onkey(snake.turn_north, "Up")
    screen.onkey(snake.turn_south, "Down")
    screen.onkey(snake.turn_east, "Right")
    screen.onkey(snake.turn_west, "Left")


setup_screen()
run_game()

screen.exitonclick()
