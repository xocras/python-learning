from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

# Settings
SCREEN_SIZE = 600

# Setup Screen:
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(SCREEN_SIZE, SCREEN_SIZE)

# Setup Objects:
snake = Snake()
food = Food(SCREEN_SIZE)
scoreboard = Scoreboard(SCREEN_SIZE)

# Setup Listeners:
screen.listen()
screen.onkeypress(snake.turn_north, "Up")
screen.onkeypress(snake.turn_south, "Down")
screen.onkeypress(snake.turn_east, "Right")
screen.onkeypress(snake.turn_west, "Left")

# Start Game:
game_over = False

while not game_over:

    sleep(0.1)

    snake.move()

    if snake.head.distance(food) <= snake.SEGMENT_SIZE * 1.5:
        food.refresh()
        snake.add_segments(1)
        scoreboard.increase_score(1)
        print(f"You ate a fruit! Score: {len(snake.segments) - snake.STARTING_LENGTH}")

    screen.update()

