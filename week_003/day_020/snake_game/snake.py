from turtle import Turtle

NORTH, SOUTH = 90, 270
WEST, EAST = 180, 0


class Snake:
    def __init__(self, screen):
        self.SEGMENT_SIZE = 20
        self.STARTING_LENGTH = 3

        self.segments = []
        self.screen = screen

        self.add_segments(self.STARTING_LENGTH)
        self.head = self.segments[0]

    def position_segments(self):
        length = len(self.segments)

        if not length > 0:
            return 0

        x_position = self.segments[length - 1].xcor() - self.SEGMENT_SIZE

        return x_position

    def add_segments(self, amount):
        for n in range(amount):
            snake_segments = Turtle("square")
            snake_segments.color("white")
            snake_segments.penup()
            snake_segments.setx(self.position_segments())
            self.segments.append(snake_segments)

        self.screen.update()

    def move_tail(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()

            self.segments[index].setposition((x, y))

    def turn_east(self):
        if self.head.heading() == WEST:
            return

        self.head.setheading(EAST)
        self.move()

    def turn_west(self):
        if self.head.heading() == EAST:
            return

        self.head.setheading(WEST)
        self.move()

    def turn_south(self):
        if self.head.heading() == NORTH:
            return

        self.head.setheading(SOUTH)
        self.move()

    def turn_north(self):
        if self.head.heading() == SOUTH:
            return

        self.head.setheading(NORTH)
        self.move()

    def move(self):
        self.move_tail()
        self.head.forward(self.SEGMENT_SIZE)
        self.screen.update()
