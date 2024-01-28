from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, direction=1):
        super().__init__()
        self.margin = 24
        self.font_size = 80
        self.score = 0
        self.direction = direction

        self.x_bound = 400
        self.y_bound = 300

        self.reset_score()

    def reset_score(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setx(self.x_bound / 2 * self.direction)
        self.sety(self.y_bound - self.font_size * 2 - self.margin)
        self.update_score()

    def set_direction(self, direction):
        self.direction = direction
        self.set_bounds(self.x_bound, self.y_bound)

    def set_bounds(self, x_bound, y_bound):
        self.x_bound = x_bound * self.direction
        self.y_bound = y_bound
        self.reset_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", False, "center", ('Courier', self.font_size, 'normal'))

    def increase_points(self, amount):
        self.score += amount
        self.update_score()
