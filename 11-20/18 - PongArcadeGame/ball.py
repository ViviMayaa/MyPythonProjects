from turtle import Turtle
import time
from scoreboard import Scoreboard


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape("circle")
        self.setposition(0, 0)
        self.speed_x = -10
        self.speed_y = 10
        self.right_score = 0
        self.left_score = 0

    def ball_move(self):
        new_x = self.xcor() + self.speed_x
        new_y = self.ycor() + self.speed_y
        # Detecting collision with wall
        if new_y >= 280 or new_y <= -280:
            self.speed_y *= -1
        self.goto(new_x, new_y)
    # 350, 40

    def touch_paddle(self, position):
        right_score_layout = Scoreboard()
        left_score_layout = Scoreboard()
        right_score_layout.score_layout((-200, 250), self.right_score)
        left_score_layout.score_layout((200, 250), self.left_score)

        if self.distance(position) < 50 and self.xcor() > 320 or self.distance(position) < 50 and self.xcor() < -320:
            self.speed_y *= - 1
            self.speed_x *= - 1
        elif self.xcor() > 390:
            self.reset_ball()
            self.right_score += 1
        elif self.xcor() < -390:
            self.reset_ball()
            self.left_score += 1

        right_score_layout.clear()
        left_score_layout.clear()

    def reset_ball(self):
        self.goto(0, 0)
        time.sleep(0.5)
        self.speed_x *= - 1
