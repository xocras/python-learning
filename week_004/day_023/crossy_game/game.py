from turtle import Screen
from player import Player
from level import Level
from car import Car
from game_over import GameOver
from time import sleep

game_over = False

CAR_AMOUNT = 15

EXTRA_CARS = 2
ADD_MULTIPLIER = 0.1

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


def check_goal():
    if player.ycor() >= player.y_bound - player.height:
        level_up()


def level_up():
    print("Level Up!")

    level.increase_level(1)

    player.reset_player()

    for car in cars:
        car.reset_car()
        car.increase_multiplier(ADD_MULTIPLIER)

    for car in range(EXTRA_CARS):
        cars.append(Car())


# Setup Screen:
screen = Screen()
screen.tracer(0)
screen.title("Crossy Road")
screen.setup(SCREEN_WIDTH * 2, SCREEN_HEIGHT * 2)
screen.bgcolor("gray")

# Setup Objects:
player = Player()

level = Level()

cars = [Car() for car in range(CAR_AMOUNT)]

# Setup Listeners:
screen.listen()

screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

# Start Game:
while not game_over:
    sleep(0.05)

    check_goal()

    for car in cars:
        car.move()
        game_over = car.crashed_player(player)
        if game_over:
            GameOver()
            break

    screen.update()

screen.exitonclick()
