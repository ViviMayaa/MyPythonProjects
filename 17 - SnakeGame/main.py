from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
WALLS = 295
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(n=0)
snake = Snake()
food = Food()
score_board = ScoreBoard()
score_board.set_text()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        score_board.adding_score()
        food.refresh()
        snake.extend()

    # Detecting collision with wall
    if snake.head.xcor() > WALLS or snake.head.xcor() < -WALLS or \
            snake.head.ycor() > WALLS or snake.head.ycor() < -WALLS:
        game_is_on = False
        score_board.game_over()

    # Detecting collision with tail
    for turtles in snake.turtle_list[1:]:
        if snake.head.distance(turtles) < 10:
            game_is_on = False
            score_board.game_over()


screen.exitonclick()
