from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
X_COOR = 0
Y_COOR = 270


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(X_COOR, Y_COOR)
        self.my_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.my_score}",
            False,
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.my_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"GAME OVER",
            False,
            align=ALIGNMENT,
            font=FONT,
        )