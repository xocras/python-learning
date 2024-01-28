from turtle import Turtle

SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.margin = 20
        self.x_bound = 400
        self.y_bound = 300
        self.color("white")
        self.penup()
        self.move()

    def set_margin(self, margin):
        self.margin = margin

    def set_x_bound(self, bound):
        self.x_bound = bound

    def set_y_bound(self, bound):
        self.y_bound = bound

    def move(self):
        self.setposition(
            self.xcor() + SPEED,
            self.ycor() + SPEED
        )
