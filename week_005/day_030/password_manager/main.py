import json

import pyperclip

from tkinter import Tk, Canvas, PhotoImage, Label, Button, Entry, messagebox

from password_generator import generate_password

BACKGROUND_WIDTH = 600
BACKGROUND_HEIGHT = 400
BACKGROUND_PADDING = 32

IMAGE_WIDTH = 200
IMAGE_HEIGHT = 200

FONT_NAME = "Arial"


# Functions
def save():
    # Fetch Inputs
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    #  Build JSON
    entry = {
        website: {
            "user": username,
            "password": password
        }
    }

    # Check Inputs
    if not website or not username or not password:
        messagebox.showinfo(
            "Error",
            "Missing information.\n\n" +
            "Please review and fill all the fields."
        )
        return

    # User Confirmation
    confirmation = messagebox.askyesno(
        "Confirmation",
        f"Are you sure you want this password to be added?\n\n" +
        f"Website: {website}\n\n" +
        f"User: {username}\n\n" +
        f"Password: {password}"
    )

    if not confirmation:
        return

    # Read Passwords
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            data.update(entry)
    except FileNotFoundError:
        data = entry

    # Save Passwords
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

    # Clear Inputs
    website_input.delete(0, 'end')
    password_input.delete(0, 'end')


def random_password():
    password = generate_password(8, 4, 4)
    password_input.delete(0, 'end')
    password_input.insert(0, password)

    pyperclip.copy(password)


# Window
window = Tk()
window.title("Password Manager")
window.geometry(f"{BACKGROUND_WIDTH}x{BACKGROUND_HEIGHT}")
window.config(padx=BACKGROUND_PADDING, pady=BACKGROUND_PADDING)

# Image
logo_image = PhotoImage(file="logo.png")

# Canvas
canvas = Canvas(
    width=BACKGROUND_WIDTH - BACKGROUND_PADDING * 2,
    height=IMAGE_HEIGHT - BACKGROUND_PADDING
)

canvas.config(highlightthickness=0, borderwidth=0)

canvas.create_image(
    BACKGROUND_WIDTH/2 - BACKGROUND_PADDING,
    (IMAGE_HEIGHT - BACKGROUND_PADDING)/2,
    image=logo_image
)

canvas.grid(column=0, row=0, columnspan=3)

# Labels
website_label = Label(text="Website: ", font=(FONT_NAME, 12))
username_label = Label(text="Email/Username: ", font=(FONT_NAME, 12))
password_label = Label(text="Password: ", font=(FONT_NAME, 12))

website_label.grid(column=0, row=1, pady=(8, 4))
username_label.grid(column=0, row=2, pady=(4, 4))
password_label.grid(column=0, row=3, pady=(4, 8))

# Inputs
website_input = Entry(width=64)
username_input = Entry(width=64)
password_input = Entry(width=32)

website_input.grid(column=1, row=1, columnspan=2, ipady=4, pady=(8, 4))
username_input.grid(column=1, row=2, columnspan=2, ipady=4, pady=(4, 4))
password_input.grid(column=1, row=3, ipady=5, pady=(4, 8))

username_input.insert(0, "oscar.cruz@mail.com")

website_input.focus()

# Button
generate_password_button = Button(text="Generate Password", font=(FONT_NAME, 12), width=19, command=random_password)
add_button = Button(text="Add", font=(FONT_NAME, 12), width=42, command=save)

generate_password_button.grid(column=2, row=3, pady=(4, 8))
add_button.grid(column=1, row=4, columnspan=2)

# Start
window.mainloop()
