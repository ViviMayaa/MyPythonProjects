from turtle import Turtle


class Playerturtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('blue')
        self.setheading(90)
        self.goto(00, -280)
        self.color('black')

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(15)


