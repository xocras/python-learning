

from tkinter import Tk, Canvas, PhotoImage, Label, Button, Entry, messagebox

BACKGROUND_WIDTH = 450
BACKGROUND_HEIGHT = 371
BACKGROUND_PADDING = 25
ICON_SIZE = 55

FONT_NAME = "Ariel"

BACKGROUND_COLOR = "#B1DDC6"

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

correct_button.config(highlightthickness=0, borderwidth=0)
incorrect_button.config(highlightthickness=0, borderwidth=0)

correct_button.grid(column=1, row=1)
incorrect_button.grid(column=0, row=1)

# Labels
language_label = Label(text="French", font=(FONT_NAME, 20, "italic"), bg="white")
word_label = Label(text="omelette", font=(FONT_NAME, 30, "bold"), bg="white")

language_label.grid(column=0, row=0, columnspan=2, pady=(0, 152))
word_label.grid(column=0, row=0, columnspan=2)

# Start
window.mainloop()
