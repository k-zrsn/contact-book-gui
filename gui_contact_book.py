### Contact book (with GUI)
### A program that allows users to add, search, and delete contacts.



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App(tk.Tk):
	def __init__(self, title, size):
		
		# main setup
		super().__init__()
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0],size[1])

		# widgets
        # this is where you call your other classes
		
		# run 
		self.mainloop()

# Write your own classes below







### Contact book with samples
contactBook = {'John Jo': '555-555-5555', 'Mugi Mu': '556-556-5656', 'Mike Mi' : '554-554-5454', 'Lora Lo' : '557-557-5757'}


# execution code
App('Class based app', (600,600)) #edit to insert your own title and window size
