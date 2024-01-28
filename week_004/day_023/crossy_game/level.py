from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.margin = 4
        self.font_size = 16
        self.level = 0

        self.x_bound = 300
        self.y_bound = 300

        self.reset_level()

    def reset_level(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.setx(-self.x_bound * 3 / 4)
        self.sety(self.y_bound - self.font_size * 2 - self.margin)
        self.update_level()

    def set_bounds(self, x_bound, y_bound):
        self.x_bound = x_bound
        self.y_bound = y_bound
        self.reset_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", ('Courier', self.font_size, 'bold'))

    def increase_level(self, amount):
        self.level += amount
        self.update_level()
