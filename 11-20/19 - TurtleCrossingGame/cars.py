from turtle import Turtle
import random


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.setheading(180)
        self.shapesize(1, 2)
        self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.goto(random.randint(300, 400), random.randint(-250, 280))

    def car_moving(self, moving_speed_max):
        self.forward(random.randint(moving_speed_max - 3, moving_speed_max))
