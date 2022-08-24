from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 18, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def game_over(self):
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def score_board(self, level):
        self.clear()
        self.goto(-225, 250)
        self.write(f"Level: {level}", move=False, align=ALIGNMENT, font=FONT)
