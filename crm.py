from tkinter import*
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
import csv
from tkinter import ttk

root = Tk()
root.title('Database')
root.resizable(height = 0, width = 0)
root.iconbitmap('index.ico')
root.geometry("400x600")
load = Image.open("image_4.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

mydb = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='sam1dave2',
	database = "samwell"
	)


my_cursor = mydb.cursor()
#create db
#my_cursor.execute("CREATE DATABASE samwell")

#create table


my_cursor.execute("CREATE TABLE IF NOT EXISTS costumers(first_name VARCHAR(255),\
	last_name VARCHAR(255), \
	zipcode INT(10),\
	price_paid DECIMAL(10,2), \
	user_id INT AUTO_INCREMENT PRIMARY KEY)")

'''
#alter table
my_cursor.execute("ALTER TABLE costumers ADD (\
	email VARCHAR(255),\
	address_1 VARCHAR(255),\
	address_2 VARCHAR(255),\
	city VARCHAR(255),\
	state VARCHAR(255),\
	country VARCHAR(255),\
	phone VARCHAR(255),\
	payment_method VARCHAR(255),\
	discount_code VARCHAR(255))")
'''
#clear fields button
def clear_fields():
	first_name_box.delete(0, END)
	last_name_box.delete(0, END)
	email_box.delete(0, END)
	zipcode_box.delete(0, END)
	price_paid_box.delete(0, END)
	address_1_box.delete(0, END)
	address_2_box.delete(0, END)
	city_box.delete(0, END)
	state_box.delete(0, END)
	country_box.delete(0, END)
	phone_box.delete(0, END)
	payment_method_box.delete(0, END)
	discount_code_box.delete(0, END)

#add customer to database
def add_customer():
	sql_command = "INSERT INTO costumers (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(), address_1_box.get(), address_2_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get())
	my_cursor.execute(sql_command, values)

	mydb.commit()

	clear_fields()

# write to csv
def write_to_csv(result):
	with open('customers.csv', 'w') as f:
		w = csv.writer(f, dialect='excel')
		for records in result:
			w.writerow(records)


