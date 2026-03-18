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
        print(f"{Index + 1}. [{status}] {name} - Contacts: {phone} - {email}")
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

    escolha = input("Choose your option: ")

    if escolha == "1":
        name = input("Enter Contact name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email Adress: ")
        add_contact(Contacts, name, phone, email)
    elif escolha == "2":
        view_contacts(Contacts)