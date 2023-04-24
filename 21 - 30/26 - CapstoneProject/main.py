from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
one_french_english = []

window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, pady=50, padx=50)


# ~~~~~~~~~~~~~~Reading list of words~~~~~~~~~~~~
try:
    with open("data/french_words.csv") as words:
        french_english = []
        for element in words:
            french_english += [list(element.split(','))]
        french_english.remove(french_english[0])
except FileNotFoundError:
    raise FileNotFoundError('File has not been found, try again with other name or file.')


def new_word():
    return random.choice(french_english)


def new_card():
    global one_french_english, flip_timer
    window.after_cancel(flip_timer)
    one_french_english = new_word()
    canvas.itemconfig(canvas_background, image=card_front)
    canvas.itemconfig(canvas_words, fill='black', text=one_french_english[0])
    canvas.itemconfig(canvas_title, fill='black', text="French")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global one_french_english
    canvas.itemconfig(canvas_background, image=card_back)
    canvas.itemconfig(canvas_words, fill='white', text=str(one_french_english[1]).strip())
    canvas.itemconfig(canvas_title, fill='white', text="English")


def card_is_known():
    global one_french_english
    french_english.remove(one_french_english)
    new_card()


flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0 )
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=card_front)
canvas_words = canvas.create_text(400, 263, text='', font=("Arial", 60, "bold"))
canvas_title = canvas.create_text(400, 150, text="", font=("Arial", 40, 'italic'))
canvas.grid(column=0, row=0, columnspan=2)


image_yes = PhotoImage(file="images/right.png")
button_yes = Button(image=image_yes, bg=BACKGROUND_COLOR, highlightthickness=0, command=card_is_known)
button_yes.grid(column=1, row=1)

image_no = PhotoImage(file="images/wrong.png")
button_no = Button(image=image_no, bg=BACKGROUND_COLOR, highlightthickness=0, command=new_card)
button_no.grid(column=0, row=1)


new_card()

window.mainloop()
