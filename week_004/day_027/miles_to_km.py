import tkinter


def miles_to_km():
    km_output["text"] = "{:,.2f}".format(float(miles_input.get()) * 1.6)


# Window
window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(100, 100)
window.config(padx=8, pady=16)

# Miles Input
miles_input = tkinter.Entry()
miles_input.grid(column=1, row=0)

# Miles Label
miles_label = tkinter.Label(text="Miles", font=("Arial", 10))
miles_label.config(padx=16, pady=8)
miles_label.grid(column=2, row=0)

# Km Output
km_output = tkinter.Label(text="0", font=("Arial", 10))
km_output.config(padx=8, pady=8)
km_output.grid(column=1, row=1)

# Km Label
km_label = tkinter.Label(text="Km", font=("Arial", 10))
km_label.config(padx=16, pady=8)
km_label.grid(column=2, row=1)

# Description
description_label = tkinter.Label(text="Is equal to: ", font=("Arial", 10))
description_label.config(padx=8, pady=8)
description_label.grid(column=0, row=1)

# Calculate Button
calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.config(padx=16, pady=4)
calculate_button.grid(column=1, row=2)

# Loop
window.mainloop()
