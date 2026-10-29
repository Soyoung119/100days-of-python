from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    convert_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_label = Label(text = "Miles")
miles_label.grid(row=0, column=2)

is_label = Label(text = "is equal to")
is_label.grid(row=1, column=0)

convert_label = Label(text = "0")
convert_label.grid(row=1, column=1)

km_label = Label(text = "Km")
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(row=0, column=1)

window.mainloop()