from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Sammy title')
#root.iconbitmap('c:/gui/codemi.ico')
root.geometry("400x400")

#Create database
conn = sqlite3.connect('address_book.db')

#create cursor
c = conn.cursor()


#create table
c.execute(""" CREATE TABLE adresses (
			first_name text,
			last_name text,
			address text, 
			city text,
			state text,
			zipcode integer)""")

#commit changes
conn.commit()


#Close
conn.close()

root.mainloop()