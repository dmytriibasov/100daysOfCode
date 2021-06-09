from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score

import time

INITIAL_COORDINATES_RIGHT = (350, 0)
INITIAL_COORDINATES_LEFT = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Initialize an object
r_paddle = Paddle(INITIAL_COORDINATES_RIGHT)
l_paddle = Paddle(INITIAL_COORDINATES_LEFT)
ball = Ball()
score = Score()

screen.listen()
# right paddle button track
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

# left paddle button track
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# cyclic screen update
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
