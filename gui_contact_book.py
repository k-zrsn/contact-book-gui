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


### Contact book class
class contactBook:
	def __init__(self):
		self.contacts = []



	def add_contact(self, contact):
		self.contacts.append(contact)

	def search_contact(self, name):
		for contact in self.contacts:
			if contact.name.lower() == name.lower():
				return contact
		return None








### Contact book with samples
'''
contactList = {'John Jo': '555-555-5555', 'Mugi Mu': '556-556-5656', 'Mike Mi' : '554-554-5454', 'Lora Lo' : '557-557-5757'}
'''


### run
app('Contact Book', (600,600))
