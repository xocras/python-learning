from turtle import Turtle
from random import randint

NORTH = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.speed = 10
        self.direction = 5 if randint(0, 1) else -5

        self.height = 20
        self.width = 20

        self.y_bound = 300

        self.reset_player()

    def reset_player(self):
        self.reset()
        self.penup()
        self.setheading(NORTH)
        self.shape("turtle")
        self.color("black")
        self.sety(-self.y_bound + self.height)

    def set_name(self, name):
        self.name = name

    def set_y_bound(self, bound):
        self.y_bound = bound

    def step_forward(self):
        self.direction = 5 if self.direction < 0 else -5

    def move_up(self):
        y = self.ycor() + self.speed

        if y < self.y_bound - self.height / 2:
            self.step_forward()
            self.setheading(NORTH + self.direction)
            self.sety(y)

    def move_down(self):
        y = self.ycor() - self.speed

        if y > -self.y_bound + self.height/2:
            self.step_forward()
            self.setheading(NORTH + self.direction)
            self.sety(y)
