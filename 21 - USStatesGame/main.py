import turtle

import pandas

screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
with open("50_states.csv") as states_csv_panda:
    states_csv = pandas.read_csv(states_csv_panda)
# getting coordenates on the image
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
game_is_on = True
score = 0
while game_is_on:
    screen.title(f'U.S. States Image {score}/{len(states_csv.state)}')
    answer_state = screen.textinput(title="Guess the State: ", prompt="What's another state's name?").title().strip()
    if [states_csv[states_csv.state == answer_state] != states_csv.empty]:
        correct_answer = states_csv[states_csv.state == answer_state]
        score += 1
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        text.goto(int(correct_answer.x), int(correct_answer.y))
        text.write(answer_state.title(), move=False, align="center", font=("Arial", 8, "normal"))
    if score == len(states_csv.state):
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        text.goto(0, 0)
        text.write("You've got them all, congrats!", move=False, align="center", font=("Arial", 18, "bold"))
        game_is_on = False
turtle.mainloop()



