from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.font_size = 48
        self.penup()
        self.sety(-self.font_size/2)
        self.color("black")
        self.write("GAME OVER", False, "center", ('Courier', self.font_size, 'normal'))
