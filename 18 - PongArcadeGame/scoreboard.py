from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 14, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')

    def score_layout(self, position, score):
        self.goto(position)
        self.write(f"Score: {score}", move=False, align=ALIGNMENT, font=FONT)

    def build_middle_line(self):
        self.color('white')
        self.goto(00, -500)
        self.setheading(90)
        for _ in range(0, 25):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.goto(-800, 225)
        self.setheading(0)
        for _ in range(0, 50):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
