from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title('Sammy title')
#root.iconbitmap('c:/gui/codemi.ico')

def open():
	global my_img
	top = Toplevel()
	top.title('Sammy title')
	lbl = Label(top, text='Hello World').pack()
	my_img = ImageTk.PhotoImage(Image.open("images/image_1.jpg"))
	myLabel = Label(top, image=my_img).pack()
	btn2= Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="open Second", command=open).pack()



mainloop()