import json
import os

# Define the file where contacts will be stored
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact to the contact book."""
    name = input("Enter the contact's name: ")
    lastname = input("Enter the contact's lastname: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    company = input("Enter the contact's campany:")
   
    if name in contacts:
        print("Contact already exists. Updating the existing contact.")
    
    contacts[name] = {
        'lastname': lastname,
        'phone': phone,
        'email': email,
        'company': company
    }
    save_contacts(contacts)
    print(f"Contact '{name}' added/updated successfully.")

def view_contacts(contacts):
    """View all contacts in the contact book."""
    if not contacts:
        print("No contacts available.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print()

def delete_contact(contacts):
    """Delete a contact from the contact book."""
    name = input("Enter the contact's name to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

def main():
    """Main function to interact with the contact book."""
    contacts = load_contacts()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        
        choice = input("Select an option (1/2/3/4): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
