from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen_size):
        super().__init__(visible=False)
        self.screen_size = screen_size
        self.font_size = 24
        self.score = 0

        self.setup_line()

        self.penup()
        self.color("white")
        self.sety(screen_size/2 - self.font_size * 2)

        self.update_score()

    def setup_line(self):
        line = Turtle(visible=False)
        line.penup()
        line.width(2)
        line.color("white")
        line.setposition(
            -self.screen_size / 2 + self.font_size,
            self.screen_size / 2 - self.font_size * 2 - 12
        )
        line.pendown()
        line.setx(self.screen_size / 2 - self.font_size - 16)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ('Courier', self.font_size, 'normal'))

    def increase_score(self, amount):
        self.score += amount
        self.update_score()
