### Contact book (with GUI)
### A program that allows users to add, search, and delete contacts.



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ContactBook(tk.Tk):
	def __init__(self):
		self.contacts = []



	def add_contact(self, contact):
		self.contacts.append(contact)

	def search_contact(self, name):


		self.mainloop()

# Write your own classes below






### Contact book with samples
contactBook = {'John Jo': '555-555-5555', 'Mugi Mu': '556-556-5656', 'Mike Mi' : '554-554-5454', 'Lora Lo' : '557-557-5757'}


# execution code
ContactBook('Contact Book', (600,600)) #edit to insert your own title and window size