#search customers
def search_customers(): 
	search = Tk()
	search.title("Search Customers")
	search.geometry("1000x700")

	def update():
		sql_command = """UPDATE costumers SET first_name = %s, last_name = %s, zipcode = %s, price_paid = %s, email = %s, address_1 = %s, address_2 = %s, city = %s, state = %s, country = %s, phone = %s, payment_method = %s, discount_code = %s WHERE user_id = %s"""

		first_name = first_name_box2.get()
		last_name = last_name_box2.get()
		email = email_box2.get()
		zipcode = zipcode_box2.get()
		price_paid = price_paid_box2.get()
		address_1 = address_1_box2.get()
		address_2 = address_2_box2.get()
		city = city_box2.get()
		state = state_box2.get()
		country = country_box2.get()
		phone = phone_box2.get()
		payment_method = payment_method_box2.get()
		discount_code = discount_code_box2.get()

		id_value = id_box2.get()
		inputs = (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code, id_value)
		my_cursor.execute(sql_command, inputs)
		mydb.commit()

		search.destroy()
	def edit_now(id, index):
		sql2 = "SELECT * FROM costumers WHERE user_id = %s"
		#sql = "SELECT * FROM costumers WHERE last_name = %s"
		name2 = (id, )
		result2 = my_cursor.execute(sql2, name2)
		result2 = my_cursor.fetchall()
		

		#create main form to enter customer data
		first_name_label = ttk.Label(frame, text="First Name").grid(row=index+1,column=0,sticky=W, padx=10, pady=10)
		last_name_label = ttk.Label(frame, text="Last Name").grid(row=index+2,column=0,sticky=W, padx=10)
		email_label = ttk.Label(frame, text="Email").grid(row=index+3, column=0,sticky=W, padx=10)
		zipcode_label = ttk.Label(frame, text="zipcode").grid(row=index+4,column=0,sticky=W, padx=10)
		price_paid_label = ttk.Label(frame, text="Price Paid").grid(row=index+5,column=0,sticky=W, padx=10)
		address_1_label = ttk.Label(frame, text="Address 1").grid(row=index+6,column=0,sticky=W, padx=10)
		address_2_label = ttk.Label(frame, text="Address 2").grid(row=index+7,column=0,sticky=W, padx=10)
		city_label = ttk.Label(frame, text="City").grid(row=index+8,column=0,sticky=W, padx=10)
		state_label = ttk.Label(frame, text="State").grid(row=index+9,column=0,sticky=W, padx=10)
		country_label = ttk.Label(frame, text="Country").grid(row=index+10,column=0,sticky=W, padx=10)
		phone_label = ttk.Label(frame, text="Phone").grid(row=index+11,column=0,sticky=W, padx=10)
		payment_method_label = ttk.Label(frame, text="Payment Method").grid(row=index+12,column=0,sticky=W, padx=10)
		discount_code_label = ttk.Label(frame, text="Discount Code").grid(row=index+13, column=0,sticky=W, padx=10)
		id_label = Label(frame, text="User Id").grid(row=index+14, column=0, sticky=W, padx=10)

		#create entry boxes
		global first_name_box2
		first_name_box2 = ttk.Entry(frame, width=25)
		first_name_box2.grid(row=index+1, column=1, pady=10)
		first_name_box2.insert(0, result2[0][0])

		global last_name_box2
		last_name_box2 = ttk.Entry(frame, width=25)
		last_name_box2.grid(row=index+2, column=1, pady=5)
		last_name_box2.insert(0, result2[0][1])


		global email_box2
		email_box2 = ttk.Entry(frame, width=25)
		email_box2.grid(row=index+3, column=1, pady=5)
		email_box2.insert(0, result2[0][5])


		global zipcode_box2
		zipcode_box2 = ttk.Entry(frame, width=25)
		zipcode_box2.grid(row=index+4, column=1, pady=5)
		zipcode_box2.insert(0, result2[0][2])


		global price_paid_box2
		price_paid_box2 = ttk.Entry(frame, width=25)
		price_paid_box2.grid(row=index+5, column=1, pady=5)
		price_paid_box2.insert(0, result2[0][3])


		global address_1_box2
		address_1_box2 = ttk.Entry(frame, width=25)
		address_1_box2.grid(row=index+6, column=1, pady=5)
		address_1_box2.insert(0, result2[0][6])


		global address_2_box2
		address_2_box2 = ttk.Entry(frame, width=25)
		address_2_box2.grid(row=index+7, column=1, pady=5)
		address_2_box2.insert(0, result2[0][7])


		global city_box2
		city_box2 = ttk.Entry(frame, width=25)
		city_box2.grid(row=index+8, column=1, pady=5)
		city_box2.insert(0, result2[0][8])


		global state_box2
		state_box2 = ttk.Entry(frame, width=25)
		state_box2.grid(row=index+9, column=1, pady=5)
		state_box2.insert(0, result2[0][9])


		global country_box2
		country_box2 = ttk.Entry(frame, width=25)
		country_box2.grid(row=index+10, column=1, pady=5)
		country_box2.insert(0, result2[0][10])


		global phone_box2
		phone_box2 = ttk.Entry(frame, width=25)
		phone_box2.grid(row=index+11, column=1, pady=5)
		phone_box2.insert(0, result2[0][11])


		global payment_method_box2
		payment_method_box2 = ttk.Entry(frame, width=25)
		payment_method_box2.grid(row=index+12, column=1, pady=5)
		payment_method_box2.insert(0, result2[0][12])


		global discount_code_box2
		discount_code_box2 = ttk.Entry(frame, width=25)
		discount_code_box2.grid(row=index+13, column=1, pady=5)
		discount_code_box2.insert(0, result2[0][13])


		global id_box2
		id_box2 = ttk.Entry(frame, width=25)
		id_box2.grid(row=index+14, column=1, pady=5)
		id_box2.insert(0, result2[0][4])


		save_record = ttk.Button(frame, text="Save", command=update)
		save_record.grid(row=index+15, column=0, padx=5)

	def search_now():
		selected = drop.get()
		if selected == "Search by....":
			return
		if selected == "Last Name":
			sql = "SELECT * FROM costumers WHERE last_name = %s"
		if selected == "Email Address":
			sql = "SELECT * FROM costumers WHERE email = %s"
		if selected == "Customer ID":
			sql = "SELECT * FROM costumers WHERE user_id = %s"

		searched = search_box.get()
		#sql = "SELECT * FROM costumers WHERE last_name = %s"
		name = (searched, )
		result = my_cursor.execute(sql, name)
		result = my_cursor.fetchall()
		global frame
		frame = Frame(search, width=100, highlightbackground='black', highlightthicknes=1)
		frame.grid(row=2, column=0, padx=10, pady=10, ipadx=3, ipady=3)
		frame_clear = Frame(search, width=100, highlightbackground='black')
		frame_clear.grid(row=3, column=0)
		# def clear_frame():
		# 	for widget in frame.winfo_children():
		# 		widget.destroy()
		def clear_frame():
			frame.destroy()
			frame_clear.destroy()
		if not result:
			result = "Record Not Found..."
			searched_label = Label(frame, text=result, justify="center")
			searched_label.grid(row=2, column=0)
		else:
			global num
			global index
			for index, x in enumerate(result):
				num = 0
				index += 2
				id_reference = str(x[4])
				edit_button = ttk.Button(frame, text="Edit", command=lambda:edit_now(id_reference, index))
				edit_button.grid(row=index, column=num, pady=3)
				for y in x:
					searched_label = Label(frame, text=y, justify="center")
					searched_label.grid(row=index, column=num+2, pady=3)
					num +=1

		clear_button = ttk.Button(frame_clear, text="clear", command=clear_frame)
		clear_button.grid(row=index+1, column=0, sticky=W)
		# searched_label = Label(search, text=result)
		# searched_label.grid(row=3, column=0, padx=10, columnspan=2)
	frame3 = Frame(search)
	frame3.grid(row=0, column=0, sticky=W)

	search_box = ttk.Entry(frame3)
	search_box.grid(row=0, column=1, padx=10, pady=10, sticky=W)

	search_box_label = ttk.Label(frame3, text="Search " )
	search_box_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

	search_btn = ttk.Button(frame3, text="Search Customers", command=search_now)
	search_btn.grid(row=1, column=0, padx=10, sticky=W)

	#drop box
	drop = ttk.Combobox(frame3, value=["Search by....","Last Name", "Email Address", "Customer ID"])
	drop.current(0)
	drop.grid(row=0, column=2)


