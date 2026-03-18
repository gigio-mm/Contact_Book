def add_contact(Contacts, name, phone, email):
    contact = {"name": name, "phone": phone, "email": email, "favorite": False}
    Contacts.append(contact)

    print(f"Contact {name} added to your Contact Book!")
    return

def view_contacts(Contacts):
    print("\nContact Book:")
    for Index, Contact in enumerate(Contacts):
        status = "★" if Contact["favorite"] else ""
        name = Contact["name"]
        phone = Contact["phone"]
        email = Contact["email"]
        print(f"{Index + 1}. [{status} ] {name} - Phone: {phone} / E-mail: {email}")
    return

def edit_contact(Contacts, index):
    real_index = int(index - 1)

    if 0 <= real_index < len(Contacts):
        current_contact = Contacts[real_index]

        print(f"\n--- Editing current contact: {current_contact['name']} ---")
        print("Tip: Press 'Enter' to keep the current information.")

        new_name = input(f"Name {current_contact['name']} to: ").strip()
        new_phone = input(f"Change phone {current_contact['phone']} to: ").strip()
        new_email = input(f"Change email {current_contact['email']} to: ").strip()

        if new_name:
            current_contact['name'] = new_name
        if new_phone:
            current_contact['phone'] = new_phone
        if new_email:
            current_contact['email'] = new_email

        print(f"\nContact {current_contact['name']} updated sucessfully!")
    else:
        print(f"\nInvalid Contact number. Please try again.")
    return

def mark_unmark_favorite(Contacts, index):
    real_index = int(index - 1)

    if 0 <= real_index < len(Contacts):
        current_contact = Contacts[real_index]
        
        current_contact['favorite'] = not current_contact['favorite']
        
        status_msg = "marked as" if current_contact['favorite'] else "unmarked as"
        print(f"Contact {current_contact['name']} {status_msg} favorite.")
    else:
        print(f"\nInvalid Contact number. Please try again.")
    return

Contacts = []
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View List of Contacts")
    print("3. Edit Existing Contact")
    print("4. Mark/Unmark Contact as Favorite")
    print("5. View List of Favorite Contacts")
    print("6. Delete Contact")
    print("7. Exit")

    option = input("Choose your option: ")

    if option == "1":
        name = input("Enter Contact name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email Adress: ").strip()
        add_contact(Contacts, name, phone, email)
    elif option == "2":
        view_contacts(Contacts)
    elif option == "3":
        view_contacts(Contacts)
        Index = int(input("Type the Contact Number you want to edit: "))
        edit_contact(Contacts, Index)
    elif option == "4":
        view_contacts(Contacts)
        Index = int(input("Type the Contact Number you want to favorite / unfavorite: "))
        mark_unmark_favorite(Contacts, Index)
    elif option == "7":
        break