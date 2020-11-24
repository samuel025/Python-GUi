from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Sammy title')
#root.iconbitmap('c:/gui/codemi.ico')
root.geometry("300x400")

#Create database
conn = sqlite3.connect('address_book.db')

#create cursor
c = conn.cursor()


#create table

'''
c.execute(""" CREATE TABLE adresses (
			first_name text,
			last_name text,
			address text, 
			city text,
			state text,
			zipcode integer)""")
'''
#update function
def update():
	#Create database
	conn = sqlite3.connect('address_book.db')

	#create cursor
	c = conn.cursor()

	record_id = delete_box.get()

	c.execute("""UPDATE adresses SET
		first_name = :first,
		last_name = :last,
		address = :address,
		city = :city,
		state = :state,
		zipcode = :zipcode

		WHERE oid = :oid""",
		{'first': f_name_editor.get(),
		 'last': l_name_editor.get(),
		 'address': address_editor.get(),
		 'city': city_editor.get(), 
		 'state': state_editor.get(),
		 'zipcode': zipcode_editor.get(),

		 'oid': record_id
		})


	conn.commit()

	#Close
	conn.close()

	edit.destroy()
	
#Edit function
def edit():
	global edit
	edit = Tk()
	edit.title('Update Records')
	#root.iconbitmap('c:/gui/codemi.ico')
	edit.geometry("310x300")

	#Create database
	conn = sqlite3.connect('address_book.db')

	#create cursor
	c = conn.cursor()

	record_id = delete_box.get()
	#Query db
	c.execute("SELECT * FROM adresses WHERE oid = " + record_id)
	records = c.fetchall()
	#create global variables for text box names
	global f_name_editor
	global l_name_editor
	global address_editor
	global city_editor
	global state_editor
	global zipcode_editor
	#create textbox
	f_name_editor = Entry(edit, width=30)
	f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

	l_name_editor = Entry(edit, width=30)
	l_name_editor.grid(row=1, column=1, padx=20)

	address_editor = Entry(edit, width=30)
	address_editor.grid(row=2, column=1, padx=20)

	city_editor = Entry(edit, width=30)
	city_editor.grid(row=3, column=1, padx=20)

	state_editor = Entry(edit, width=30)
	state_editor.grid(row=4, column=1, padx=20)

	zipcode_editor = Entry(edit, width=30)
	zipcode_editor.grid(row=5, column=1, padx=20)



	#create texbox label
	f_name_label = Label(edit, text="First Name")
	f_name_label.grid(row=0, column=0, pady=(10, 0))

	l_name_label = Label(edit, text="Last Name")
	l_name_label.grid(row=1, column=0)

	address_label = Label(edit, text="Address")
	address_label.grid(row=2, column=0)

	city_label = Label(edit, text="City")
	city_label.grid(row=3, column=0)

	state_label = Label(edit, text="State")
	state_label.grid(row=4, column=0)

	zipcode_label = Label(edit, text="Zipcode")
	zipcode_label.grid(row=5, column=0)

	
	#loop through results
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		address_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		zipcode_editor.insert(0, record[5])

	#seve edit button
	edit_btn = Button(edit, text="Save Record", command=update)
	edit_btn.grid(row=6, column=0, columnspan=2, pady=10, ipadx=100)




#Create delete function
def delete():
	#Create database
	conn = sqlite3.connect('address_book.db')

	#create cursor
	c = conn.cursor()

	c.execute("DELETE from adresses WHERE oid= " + delete_box.get())
	delete_box.delete(0, END)

	conn.commit()


	#Close
	conn.close()

#create submit dunction
def submit():
	#Create database
	conn = sqlite3.connect('address_book.db')

	#create cursor
	c = conn.cursor()

	#insert into table
	c.execute("INSERT INTO adresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'address': address.get(),
				'city': city.get(),
				'state': state.get(),
				'zipcode': zipcode.get()
			})


	#commit changes
	conn.commit()


	#Close
	conn.close()

	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zipcode.delete(0, END)

#define query
def query():
	#Create database
	conn = sqlite3.connect('address_book.db')

	#create cursor
	c = conn.cursor()

	#Query db
	c.execute("SELECT *, oid FROM adresses")
	records = c.fetchall()
	#print(records)
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[6]) + "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(row=12, column=0, columnspan=2)

	#commit changes
	conn.commit()


	#Close
	conn.close()


#create textbox
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)


#create texbox label
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text='Select ID')
delete_box_label.grid(row=9, column=0, pady=5)
#Create submit button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, ipadx=70)


#create query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#delete button

delete_btn = Button(root, text="Delete Records", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#update button
update_btn = Button(root, text="Edit Records", command=edit)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


#commit changes
conn.commit()


#Close
conn.close()

root.mainloop()