from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('My own program')


frame = LabelFrame(root, text="This is a frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)


b = Button(frame, text="How far")
b2 = Button(frame, text="How Well")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()