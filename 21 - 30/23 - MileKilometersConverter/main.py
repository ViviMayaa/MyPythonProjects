from tkinter import *

window = Tk()
window.title("Mile to Kilometers")
window.minsize(width=300, height=200)

entry = Entry(fg='grey')
entry.config(font=('Arial', 10))
entry.grid(column=1, row=0)
entry.insert(END, '0')
entry.get()


miles_label = Label(text="Miles")
miles_label.config(font=('Arial', 10, 'bold'))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.config(font=("Arial", 10, 'bold'))
equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.config(font=("Arial", 10, 'bold'))
km_label.grid(column=2, row=1)

result_label = Label()
result_label.config(font=("Arial", 10, 'bold'))
result_label.grid(column=1, row=1)


def calculate():
    number_km = int(entry.get()) * 1.609344
    result_label.config(text=int(number_km))


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)


window.mainloop()
