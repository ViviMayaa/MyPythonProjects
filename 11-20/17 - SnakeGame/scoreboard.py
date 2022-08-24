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

    def highest_score_record(self):
        with open("highest_score.txt", "w") as archive:
            archive.write(str(self.score))

    def set_text(self):
        self.clear()
        with open("highest_score.txt", "r") as archive:
            highest_score = archive.read()
            self.write(f"Score: {self.score} Highest Score: {highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)
        with open("highest_score.txt", "r") as archive:
            highest_score = int(archive.read())
            if self.score > highest_score:
                self.setposition(0, -25)
                self.write(f"You beat the highest score, congratulations!",
                           move=False, align=ALIGNMENT, font=FONT)
                self.highest_score_record()
