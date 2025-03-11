#Build a basic CRUD (Create, Read, Update, Delete) application.


# Simple CRUD Application using Dictionary

data_store = {}  # Dictionary to store records

def create():
    key = input("Enter key: ")
    value = input("Enter value: ")
    data_store[key] = value
    print("Record added successfully!")

def read():
    if data_store:
        for key, value in data_store.items():
            print(f"{key}: {value}")
    else:
        print("No records found.")

def update():
    key = input("Enter key to update: ")
    if key in data_store:
        value = input("Enter new value: ")
        data_store[key] = value
        print("Record updated successfully!")
    else:
        print("Record not found!")

def delete():
    key = input("Enter key to delete: ")
    if key in data_store:
        del data_store[key]
        print("Record deleted successfully!")
    else:
        print("Record not found!")

# Menu-driven loop
while True:
    print("\n1. Create  2. Read  3. Update  4. Delete  5. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        create()
    elif choice == '2':
        read()
    elif choice == '3':
        update()
    elif choice == '4':
        delete()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again!")
