from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Moving the turtle ~~~~~~~~~~~~~~~~~~~~~~~~~~
def move_foward():
    tim.forward(50)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


def move_back():
    tim.backward(50)


def clear_drawing():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_foward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()