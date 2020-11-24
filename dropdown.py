from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Sammy title')
#root.iconbitmap('c:/gui/codemi.ico')

def show():
	myLabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "THursday")
drop.pack()

myButton = Button(root, text="Show", command=show).pack()

mainloop()