def list_customers():
	list_customers_query = Tk()
	list_customers_query.title("List of costumers")
	list_customers_query.geometry("760x500")
	list_customers_query.resizable(height = 0, width = 0)
	# canvas = Canvas(container)
	# scrollbar = ttk.Scrollbar(container, orien="vertical", command=canvas.yview)
	# scrollable_frame = ttk.Frame(canvas)

	# scrollable_frame.bind(
	# 	"<Configure>",
	# 	lambda e: canvas.configure(
	# 		scrollregion=canvas.bbox("all")
	# 		)
	# 	)

	# canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
	# canvas.configure(yscrollcommand=scrollbar.set, width=777, height="595")

	my_cursor.execute("SELECT * FROM costumers")
	result = my_cursor.fetchall()

	Framed = ttk.Frame(list_customers_query)
	Framed.grid(pady=50, row=1, column=0, padx=10)

	title_label = Label(list_customers_query, text="Customers Table", font=("Times", 16,"bold"))
	title_label.place(x=335, y=10)	

	
	tv = ttk.Treeview(Framed, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14), show="headings", height=15)
	tv.pack(side=LEFT)
	# tv.place(x=0, y=0)

	tv.heading(1, text="First Name")
	tv.heading(2, text="Last Name")
	tv.heading(3, text="Zipcode")
	tv.heading(4, text="Price Paid")
	tv.heading(5, text="User ID")
	tv.heading(6, text="Email")
	tv.heading(7, text="Address 1")
	tv.heading(8, text="Address 2")
	tv.heading(9, text="City")
	tv.heading(10, text="State")
	tv.heading(11, text="Country")
	tv.heading(12, text="Phone")
	tv.heading(13, text="Payment Method")
	tv.heading(14, text="Coupon Code")

	tv.column(1, width=60, minwidth=100)
	tv.column(2, width=60, minwidth=100)
	tv.column(3, width=60, minwidth=100)
	tv.column(4, width=60, minwidth=100)
	tv.column(5, width=60, minwidth=100)
	tv.column(6, width=60, minwidth=100)
	tv.column(7, width=60, minwidth=100)
	tv.column(8, width=60, minwidth=100)
	tv.column(9, width=60, minwidth=100)
	tv.column(10, width=60, minwidth=100)
	tv.column(11, width=60, minwidth=100)
	tv.column(12, width=60, minwidth=100)
	tv.column(13, width=60, minwidth=100)
	tv.column(14, width=60, minwidth=100)


	#verrtical scroll bar
	yscrollbar = ttk.Scrollbar(Framed, orient="vertical", command=tv.yview)
	yscrollbar.place(x=734, y=1, height=325)

	xscrollbar = ttk.Scrollbar(list_customers_query, orient="horizontal", command=tv.xview)
	xscrollbar.place(x=4, y=377, width=755)

	tv.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
	tv.pack_propagate(0)

	# row = 1
	# column = 0
	for results in result:
		tv.insert("", 'end', values=results)
		
	# 	row += 1
	# 	lookup_label = Label(scrollable_frame, text="Customer Id:              " + str(results[4]) + "\n"
	# 													+ "Name:                         " + str(results[0]) + "\n" 
	# 													+ "Last Name:                 " + str(results[1]) + "\n" 
	# 													+ "Zipcode:                     " + str(results[2]) + "\n"
	# 													+ "Price Paid:                  " + str(results[3]) + "\n"
	# 													+ "Mail:                            " + str(results[5]) + "\n"
	# 													+ "Address 1:                   " + str(results[6]) + "\n"
	# 													+ "Address 2:                   " + str(results[7]) + "\n"
	# 													+ "City:                             " + str(results[8]) + "\n"
	# 													+ "State:                            " + str(results[9]) + "\n"
	# 													+ "Country:                      " + str(results[10]) + "\n"
	# 													+ "Phone:                         " + str(results[11]) + "\n"
	# 													+ "Payment Method:      " + str(results[12]) + "\n"
	# 													+ "Coupon Code:            " + str(results[13]) + "\n"
	# 													+ "=========================================",
	# 													 justify="left")
	# 	lookup_label.grid(row=row, column=column)
	

	csv_button = ttk.Button(list_customers_query, text="Save to Excel", command=lambda: write_to_csv(result))
	csv_button.place(x=10, y=430)


	# canvas.pack(side = "left", fill="both", expand=True)
	# scrollbar.pack(side="right", fill="y")

