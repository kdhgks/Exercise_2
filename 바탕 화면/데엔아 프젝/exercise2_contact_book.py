contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts saved.")
        return
    print("=== Contact List ===")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def save_contacts(file_path="contacts.txt"):
    with open(file_path, "w", encoding="utf-8") as f:
        for name, phone in contacts.items():
            f.write(f"{name},{phone}")
    print("Contacts saved.")

def load_contacts(file_path="contacts.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass

def main():
    load_contacts()
    while True:
        print("1) Add Contact")
        print("2) View Contacts")
        print("3) Search Contact")
        print("4) Quit")
        choice = input("Select an option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            save_contacts()
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
