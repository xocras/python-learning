from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self, screen_size):
        super().__init__("circle")
        self.FOOD_SIZE = 20
        self.SCORE_SIZE = 64

        self.penup()
        self.color("purple")

        self.x_bound = int(screen_size/2) - self.FOOD_SIZE
        self.y_bound = int(screen_size/2) - self.FOOD_SIZE
        self.offset = int(self.FOOD_SIZE/2)

        self.refresh()

    def refresh(self):
        self.setposition(
            randint(-self.x_bound, self.x_bound - self.offset),
            randint(-self.y_bound + self.offset, self.y_bound - self.SCORE_SIZE)
        )
