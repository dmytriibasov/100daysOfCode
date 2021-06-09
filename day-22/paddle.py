from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20
SHAPE = "square"
COLOR = "white"
WIDTH = 1
LENGTH = 5


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.turtlesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.speed("fastest")
        self.setheading(UP)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
