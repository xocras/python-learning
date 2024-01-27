from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self, screen_size):
        super().__init__("circle")
        self.FOOD_SIZE = 20

        self.penup()
        self.color("purple")

        self.x_bound = screen_size - self.FOOD_SIZE * 2
        self.y_bound = screen_size - self.FOOD_SIZE * 2

        self.random_position()

    def random_position(self):
        self.setposition(
            randint(0, self.x_bound) - self.x_bound/2,
            randint(0, self.y_bound) - self.y_bound/2
        )
