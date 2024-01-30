import tkinter

# Window
window = tkinter.Tk()
window.title("Hello World!")
window.minsize(500, 300)

# Label
description = tkinter.Label(text="This is a GUI", font=("Arial", 16))
description.pack(expand=True)

window.mainloop()
