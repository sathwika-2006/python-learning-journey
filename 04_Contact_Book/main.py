print("WELCOME TO CONTACT BOOK")
contacts = [
   {"name": "Sach", "phone": "98765", "email": "sachie@gmail.com"},
   {"name": "dimpu",  "phone": "91234", "email": "dimpu@gmail.com"}
]


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email id: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)
    print("Contact added successfully!")


def view_contacts():
    if len(contacts)==0:
        print("No contacts found")
    else:
        for contact in contacts:
            print("\nName :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("--------------------")

def search_contact():
    search_name = input("Enter name to search: ")
    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("\nContact Found ✅")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True
            break
    if found == False:
        print("Contact not found")

def delete_contact():
    delete_name=input("Enter contact name to delete: ")
    found=False

    for contact in contacts:
        if contact["name"].lower() == delete_name.lower():
            contacts.remove(contact)
            print("\n Contact deleted sucessfully")
            found=True
            break
    if found==False:
        print("Contact not found")
        

while True:
    print("1.Add Contact\n")
    print("2.View All Contacts\n")
    print("3.Search Contact\n")
    print("4.Delete Contact\n")
    print("5.Exit")

    choice=input("Please enter your choice: ")
    if choice=="1":
        add_contact()

    elif choice=="2":
        view_contacts()
    
    elif choice=="3":
        search_contact()

    elif choice=="4":
        delete_contact()

    elif choice == "5":
        print("Thank you for using Contact Book")
        break

    else:
        print("Ivalid choice")

