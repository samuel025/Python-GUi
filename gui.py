from tkinter import *
root = Tk()

e= Entry(root, width=50)
e.pack()
e.insert(0, "Enter Name: ") #for inserting place holders

def myClick():
    hello = "HELLO " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter", command=myClick)
myButton.pack()

root.mainloop()