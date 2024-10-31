### Contact book (with GUI)
### A program that allows users to add, search, and delete contacts.

import tkinter as tk
from tkinter import messagebox




class contactInfo:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


    def __str__(self):
        return f"{self.name}: {self.phone}, {self.email} "



class contactBook:
    def __init__(self):
        self.contacts = []


    def add_contact_to_book(self, contact):
        self.contacts.append(contact)


    def search_contact_in_book(self, search_name):
        search_match = []
        index = 0

        for contact in self.contacts:
            if search_name in contact.name.lower():
                search_match.append(index)
            index += 1
        return search_match


    def delete_contact_from_book(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]





def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        contact_book.add_contact_to_book(contactInfo(name, phone, email))
        listbox.delete(0, tk.END)  
        for contact in contact_book.contacts:
            listbox.insert(tk.END, str(contact))
    else:
        messagebox.showwarning("Input Error", "Please enter both name and phone number.")



def search_contact():
    search_entry = name_entry.get().lower()
    listbox.selection_clear(0, tk.END)  
    search_result = contact_book.search_contact_in_book(search_entry)

    if search_result:
        for index in search_result:
            listbox.selection_set(index)
            listbox.see(index)
    else:
        messagebox.showinfo("Search Result", "No matching contacts found.")



def delete_contact():
    selected_index = listbox.curselection()

    if selected_index:
        index = selected_index[0]
        contact_book.delete_contact_from_book(index)
        listbox.delete(index)
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")




app = tk.Tk()
app.title("Contact Book")

contact_book = contactBook()

name_entry = tk.Entry(app, width=30)
name_entry.pack(pady=10)
name_entry.insert(0, "Name")

phone_entry = tk.Entry(app, width=30)
phone_entry.pack(pady=10)
phone_entry.insert(0, "Phone")

email_entry = tk.Entry(app, width=30)
email_entry.pack(pady=10)
email_entry.insert(0, "Email")

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
delete_button.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(button_frame, text="Search Contact", command=search_contact)
search_button.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(app, width=50, height=10)
listbox.pack(pady=10)

app.mainloop()
