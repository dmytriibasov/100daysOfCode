from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
SHAPE = "turtle"
COLOR = "cyan"


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.color(COLOR)
        self.setheading(90)
        self.set_start_position()

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def set_start_position(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):

        if self.ycor() > 280:
            return True
        return False