from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('My own program')


img1 = ImageTk.PhotoImage(Image.open("images/image_1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/image_2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/image_3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images/image_4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/image_5.jpg"))

image_list = [img1, img2, img3, img4, img5]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label= Label(image=image_list[image_number-1])
	button_forward = Button(root, text="Next Image", command=lambda: forward(image_number+1), width=20)
	button_back = Button(root, text="Previous Image", command=lambda: back(image_number-1), width=20)

	if image_number == 5:
		button_forward = Button(root, text="Next Image", state=DISABLED, width=20)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

	status = Label(root, text="Image " + str(image_number) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
	global my_label
	global button_forward
	global button_back
	
	my_label.grid_forget()
	my_label= Label(image=image_list[image_number-1])
	button_forward = Button(root, text="Next Image", command=lambda: forward(image_number+1), width=20)
	button_back = Button(root, text="Previous Image", command=lambda: back(image_number-1), width=20)

	if image_number == 1:
		button_back = Button(root, text="Previous Image", state=DISABLED, width=20)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

	status = Label(root, text="Image " + str(image_number) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="Previous Image", command=back, state=DISABLED, width=20)
button_exit = Button(root, text="Exit", command=root.quit, width=20)
button_forward = Button(root, text="Next Image", command=lambda: forward(2), width=20)


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)



root.mainloop()