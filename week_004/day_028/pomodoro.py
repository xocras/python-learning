from tkinter import Tk, Canvas, PhotoImage
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

BACKGROUND_WIDTH = 200
BACKGROUND_HEIGHT = 224

MARGIN = 24

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro")
window.minsize(BACKGROUND_WIDTH, BACKGROUND_HEIGHT)
window.config(padx=112, pady=48, bg=YELLOW)

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

canvas.create_text(
    BACKGROUND_WIDTH/2,
    BACKGROUND_HEIGHT/2 + MARGIN,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 32, "bold")
)

canvas.grid(column=2, row=2)

# Start
window.mainloop()