# create label
title_label = Label(root, text="Samuel's CRM Database", bg="#ffffff", font=("Times", 16,"bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

#create main form to enter customer data
first_name_label = Label(root, text="First Name", bg="#ffffff", fg="black").grid(row=1,column=0,sticky=W, padx=10)
last_name_label = Label(root, text="Last Name", bg="white", fg="black").grid(row=2,column=0,sticky=W, padx=10)
email_label = Label(root, text="Email", bg="white", fg="black").grid(row=3, column=0,sticky=W, padx=10)
zipcode_label = Label(root, text="zipcode", bg="white", fg="black").grid(row=4,column=0,sticky=W, padx=10)
price_paid_label = Label(root, text="Price Paid", bg="white", fg="black").grid(row=5,column=0,sticky=W, padx=10)
address_1_label = Label(root, text="Address 1", bg="white", fg="black").grid(row=6,column=0,sticky=W, padx=10)
address_2_label = Label(root, text="Address 2", bg="white", fg="black").grid(row=7,column=0,sticky=W, padx=10)
city_label = Label(root, text="City", bg="white", fg="black").grid(row=8,column=0,sticky=W, padx=10)
state_label = Label(root, text="State", bg="white", fg="black").grid(row=9,column=0,sticky=W, padx=10)
country_label = Label(root, text="Country", bg="white", fg="black").grid(row=10,column=0,sticky=W, padx=10)
phone_label = Label(root, text="Phone", bg="white", fg="black").grid(row=11,column=0,sticky=W, padx=10)
payment_method_label = Label(root, text="Payment Method", bg="white", fg="black").grid(row=12,column=0,sticky=W, padx=10)
discount_code_label = Label(root, text="Discount Code", bg="white", fg="black").grid(row=13, column=0,sticky=W, padx=10)


#create entry boxes
first_name_box = ttk.Entry(root)
first_name_box.grid(row=1, column=1, sticky=W)

last_name_box = ttk.Entry(root)
last_name_box.grid(row=2, column=1, pady=5, sticky=W)

email_box = ttk.Entry(root)
email_box.grid(row=3, column=1, pady=5, sticky=W)

zipcode_box = ttk.Entry(root)
zipcode_box.grid(row=4, column=1, pady=5, sticky=W)

price_paid_box = ttk.Entry(root)
price_paid_box.grid(row=5, column=1, pady=5, sticky=W)

address_1_box = ttk.Entry(root)
address_1_box.grid(row=6, column=1, pady=5, sticky=W)

address_2_box = ttk.Entry(root)
address_2_box.grid(row=7, column=1, pady=5, sticky=W)

city_box = ttk.Entry(root)
city_box.grid(row=8, column=1, pady=5, sticky=W)

state_box = ttk.Entry(root)
state_box.grid(row=9, column=1, pady=5, sticky=W)

country_box = ttk.Entry(root)
country_box.grid(row=10, column=1, pady=5, sticky=W)

phone_box = ttk.Entry(root)
phone_box.grid(row=11, column=1, pady=5, sticky=W)

payment_method_box = ttk.Combobox(root, value=["Master Card", "Visa", "Cash", "Paypal"  ], width=17)
payment_method_box.grid(row=12, column=1, pady=5, sticky=W)

discount_code_box = ttk.Entry(root)
discount_code_box.grid(row=13, column=1, pady=10, sticky=W)

#create buttom
add_customer_button = ttk.Button(root, text="Add Customer To Database", command=add_customer)
add_customer_button.grid(row=14, column=0, padx=10)

clear_fields_button = ttk.Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=14, column=1)

list_customers_button = ttk.Button(root, text="List Customers", command=list_customers)
list_customers_button.grid(row=15, column=0, sticky=W, padx=10)

search_customers_button = ttk.Button(root, text="Search/Edit Customers", command=search_customers)
search_customers_button.grid(row=16, column=0, sticky=W, padx=10)

root.mainloop()