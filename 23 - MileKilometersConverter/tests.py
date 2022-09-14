# import tkinter
# tkinter.Tk() will become Tk()
from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
# Padding
window.config(padx=10, pady=10)

# Label

my_label = Label(text="Trying this for the first time", font=("Arial", 15, "bold"))
# my_label.pack(side="bottom")
# my_label.pack(expand=True)
# my_label.place(x=0,y=0)
my_label.grid(column=0, row=0)
my_label['text'] = "New label"
my_label.config(text="New new label")

# Button

def button_clicked():
    answer = input.get()
    my_label.config(text=answer)


button = Button(text="Click here!", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=2)

# Entry // input

input = Entry(width=10)
input.grid(column=3, row=3)




window.mainloop()