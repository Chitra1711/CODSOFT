import tkinter as tk
from tkinter import messagebox

# Create a dictionary to store contact information
contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone are required.")

# Function to update the contact list
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        contact_listbox.insert(tk.END, name)

# Function to display contact details when selected from the list
def display_contact(event):
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact in contacts:
        details = contacts[selected_contact]
        details_text.config(text=f"Phone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
    else:
        details_text.config(text="")

# Function to clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to search for a contact by name or phone number
def search_contact():
    query = search_entry.get()
    if query:
        matches = [name for name in contacts if query in name or query in contacts[name]['Phone']]
        contact_listbox.delete(0, tk.END)
        for name in matches:
            contact_listbox.insert(tk.END, name)

# Function to update contact details
def update_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact in contacts:
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if name and phone:
            contacts[selected_contact] = {'Phone': phone, 'Email': email, 'Address': address}
            update_contact_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone are required.")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact in contacts:
        del contacts[selected_contact]
        update_contact_list()
        clear_entries()
        details_text.config(text="")

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Labels and entry fields for contact information
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Add, Search, Update, and Delete buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

# List of contacts
contact_listbox = tk.Listbox(root)
contact_listbox.pack()
contact_listbox.bind("<<ListboxSelect>>", display_contact)

# Display contact details
details_text = tk.Label(root, text="")
details_text.pack()

# Start the main loop
update_contact_list()
root.mainloop()
