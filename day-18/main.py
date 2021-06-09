import turtle as t
import random

colours = [
    "coral",
    "orange red",
    "lawn green",
    "teal",
    "light sky blue",
    "pale green",
    "blue",
    "red",
    "black",
    "purple",
    "cyan",
]

directions = [
    0,
    90,
    180,
    270,
]

# def draw_figure(object, side_length, number_of_sides):

#     try:
#         angle = 360 / number_of_sides

#     except:
#         ZeroDivisionError

#     for _ in range(number_of_sides):
#         object.right(angle)
#         object.fd(side_length)

t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")
timmy.pensize(1)
# timmy.shape("arrow")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


# timmy.shape("turtle")
# timmy.pensize(5)

# for _ in range(200):
#     timmy.pencolor(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#     timmy.color(random.choice(colours))


# side_length = 100

# for shape_side in range(11):
#     timmy.color(random.choice(colours))
#     draw_figure(timmy, side_length, shape_side)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.pencolor(random_color())
        timmy.circle(90)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()
