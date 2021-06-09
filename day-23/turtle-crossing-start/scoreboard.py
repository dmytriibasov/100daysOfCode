from turtle import Turtle

FONT = ("Courier", 20, "normal")
SCORE_COORDINATES = (-220, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(SCORE_COORDINATES)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)