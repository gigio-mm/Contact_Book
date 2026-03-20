# 📇 Contact Book Manager (CLI)

A terminal-based Contact Book application developed as a practical challenge for the **Rocketseat Python Fundamentals** module. This project demonstrates core Python concepts such as list manipulation, dictionary management, and conditional flow control.

## 🚀 Features

The application allows users to manage a digital contact list with the following functionalities:

* **Add Contacts**: Save a contact's name, phone, and email.
* **View Contacts**: Display a complete list of all registered contacts.
* **Edit Contacts**: Update existing information (Name, Phone, or Email) with a "smart-keep" feature (press Enter to keep current data).
* **Favorite System**: Mark or unmark contacts as favorites with a visual indicator (★).
* **Filter Favorites**: View a dedicated list containing only your favorite contacts.
* **Delete Contacts**: Remove contacts from the list safely by their index.

## 🛠️ Technologies Used

* **Python 3.14**: Core logic and data structures.
* **Clean Code Practices**: Modular functions and descriptive naming conventions.
* **Conventional Commits**: Organized Git history.

## 📦 How to Run

1.  **Prerequisites**: Ensure you have Python installed on your machine.
2.  **Clone the repository**:
    ```bash
    git clone https://github.com/gigio-mm/contact-book.git
    ```
3.  **Navigate to the folder**:
    ```bash
    cd contact-book
    ```
4.  **Run the application**:
    ```bash
    python contact_book.py
    ```

## 📝 Code Structure

The project is structured into specific functions to ensure maintainability:
- `add_contact()`: Handles data input and storage.
- `view_contacts()`: Iterates and formats the full contact list.
- `edit_contact()`: Manages updates using index-based selection.
- `mark_unmark_favorite()`: Toggles the boolean status of a contact.
- `view_favorites()`: Filters and displays only favored contacts.
- `delete_contact()`: Safely removes entries from the main list.

---
Developed with ☕ and 🧠 by Gigio
