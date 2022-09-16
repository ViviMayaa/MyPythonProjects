from tkinter import *
import string
import random
from tkinter import messagebox
import json
import ast

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
    file_formatted = {}
    if password_entry.get() != "":
        file_formatted = {
            website_entry.get():
            {
                "email": email_entry.get(),
                "password": password_entry.get()

            }
        }
        # file = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n"
    else:
        file_formatted = {
            website_entry.get():
                {
                    "email": email_entry.get(),
                    "password": created_password

                }
        }

        # file = f"{website_entry.get()} | {email_entry.get()} | {created_password}\n"

    messagebox.showinfo(title="Save", message="Information saved.")

    # with open("list_passwords.txt", "a") as text:
    #     text.write(file)
    #     website_entry.delete(0, END)
    #     password_entry.delete(0, END)

    # Using Json
    # Reading old data to update and add more data later
    try:
        with open("list_passwords.json", "r") as text_read:
            data = json.load(text_read)
            #     Updating old with new data
            data.update(file_formatted)
    except FileNotFoundError:
        with open("list_passwords.json", "w") as text_write:
            json.dump(file_formatted, text_write, indent=4)
    # writing new file in
    else:
        with open("list_passwords.json", "w") as text_write:
            json.dump(data, text_write, indent=4)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# -----------------------------Search----------------------------------#

def search_data():
    try:
        with open("list_passwords.json", 'r') as text_read:
            # String to dict
            # text_dict = ast.literal_eval(text_read.read())

            # try:
            #     searched_data = text_dict[website_entry.get()]
            # except KeyError:
            #     messagebox.showinfo(title="Error", message="There is no website.")
            # finally:
            #     messagebox.showinfo(title="Data Found", message=f"Data found:\n "
            #                                                     f"Website: {website_entry.get()}\n"
            #                                                     f"Email: {searched_data['email']}\n"
            #                                                     f"Password: {searched_data['password']}")

            # Already reads as Dict
            text_dict = json.load(text_read)
            website = website_entry.get()
            if website in text_dict:
                messagebox.showinfo(title="Data Found", message=f"Data found:\n "
                                                                f"Website: {website}\n"
                                                                f"Email: {text_dict[website]['email']}\n"
                                                                f"Password: {text_dict[website]['password']}")
            else:
                messagebox.showinfo(title="Error", message=f"There is no data for {website}.")

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There is no file.")


    print(type(text_dict))

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

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)
password_entry.insert(END, created_password)


password_button = Button(text="Generate Password", command=generate_password, width= 15)
password_button.grid(column=3, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_buttom = Button(text="Search", width= 15, command=search_data)
search_buttom.grid(column=3, row=1, columnspan=3)

window.mainloop()
