from tkinter import Tk, Canvas, PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

BACKGROUND_WIDTH = 280
BACKGROUND_HEIGHT = 240

MARGIN = 24

# ---------------------------- TIMER RESET ------------------------------- #
reset = False


def reset_timer():
    global reset
    reset = True

    count_down(0, work=False, breaks=0)
    update_checkmark(0)
    title.config(text="Pomodoro!", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    reset_timer()

    global reset
    reset = False

    update_checkmark(0)
    title.config(text="Working", fg=GREEN)
    count_down(WORK_MIN * 60, work=True, breaks=0)


def update_checkmark(amount):

    if amount:
        checkmarks.config(text=checkmarks.cget('text') + "✔")
    else:
        checkmarks.config(text="")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, work, breaks):

    # Reset Timer
    if count and reset:
        return

    # Start Short Break
    elif count <= 0 and work and breaks < 3:
        update_checkmark(1)

        title.config(text="Break", fg=PINK)
        window.after(1000, count_down, SHORT_BREAK_MIN * 60, False, breaks + 1)

    # Start Long Break
    elif count <= 0 and work:
        update_checkmark(1)

        title.config(text="Long Break", fg=RED)
        window.after(1000, count_down, LONG_BREAK_MIN * 60, False, 0)

    # Start Working
    elif count <= 0 and not work:

        if not breaks:
            update_checkmark(0)

        title.config(text="Working", fg=GREEN)
        count_down(WORK_MIN * 60, work=True, breaks=breaks)

    # Continue Timer
    else:
        window.after(1000, count_down, count - 1, work, breaks)

    # Update Display
    minutes, seconds = divmod(count, 60)

    canvas.itemconfig(timer, text=f"{minutes:02d}:{seconds:02d}")


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro!")
window.minsize(BACKGROUND_WIDTH, BACKGROUND_HEIGHT)
window.config(padx=80, pady=8, bg=YELLOW)


# Image
background_image = PhotoImage(file="tomato.png")

# Canvas
canvas = Canvas(width=BACKGROUND_WIDTH, height=BACKGROUND_HEIGHT, bg=YELLOW)
canvas.config(highlightthickness=0, borderwidth=0)

canvas.create_image(
    BACKGROUND_WIDTH/2,
    BACKGROUND_HEIGHT/2,
    image=background_image
)

timer = canvas.create_text(
    BACKGROUND_WIDTH/2,
    BACKGROUND_HEIGHT/2 + MARGIN,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 32, "bold")
)

canvas.grid(column=2, row=2, pady=8)

# Title

title = Label(
    text="Pomodoro!",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 32, "bold")
)

title.grid(column=2, row=0, pady=(32, 16))

# Start Button

start_button = Button(
    text="Start",
    font=(FONT_NAME, 16, "bold"),
    command=start_timer
)

start_button.grid(column=1, row=3, pady=(32, 64))

# Reset Button

reset_button = Button(
    text="Reset",
    font=(FONT_NAME, 16, "bold"),
    command=reset_timer
)

reset_button.grid(column=3, row=3, pady=(32, 64))

# Checkmarks

checkmarks = Label(
    text="",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 16, "bold")
)

checkmarks.grid(column=2, row=3, pady=(32, 64))

# Start

window.mainloop()
