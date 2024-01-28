from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep

game_over = False

MARGIN = 40
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# Setup Screen:
screen = Screen()
screen.tracer(0)
screen.title("Pong!")
screen.setup(SCREEN_WIDTH * 2, SCREEN_HEIGHT * 2)
screen.bgcolor("black")

# Setup Objects:
ball = Ball()

player_1 = Paddle(-SCREEN_WIDTH + MARGIN)
player_1.set_name("Player 1")

player_2 = Paddle(SCREEN_WIDTH - MARGIN - 5)
player_1.set_name("Player 2")

# Setup Listeners:
screen.listen()

screen.onkeypress(player_1.move_up, "w")
screen.onkeypress(player_1.move_down, "s")

screen.onkeypress(player_2.move_up, "Up")
screen.onkeypress(player_2.move_down, "Down")

# Start Game:
while not game_over:
    sleep(0.05)

    ball.move()

    screen.update()

screen.exitonclick()
