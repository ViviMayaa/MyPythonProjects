from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
tim.color('turquoise')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# square
# for _ in range(4):
#     tim.forward(200)
#     tim.right(90)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# dashed line
# for _ in range(8):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  increasing sides
# sides = 3
# tim.penup()
# tim.left(90)
# tim.forward(200)
# tim.right(90)
# tim.pendown()
# while sides != 11:
#     tim.color(random.random(), random.random(), random.random())
#     tries = 0
#     for i in range(sides):
#         angle = 360 / sides
#         tim.forward(100)
#         tim.right(angle)
#     sides += 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# random path taker
# def generating_random_number():
#     return random.randint(1, 4) * 90
#
#
# def generating_random_color():
#     rgb = []
#     for _ in range(3):
#         rgb.append(random.random())
#     rgb = tuple(rgb)
#     return rgb
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def random_move():
#     tim.pencolor(generating_random_color())
#     # tim.color(random.random(), random.random(), random.random())
#     tim.setheading(generating_random_number())
#     tim.forward(random.randrange(20, 50, 5))
#
#
# tim.pensize(10)
# tim.speed(10)
# for _ in range(50):
#     random_move()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# draw spirograph
# def circle():
#     for _ in range(72):
#         tim.forward(8)
#         tim.right(5)


tim.speed(10)
total_size = 360
while total_size > 0:
    tim.color('lightseagreen')
    # circle()
    tim.circle(100)
    tim.right(10)
    tim.color('mediumturquoise')
    # circle()
    tim.circle(100)
    tim.right(10)
    tim.color('paleturquoise')
    # circle()
    tim.circle(100)
    tim.right(10)
    total_size -= 30




screen = Screen()
screen.exitonclick()