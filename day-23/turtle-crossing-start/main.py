import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# class init
player = Player()
car_manager = CarManager()
score = Scoreboard()

# listen
screen.listen()
screen.onkey(player.move, "Up")

# main loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.is_at_finish_line():
        score.increase_level()
        player.set_start_position()
        car_manager.increment_move_speed()

    # detect collision with a car
    for car in car_manager.car_list:

        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()