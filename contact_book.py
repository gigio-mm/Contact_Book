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
        print(f"{Index + 1}. [{status}] {name} - Phone: {phone} / E-mail: {email}")
    return

def edit_contact(Contacts, index):
    real_index = int(index - 1)

    if 0 <= real_index < len(Contacts):
        current_contact = Contacts[real_index]

        print(f"\n--- Editing current contact: {current_contact['name']} ---")
        print("Tip: Press 'Enter' to keep the current information.")

        new_name = input(f"Name {current_contact['name']} to: ")
        new_phone = input(f"Change phone {current_contact['phone']} to: ")
        new_email = input(f"Change email {current_contact['email']} to: ")

        if new_name:
            current_contact['name'] = new_name
        if new_phone:
            current_contact['phone'] = new_phone
        if new_email:
            current_contact['email'] = new_email

        print(f"\nContact {current_contact['name']} updated sucessfully!")
    else:
        print("\nInvalid Contact number. Please try again.")
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

    escolha = input("Choose your option: ")

    if escolha == "1":
        name = input("Enter Contact name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email Adress: ")
        add_contact(Contacts, name, phone, email)
    elif escolha == "2":
        view_contacts(Contacts)
    elif escolha == "3":
        view_contacts(Contacts)
        Index = int(input("Type the number of the Contact you want to edit: "))
        edit_contact(Contacts, Index)
    elif escolha == "7":
        break