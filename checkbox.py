from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Sammy title')
#root.iconbitmap('c:/gui/codemi.ico')


def show():
	myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this", variable=var, onvalue="on", offvalue="off")
c.deselect()
c.pack()

myLabel = Label(root, text=var.get()).pack()
myButton = Button(root, text="Show", command=show).pack()

mainloop()