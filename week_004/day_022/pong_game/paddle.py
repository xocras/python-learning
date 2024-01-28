from turtle import Turtle

SPEED = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__("square")
        self.name = ""

        self.height = 100
        self.width = 20
        self.default = 20

        self.y_bound = 300
        self.color("white")

        self.turtlesize(
            self.height/self.default,
            self.width/self.default
        )

        self.penup()
        self.setx(position)

    def set_name(self, name):
        self.name = name

    def set_y_bound(self, bound):
        self.y_bound = bound

    def move_up(self):
        y = self.ycor() + SPEED

        if y <= self.y_bound - self.height / 2:
            self.sety(y)

    def move_down(self):
        y = self.ycor() - SPEED

        if y >= -self.y_bound + self.height/2:
            self.sety(y)
