import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x450")
        self.root.configure(background="light blue")

       
        self.contacts = []

   
   
        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="Name", bg="light blue").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text="Phone", bg="light blue").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text="Email", bg="light blue").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text="Address", bg="light blue").grid(row=3, column=0, padx=10, pady=5, sticky="w")

 
 
        self.name_entry = tk.Entry(self.root)
        self.phone_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.address_entry = tk.Entry(self.root)

        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=1, padx=10, pady=10, sticky="e")
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=5, column=1, padx=10, pady=10, sticky="e")
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=6, column=1, padx=10, pady=10, sticky="e")
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=7, column=1, padx=10, pady=10, sticky="e")
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=1, padx=10, pady=10, sticky="e")
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=9, column=1, padx=10, pady=10, sticky="e")

        # Text Area to display contacts
        self.display_area = tk.Text(self.root, height=10, width=40, font=("Arial", 10))
        self.display_area.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not phone:
            messagebox.showerror("Input Error", "Name and Phone fields are required.")
            return

        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        self.contacts.append(contact)

        self.clear_entries()
        self.display_contacts()
        messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        self.display_contacts()

    def search_contact(self):
        search_term = self.name_entry.get().strip() or self.phone_entry.get().strip()

        if not search_term:
            messagebox.showerror("Input Error", "Please enter a name or phone number to search.")
            return

        matches = [contact for contact in self.contacts if search_term in contact["Name"] or search_term in contact["Phone"]]

        if matches:
            self.display_area.delete(1.0, tk.END)
            for contact in matches:
                self.display_area.insert(tk.END, f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n\n")
        else:
            messagebox.showinfo("Not Found", "No matching contacts found.")

    def update_contact(self):
        search_term = self.name_entry.get().strip() or self.phone_entry.get().strip()

        if not search_term:
            messagebox.showerror("Input Error", "Please enter a name or phone number to search.")
            return

        for contact in self.contacts:
            if search_term in contact["Name"] or search_term in contact["Phone"]:
                contact["Name"] = self.name_entry.get().strip()
                contact["Phone"] = self.phone_entry.get().strip()
                contact["Email"] = self.email_entry.get().strip()
                contact["Address"] = self.address_entry.get().strip()

                self.clear_entries()
                self.display_contacts()
                messagebox.showinfo("Success", "Contact updated successfully.")
                return

        messagebox.showinfo("Not Found", "No matching contact found.")

    def delete_contact(self):
        search_term = self.name_entry.get().strip() or self.phone_entry.get().strip()

        if not search_term:
            messagebox.showerror("Input Error", "Please enter a name or phone number to search.")
            return

        for i, contact in enumerate(self.contacts):
            if search_term in contact["Name"] or search_term in contact["Phone"]:
                del self.contacts[i]
                self.clear_entries()
                self.display_contacts()
                messagebox.showinfo("Success", "Contact deleted successfully.")
                return

        messagebox.showinfo("Not Found", "No matching contact found.")

    def display_contacts(self):
        self.display_area.delete(1.0, tk.END)
        if not self.contacts:
            self.display_area.insert(tk.END, "No contacts available.")
        else:
            for contact in self.contacts:
                self.display_area.insert(tk.END, f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n\n")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
