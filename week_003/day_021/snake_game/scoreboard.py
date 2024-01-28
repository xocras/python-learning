from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen_size):
        super().__init__(visible=False)

        self.font_size = 24
        self.score = 0

        self.line = Turtle(visible=False)
        self.line.penup()
        self.line.color("white")
        self.line.setposition(
            -screen_size / 2 + self.font_size,
            screen_size/2 - self.font_size * 2 - 16
        )
        self.line.pendown()
        self.line.setx(screen_size / 2 - self.font_size - 16)

        self.penup()
        self.color("white")
        self.sety(screen_size/2 - self.font_size * 2)

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ('Arial', self.font_size, 'normal'))

    def increase_score(self, amount):
        self.score += amount
        self.update_score()
