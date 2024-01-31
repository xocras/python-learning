import tkinter


def greet():
    description["text"] = text_input.get()


# Window
window = tkinter.Tk()
window.title("TKInter Widgets")
window.minsize(300, 100)

# Label
description = tkinter.Label(text="Hello World!", font=("Arial", 16))
description.pack()

# Entry
text_input = tkinter.Entry()
text_input.pack()

# Text
text_area = tkinter.Text(height=5, width=30)
text_area.focus()
text_area.insert(tkinter.END, "Example of a multi-line text entry.")
text_area.pack()

print(text_area.get("1.0", tkinter.END))

# Spinbox
spinbox = tkinter.Spinbox(from_=0, to=10, width=5)
spinbox.pack()

# Scale
scale = tkinter.Scale(from_=100, to=0)
scale.pack()

# Checkboxes
checkbox_state = tkinter.IntVar()
checkbox = tkinter.Checkbutton(text="Python", variable=checkbox_state)
checkbox.pack()

# Radio Button
radio_state = tkinter.IntVar()
radio_button1 = tkinter.Radiobutton(text="Option #1", value=1, variable=radio_state)
radio_button2 = tkinter.Radiobutton(text="Option #2", value=2, variable=radio_state)

radio_button1.pack()
radio_button2.pack()

# Listbox
listbox = tkinter.Listbox(height=4, justify="center")

for i, option in enumerate([f"Option {i + 1}" for i in range(10)]):
    listbox.insert(i, option)

listbox.bind("<<ListboxSelect>>", print)

listbox.pack()

# Button
button = tkinter.Button(text="Submit", command=greet)
button.pack()

window.mainloop()
