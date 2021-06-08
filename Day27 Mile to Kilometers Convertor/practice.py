import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50,pady=50)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    my_label.config(text=input.get())

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="Click Me Also", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)
print(input.get())

window.mainloop()
