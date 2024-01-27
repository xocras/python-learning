from turtle import Screen
from snake import Snake


SCREEN_SIZE = 600

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(SCREEN_SIZE, SCREEN_SIZE)

snake = Snake(screen)

screen.listen()

screen.onkeypress(snake.turn_north, "Up")
screen.onkeypress(snake.turn_south, "Down")
screen.onkeypress(snake.turn_east, "Right")
screen.onkeypress(snake.turn_west, "Left")

screen.exitonclick()
