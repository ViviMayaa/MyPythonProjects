from tkinter import *
import string
import random
from tkinter import messagebox

created_password = ''
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    global created_password
    created_password = ''
    password_entry.delete(0, END)
    for _ in range(10, 20):
        lottery = random.randint(0, 3)
        if lottery == 0:
            created_password += random.choice(string.ascii_uppercase)
        elif lottery == 1:
            created_password += random.choice(string.ascii_lowercase)
        elif lottery == 2:
            created_password += random.choice(string.punctuation)
        elif lottery == 3:
            created_password += random.choice(string.digits)
    password_entry.insert(END, created_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if password_entry.get() != "":
        file = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n"
    else:
        file = f"{website_entry.get()} | {email_entry.get()} | {created_password}\n"

    messagebox.showinfo(title="Save", message="Information saved.")

    with open("list_passwords.txt", "w") as text:
        text.write(file)
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=('Arial', 12))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ", font=('Arial', 12))
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ", font=('Arial', 12))
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(END, "angela@email.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)
password_entry.insert(END, created_password)


password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
