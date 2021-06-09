from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SHAPE = "square"
WIDTH = 1
LENGTH = 2
X_COOR = 300


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.move_speed)

    def increment_move_speed(self):
        self.move_speed += MOVE_INCREMENT

    def create_car(self, shape=SHAPE):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape=shape)
            car.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
            car.penup()
            car.color(random.choice(COLORS))
            car.speed("fastest")
            random_y = random.randint(-250, 250)
            car.setposition(X_COOR, random_y)
            self.car_list.append(car)
