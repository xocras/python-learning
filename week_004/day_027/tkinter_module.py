import tkinter

# Notes:
# .pack() - Stacks elements
# .place() - Precise position
# .grid() - Column and Rows


def greet():
    print(text_input.get())


# Window
window = tkinter.Tk()
window.title("TKInter Widgets")
window.minsize(350, 300)
window.config(padx=48, pady=48)

# Label
label1 = tkinter.Label(text="Enter some text:", font=("Arial", 12))
label1.grid(column=2, row=0)

# Entry
text_input = tkinter.Entry()
text_input.grid(column=2, row=1)

# Label
label2 = tkinter.Label(text="Enter some text:", font=("Arial", 12))
label2.grid(column=2, row=2)

# Text
text_area = tkinter.Text(height=5, width=30)
text_area.focus()
text_area.insert(tkinter.END, "Example of a multi-line text entry.")
text_area.grid(column=2, row=4)

print(text_area.get("1.0", tkinter.END))

# Spinbox
spinbox = tkinter.Spinbox(from_=0, to=10, width=5)
spinbox.grid(column=2, row=3)

# Scale
scale = tkinter.Scale(from_=100, to=0)
scale.grid(column=3, row=4)

# Label
label3 = tkinter.Label(text="Select favorite language:", font=("Arial", 12))
label3.grid(column=2, row=5)

# Checkboxes
checkbox_state = tkinter.IntVar()
checkbox = tkinter.Checkbutton(text="Python", variable=checkbox_state)
checkbox.grid(column=2, row=6)

# Label
label3 = tkinter.Label(text="Select an option:", font=("Arial", 12))
label3.grid(column=2, row=7)

# Radio Button
radio_state = tkinter.IntVar()
radio_button1 = tkinter.Radiobutton(text="Option #1", value=1, variable=radio_state)
radio_button2 = tkinter.Radiobutton(text="Option #2", value=2, variable=radio_state)

radio_button1.grid(column=2, row=10)
radio_button2.grid(column=2, row=11)

# Listbox
listbox = tkinter.Listbox(height=4, justify="center")

for i, option in enumerate([f"Option {i + 1}" for i in range(10)]):
    listbox.insert(i, option)

listbox.bind("<<ListboxSelect>>", print)

listbox.grid(column=2, row=12)

# Button
button = tkinter.Button(text="Submit", command=greet)
button.grid(column=2, row=13)

window.mainloop()
