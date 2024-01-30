from turtle import Turtle


class State(Turtle):
    def __init__(self, state, x, y, ):
        super().__init__(visible=False)
        self.font_size = 16
        self.penup()
        self.setposition(x, y)
        self.color("black")
        self.write(state, False, "center", ('Courier', self.font_size, 'bold'))
