import random
import turtle
from turtle import Turtle, Screen

red_turtle = Turtle()
green_turtle = Turtle()
purple_turtle = Turtle()
yellow_turtle = Turtle()
blue_turtle = Turtle()
tim_worker = Turtle()

red_turtle.shape("turtle")
green_turtle.shape("turtle")
purple_turtle.shape("turtle")
yellow_turtle.shape("turtle")
blue_turtle.shape("turtle")

red_turtle.color('red')
green_turtle.color('green')
purple_turtle.color('purple')
yellow_turtle.color('yellow')
blue_turtle.color('blue')

screen = Screen()
screen.setup(width=800, height=500)
angle_line = -240


def position_line(x, turtle):
    turtle.penup()
    turtle.setposition(-310, x)


def start_position():
    position_line(angle_line + 80, red_turtle)
    position_line(angle_line + (80 * 2), green_turtle)
    position_line(angle_line + (80 * 3), purple_turtle)
    position_line(angle_line + (80 * 4), yellow_turtle)
    position_line(angle_line + (80 * 5), blue_turtle)


def move_forward(turt):
    turt.forward(random.randint(1, 5))


def random_speed():
    move_forward(red_turtle)
    move_forward(green_turtle)
    move_forward(purple_turtle)
    move_forward(yellow_turtle)
    move_forward(blue_turtle)


def who_won():
    winner = ''
    if int(red_turtle.xcor()) >= 300:
        print("Red Turtle won! ")
        winner = 'Red'
        return False, winner
    if int(green_turtle.xcor()) >= 300:
        print("Green Turtle won! ")
        winner = 'Green'
        return False, winner
    if int(purple_turtle.xcor()) >= 300:
        print("Purple Turtle won! ")
        winner = 'Purple'
        return False, winner
    if int(yellow_turtle.xcor()) >= 300:
        print("Yellow Turtle won! ")
        winner = 'Yellow'
        return False, winner
    if int(blue_turtle.xcor()) >= 300:
        winner = 'Blue'
        print("Blue Turtle won! ")
        return False, winner
    return True, winner


def building_stage():
    tim_worker.hideturtle()
    tim_worker.speed('fastest')
    tim_worker.penup()
    tim_worker.forward(310)
    tim_worker.right(90)
    tim_worker.forward(200)
    tim_worker.left(180)
    tim_worker.pendown()
    tim_worker.pensize(2)
    tim_worker.forward(400)


def play_race():
    building_stage()
    start_position()
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

    running = True
    x = - 307
    x_comparison = x
    while running:
        random_speed()
        x = red_turtle.xcor()
        if x >= x_comparison + 10:
            x_comparison = x
            random_speed()
        data = who_won()
        running = data[0]
        winner = data[1]
    if winner == user_bet.title():
        print(f"Congrats, your {user_bet.title()} turtle won! ")
    else:
        print(f"Your {user_bet.title()} Turtle lost! ")


play_race()
screen.exitonclick()