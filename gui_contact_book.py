### Contact book (with GUI)
### A program that allows users to add, search, and delete contacts.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



### Application class
class app(tk.Tk):
	def __init__(self, title, size):
		
		# main setup
		super().__init__()
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0],size[1])

		# widgets
        # this is where you call your other classes
		###self.menu = Menu(self) # delete this example in your own code

		# run 
		self.mainloop()



### Contact class
class contact_information:
	def __init__(self, name, phone):
		self.name = name
		self.phone = phone

	def __str__(self):
		return f"{self.name}: {self.phone}"



### Contact book class
class contact_book:
	def __init__(self):
		self.contacts = []



	def add_contact_to_book(self, contact):
		self.contacts.append(contact)

	def search_contact(self, name):
		for contact in self.contacts:
			if contact.name.lower() == name.lower():
				return contact
		return None



def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contact_book.add_contact_to_book(contact_information(name, phone))
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both name and phone number.")





### Contact book with samples
'''
contactList = {'John Jo': '555-555-5555', 'Mugi Mu': '556-556-5656', 'Mike Mi' : '554-554-5454', 'Lora Lo' : '557-557-5757'}
'''


### run
app = tk.Tk()
app.title = ("Contact Book")
contact_book = contact_book()


name_entry = tk.Entry(app, width=30)
name_entry.pack(pady=10)
name_entry.insert(0, "Name")

phone_entry = tk.Entry(app, width=30)
phone_entry.pack(pady=10)
phone_entry.insert(0, "Phone Number")

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact)
add_button.pack(side=tk.LEFT, padx=5)

app.mainloop()