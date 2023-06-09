from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# Entry

input = Entry()
input.pack()

# Button


def button_clicked():
    user_input = input.get()
    my_label.config(text=user_input)


button = Button(text="Click Me", command=button_clicked)
button.pack()





window.mainloop()
