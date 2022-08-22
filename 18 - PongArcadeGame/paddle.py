from turtle import Turtle

SIZE = (5, 1)


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shapesize(SIZE[0], SIZE[1])
        self.color('white')
        self.shape("square")
        self.position = position
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 25
        self.goto(self.position[0], new_y)

    def down(self):
        new_y = self.ycor() - 25
        self.goto(self.position[0], new_y)
