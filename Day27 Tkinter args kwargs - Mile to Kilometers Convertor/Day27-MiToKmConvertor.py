import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)


def button_click():
    km_value = float(tbox.get()) * 1.60934
    value.config(text=round(km_value, 2))


tbox = tkinter.Entry(width=7)
tbox.grid(column=1, row=0)

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)
is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

value = tkinter.Label(text="0")
value.grid(column=1, row=1)

km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

calculate = tkinter.Button(text="Calculate", command=button_click)
calculate.grid(column=1, row=2)

window.mainloop()
