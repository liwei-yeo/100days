import tkinter
from tkinter import messagebox
import pyperclip
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
    , 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'
    , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password = []
    password.extend([letters[random.randrange(0, len(letters))] for letter in range(8, 10)])
    password.extend([symbols[random.randrange(0, len(symbols))] for symbol in range(2, 4)])
    password.extend([numbers[random.randrange(0, len(numbers))] for number in range(2, 4)])

    random.shuffle(password)
    string_pass = "".join(password)

    pyperclip.copy(string_pass)
    password_field.insert(index=0, string=string_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entries():
    website = website_field.get()
    email = email_field.get()
    password = password_field.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("./data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_field.delete(0, "end")
            password_field.delete(0, "end")
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=1)

# row 1
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
website_field = tkinter.Entry(width=52)
website_field.grid(column=1, row=1, columnspan=2, sticky="W")

# row 2
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_field = tkinter.Entry(width=52)
email_field.insert(index=0, string="default@email.com")
email_field.grid(column=1, row=2, columnspan=2)

# row 3
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)
password_field = tkinter.Entry(width=30)
password_field.grid(column=1, row=3, columnspan=1, sticky="W")
password_button = tkinter.Button(text="Generate Password", command=generate)
password_button.grid(column=2, row=3, sticky="EW")

# row 4
add_button = tkinter.Button(text="Add", command=save_entries, width=44)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
