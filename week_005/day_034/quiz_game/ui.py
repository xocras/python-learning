from tkinter import Tk, Label, Canvas, PhotoImage, Button
from quiz_brain import QuizBrain

FONT_NAME = "Arial"
THEME_COLOR = "#375362"

PADDING = 20
CARD_WIDTH = 300
CARD_HEIGHT = 250
UI_WIDTH = CARD_WIDTH + PADDING * 2
UI_HEIGHT = 420 + PADDING * 2

GRID = {'ROWS': 3, 'COLUMNS': 2}


class QuizInterface:
    def __init__(self, brain: QuizBrain):
        # Properties
        self.brain = brain
        self.feedback = False

        # Window
        self.window = Tk()

        self.window.geometry(f"{UI_WIDTH}x{UI_HEIGHT}")

        self.window.config(
            padx=PADDING,
            pady=PADDING,
            bg=THEME_COLOR
        )

        for i in range(GRID['COLUMNS']):
            self.window.columnconfigure(i, weight=1)

        for i in range(GRID['ROWS']):
            self.window.rowconfigure(i, weight=1)

        self.window.title("Trivia API")

        # Score
        self.score_label = Label(
            text=f"Score: {self.brain.score}",
            font=(FONT_NAME, 12, "bold"),
            bg=THEME_COLOR,
            fg="white"
        )

        self.score_label.grid(column=1, row=0, sticky="nsew")

        # Canvas
        self.canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT)

        self.canvas.config(highlightthickness=0, borderwidth=0, bg="white")

        self.canvas.grid(column=0, row=1, columnspan=2, sticky="nsew", pady=PADDING)

        # Question
        self.question_label = Label(
            text="Question",
            width=CARD_WIDTH - PADDING * 2,
            wraplength=CARD_WIDTH - PADDING * 2,
            font=(FONT_NAME, 16, "italic"),
            bg="white"
        )

        self.update_question()

        self.question_label.grid(column=0, row=1, columnspan=2, sticky="nsew", padx=PADDING, pady=PADDING)

        # Images
        true_source = PhotoImage(file="images/true.png")
        false_source = PhotoImage(file="images/false.png")

        # Buttons
        self.true_button = Button(image=true_source)
        self.false_button = Button(image=false_source)

        self.true_button.config(
            highlightthickness=0,
            borderwidth=0,
            command=self.mark_true,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR
        )

        self.false_button.config(
            highlightthickness=0,
            borderwidth=0,
            command=self.mark_false,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR
        )

        self.true_button.grid(column=0, row=2, sticky="nsew")
        self.false_button.grid(column=1, row=2, sticky="nsew")

        # Start
        self.window.mainloop()

    def update_ui(self):
        self.update_question()
        self.update_score()

    def display_feedback(self, color: str):
        self.feedback = True
        self.canvas.config(bg=color)
        self.question_label.config(bg=color, fg="white")
        self.window.after(1500, self.remove_feedback)

    def remove_feedback(self):
        self.canvas.config(bg="white")
        self.question_label.config(bg="white", fg="black")
        self.update_ui()
        self.feedback = False

    def update_question(self):
        self.question_label.config(text=self.brain.next_question())

    def update_score(self):
        self.score_label.config(text=f"Score: {self.brain.score}")

    def mark_true(self):
        self.check_answer('True')

    def mark_false(self):
        self.check_answer('False')

    def check_answer(self, answer):
        if self.feedback:
            return

        if self.brain.question_index == len(self.brain.question_list):
            print("\nYou've reached the end. There are no more questions.")
            return

        if self.brain.check_answer(answer):
            self.display_feedback('green')
        else:
            self.display_feedback('red')
