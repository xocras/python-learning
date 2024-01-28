from turtle import Turtle

SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.margin = 20
        self.x_bound = 400
        self.y_bound = 300

        self.x_direction = 1
        self.y_direction = 1

        self.color("white")
        self.penup()
        self.move()

    def set_margin(self, margin):
        self.margin = margin

    def set_x_bound(self, bound):
        self.x_bound = bound

    def set_y_bound(self, bound):
        self.y_bound = bound

    def switch_x_direction(self):
        self.x_direction = 1 if self.x_direction == -1 else -1

    def switch_y_direction(self):
        self.y_direction = 1 if self.y_direction == -1 else -1

    def y_collision(self, y):
        return not -self.y_bound + self.margin <= y <= self.y_bound - self.margin

    def x_collision(self, x):
        return not -self.x_bound + self.margin <= x <= self.x_bound - self.margin

    def move(self):
        x = self.xcor() + SPEED * self.x_direction
        y = self.ycor() + SPEED * self.y_direction

        if self.y_collision(y):
            self.switch_y_direction()

        if self.x_collision(x):
            self.switch_x_direction()

        self.setposition(x, y)


