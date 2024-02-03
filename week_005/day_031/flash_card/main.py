import random

import pandas

from tkinter import Tk, Canvas, PhotoImage, Label, Button

BACKGROUND_WIDTH = 450
BACKGROUND_HEIGHT = 371
BACKGROUND_PADDING = 25
ICON_SIZE = 55

FONT_NAME = "Ariel"

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_COLOR = "#91C2AF"


# Functions
def next_round():
    global timer
    window.after_cancel(timer)
    timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_source)

    language_label.config(bg=CARD_BACK_COLOR, fg="white", text="English")
    word_label.config(bg=CARD_BACK_COLOR, fg="white", text=word["English"])


def next_card():
    global word
    word = random.choice(words)

    canvas.itemconfig(card_image, image=card_front_source)

    language_label.config(bg="white", fg="black", text="French")
    word_label.config(bg="white", fg="black", text=word["French"])

    next_round()


def add_score():
    global score
    score += 1
    update_words()
    next_card()


def update_words():
    words.remove(word)
    pandas.DataFrame(words).to_csv("./data/words_to_learn.csv", index=False)


# Score
score = 0

# Load Words
try:
    words = pandas.read_csv("./data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    words = pandas.read_csv("./data/french_words.csv").to_dict(orient="records")
print(len(words))
word = random.choice(words)

# Window
window = Tk()
window.title("Flash Cards")
window.geometry(f"{BACKGROUND_WIDTH}x{BACKGROUND_HEIGHT}")
window.config(padx=BACKGROUND_PADDING, pady=BACKGROUND_PADDING, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(
    width=BACKGROUND_WIDTH - BACKGROUND_PADDING * 2,
    height=BACKGROUND_HEIGHT - BACKGROUND_PADDING * 2 - ICON_SIZE
)

canvas.config(highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR)

# Images
card_front_source = PhotoImage(file="images/card_front.png").subsample(2, 2)
card_back_source = PhotoImage(file="images/card_back.png").subsample(2, 2)
correct_source = PhotoImage(file="images/right.png").subsample(2, 2)
incorrect_source = PhotoImage(file="images/wrong.png").subsample(2, 2)

card_image = canvas.create_image(
    BACKGROUND_WIDTH / 2 - BACKGROUND_PADDING,
    BACKGROUND_HEIGHT / 2 - BACKGROUND_PADDING - ICON_SIZE / 2,
    image=card_front_source
)

canvas.grid(column=0, row=0, columnspan=2)

#  Buttons
correct_button = Button(image=correct_source)
incorrect_button = Button(image=incorrect_source)

correct_button.config(highlightthickness=0, borderwidth=0, command=add_score)
incorrect_button.config(highlightthickness=0, borderwidth=0, command=next_card)

correct_button.grid(column=1, row=1)
incorrect_button.grid(column=0, row=1)

# Labels
language_label = Label(text="French", font=(FONT_NAME, 20, "italic"), bg="white")
word_label = Label(text=f"{word["French"]}", font=(FONT_NAME, 30, "bold"), bg="white")

language_label.grid(column=0, row=0, columnspan=2, pady=(0, 128))
word_label.grid(column=0, row=0, columnspan=2, pady=(8, 0))

# Game
timer = window.after(3000, flip_card)

# Start
window.mainloop()
