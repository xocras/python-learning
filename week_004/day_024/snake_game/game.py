from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep


def check_collision():
    # Food Collision
    if snake.head.distance(food) <= snake.SEGMENT_SIZE * 1.5:
        food.refresh()
        snake.add_segments(1)
        scoreboard.increase_score(1)

    # Head Position
    x = snake.head.xcor()
    y = snake.head.ycor()

    # Wall Collision
    wall = (x >= BOUNDS or
            x <= -BOUNDS - 5 or
            y <= -BOUNDS or
            y >= BOUNDS - SCOREBOARD_SIZE)

    # Tail Collision
    tail = False
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) <= SEGMENT_SIZE/2:
            tail = True
            break

    # Game Over Message
    if wall or tail:

        # Check Highscore
        scoreboard.update_highscore()

        alert("Game Over")

    return wall or tail


def alert(message):
    alert_box = Turtle(visible=False)
    alert_box.color("white")
    alert_box.write(message, False, "center", ('Courier', 16, 'normal'))


# Settings
SEGMENT_SIZE = 20
SCOREBOARD_SIZE = 64
SCREEN_SIZE = 600
BOUNDS = SCREEN_SIZE / 2 - SEGMENT_SIZE

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

    game_over = check_collision()

    screen.update()

screen.exitonclick()
