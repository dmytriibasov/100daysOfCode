# from turtle import Turtle, Screen
# import time

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan2")

# timmy.forward(100)

# timmy.color("DarkCyan")

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column(
    "Pokemon Name",
    [
        "Pikachu",
        "Squirtle",
        "Charmander",
    ],
)
table.add_column(
    "Type",
    [
        "Electric",
        "Water",
        "Fire",
    ],
)
table.align = "l"

print(table)
