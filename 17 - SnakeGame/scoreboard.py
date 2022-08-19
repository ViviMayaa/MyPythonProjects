from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 14, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.setposition(0, 270)
        self.color("white")

    def adding_score(self):
        self.score += 1
        self.set_text()

    def set_text(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)
