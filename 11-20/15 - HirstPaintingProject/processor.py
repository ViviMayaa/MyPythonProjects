import random

import colorgram
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
tim = Turtle()


# def extracting_color_image():
#     _extract = []
#     colors = colorgram.extract('image.jpg', 30)
#     for element in colors:
#         first_color = element
#         _extract.append(first_color.)
#     return _extract
# 
# 
#  = extracting_color_image()
rgb_list = [(235, 250, 241), (240, 230, 68), (182, 19, 42), (219, 238, 244), (187, 74, 36), (251, 230, 235),
            (18, 139, 86),(114, 180, 206), (25, 120, 166), (190, 179, 23), (218, 61, 97), (206, 164, 91),
            (27, 39, 74), (76, 173, 98), (176, 46, 64), (38, 44, 112), (238, 232, 3), (18, 164, 211), (216, 133, 155),
            (212, 72, 54), (126, 184, 127), (8, 55, 37), (12, 93, 55), (236, 157, 177), (165, 29, 26),
            (148, 209, 221), (8, 86, 109), (161, 210, 186), (234, 172, 164)]

# x = -250
angle_line = -380


def position_line(x):
    tim.penup()
    tim.setposition(-310, x)


def paiting_dots(rgb):

    # tim.color(random.choice(rgb))
    # tim.forward(1)
    tim.dot(50, random.choice(rgb))


def moving_dots():
    for _ in range(7):
        paiting_dots(rgb_list)
        tim.forward(100)

tim.hideturtle()
position_line(angle_line + 130)
moving_dots()
position_line(angle_line + (130 * 2))
moving_dots()
position_line(angle_line + (130 * 3))
moving_dots()
position_line(angle_line + (130 * 4))
moving_dots()
position_line(angle_line + (130 * 5))
moving_dots()


screen.exitonclick()