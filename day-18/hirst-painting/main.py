import colorgram
import random
import turtle as t

# colors = colorgram.extract(
#     r"C:\Users\Dmytrii Basov\Desktop\Python\Study materials\Udemy_projects\day-18\hirst-painting\dot_image.jpg",
#     30,
# )

# rgb_colors = []

# for color in colors:

#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
t.colormode(255)
timmy = t.Turtle()


colors_list = [
    (201, 164, 112),
    (239, 246, 241),
    (152, 75, 50),
    (221, 201, 138),
    (57, 95, 126),
    (170, 152, 44),
    (138, 31, 20),
    (135, 163, 183),
    (196, 94, 75),
    (49, 121, 88),
    (143, 177, 149),
    (95, 75, 77),
    (76, 39, 32),
    (164, 146, 157),
    (16, 98, 71),
    (232, 176, 165),
    (54, 46, 48),
    (32, 61, 76),
    (22, 83, 89),
    (182, 204, 176),
    (141, 22, 25),
    (86, 147, 127),
    (45, 66, 85),
    (8, 68, 53),
    (177, 94, 97),
    (222, 177, 182),
    (109, 128, 151),
]

dot_color = random.choice(colors_list)
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
init_x = -250
init_y = -200
x, y = init_x, init_y
timmy.setpos(x, y)

for i in range(1, 11):

    for j in range(1, 11):

        timmy.dot(20, random.choice(colors_list))
        timmy.setpos(x, y)
        x += 50

        if i == j == 10:
            timmy.dot(20, random.choice(colors_list))

    x = init_x
    y += 50

timmy.home()

screen = t.Screen()
screen.exitonclick()