from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Sammy title')
#root.iconbitmap('c:/gui/codemi.ico')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

myLabel = Label(root, text=horizontal.get()).pack()

def slide():
	myLabel = Label(root, text=horizontal.get()).pack()
	
mybutton = Button(root, text="Click", command=slide).pack()


mainloop()