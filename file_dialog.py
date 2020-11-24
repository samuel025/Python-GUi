from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog


root = Tk()
root.title('Sammy title')
#root.iconbitmap('c:/gui/codemi.ico')



def open():
	global my_img
	root.filename = filedialog.askopenfilename(initialdir="/gui/", title="Select File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
	myLabel = Label(root, text=root.filename).pack()
	my_img = ImageTk.PhotoImage(Image.open(root.filename))
	my_img_label = Label(image=my_img).pack()


my_btn = Button(root, text="Open File", command=open).pack()
root.mainloop()