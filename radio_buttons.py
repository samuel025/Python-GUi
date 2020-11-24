from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title('Sammy title')
#root.iconbitmap('c:/gui/codemi.ico')

# r = IntVar()
# r.set('2')
#for string
#r = StrVar()
MODES = [
	("Pepperoni", "Pepperoni"),
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom"),
	("Onion", "Onion"),
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in MODES:
	Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
	myLabel = Label(root, text=value)
	myLabel.pack()


#this is for doing it one by one
# Radiobutton(root, text='option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

# myLabel = Label(root, text=pizza.get())
# myLabel.pack()

myButton = Button(root, text='Click', command=lambda: clicked(pizza.get()))
myButton.pack()
mainloop()
