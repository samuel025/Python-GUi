from tkinter import*
from tkinter import messagebox


root = Tk()
root.title('Sammy title')
#root.iconbitmap('c:/gui/codemi.ico')

#types of popup boxes
#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

'''This is for askyesno messagebox
def popup():
	response = messagebox.askyesno("This is my popup", "Hello World")
	#Label(root, text=response).pack()
	if response == 1:
		Label(root, text="You clicked yes").pack()
	else:
		Label(root, text="You clicked no").pack()
'''

def popup():
	response = messagebox.askquestion("This is my popup", "Hello World")
	Label(root, text=response).pack()
	if response == 'yes':
		Label(root, text="You clicked yes").pack()
	else:
		Label(root, text="You clicked no").pack()


Button(root, text="popup", command=popup).pack()

mainloop()