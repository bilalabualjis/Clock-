from tkinter import *
from tkinter.ttk import *

from time import strftime

# Creating a root window
root = Tk()

# Adding a title to the window
root.title("Clock")

# Defining a time function
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background="blue", foreground= "black")
label.pack(anchor='center')
time()

mainloop()