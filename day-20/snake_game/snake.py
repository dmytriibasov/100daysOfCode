from turtle import Turtle

INITIAL_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIRECTION = {"right": 0, "up": 90, "left": 180, "down": 270}
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):

        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):

        for position in INITIAL_COORDINATES:
            self.add_segment(position)

    def add_segment(self, position, shape="turtle", color="white"):
        segment = Turtle(shape=shape)
        segment.color(color)
        segment.penup()
        segment.goto(position)
        self.snake_segments.append(segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != MOVE_DIRECTION["down"]:
            self.head.setheading(MOVE_DIRECTION["up"])

    def down(self):
        if self.head.heading() != MOVE_DIRECTION["up"]:
            self.head.setheading(MOVE_DIRECTION["down"])

    def left(self):
        if self.head.heading() != MOVE_DIRECTION["right"]:
            self.head.setheading(MOVE_DIRECTION["left"])

    def right(self):
        if self.head.heading() != MOVE_DIRECTION["left"]:
            self.head.setheading(MOVE_DIRECTION["right"])
