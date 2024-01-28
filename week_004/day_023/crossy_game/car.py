from turtle import Turtle
from random import random, randint


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.x_bound = 300
        self.y_bound = 240

        self.x_direction = 0
        self.y_position = 0
        self.multiplier = 1
        self.speed = 0

        self.speed_min = 5
        self.speed_max = 10

        self.height = 20
        self.width = 40
        self.default = 20

        self.reset_car()

    def increase_multiplier(self, amount):
        self.multiplier += amount

    def set_x_bound(self, bound):
        self.x_bound = bound

    def set_y_bound(self, bound):
        self.y_bound = bound

    def reset_y(self):
        self.y_position = randint(0, self.y_bound) * random_direction()
        self.sety(self.y_position)

    def reset_x_direction(self):
        self.x_direction = random_direction()

    def reset_speed(self):
        self.speed = randint(self.speed_min, self.speed_max)

    def reset_car(self):
        self.reset()
        self.penup()
        self.shape("square")
        self.turtlesize(
            self.height / self.default,
            self.width / self.default
        )
        self.setx((self.x_bound + self.width / 2) * self.x_direction)
        self.reset_y()
        self.reset_speed()
        self.reset_color()
        self.reset_x_direction()

    def reset_color(self):
        self.color((
            random(),
            random(),
            random()
        ))

    def move(self):
        x = self.xcor() + self.speed * self.x_direction * self.multiplier

        if self.x_direction < 0 and x + self.width/2 < -self.x_bound:
            self.reset_car()
            return

        if self.x_direction > 0 and x - self.width/2 > self.x_bound:
            self.reset_car()
            return

        self.setx(x)

    def crashed_player(self, player):
        return self.distance(player) <= (self.height + player.height) / 2


def random_direction():
    return 1 if randint(0, 1) else -1
