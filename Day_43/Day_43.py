#Implement encapsulation in a class.

"""Encapsulation ensures that sensitive data is hidden from direct access and can only be modified through specific methods."""

class Student:
    """A simple class demonstrating encapsulation with user input."""

    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        if name.strip():
            self.__name = name
        else:
            print("Name cannot be empty.")

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:  # Validate age
            self.__age = age
        else:
            print("Age must be positive.")

# Main program
def main():
    # Get user input for name and age
    name = input("Enter the student's name: ").strip()
    while True:
        try:
            age = int(input("Enter the student's age: ").strip())
            if age > 0:
                break
            else:
                print("Age must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid age.")

    # Create a Student object
    student = Student(name, age)

    # Display student details
    print("\nStudent Details:")
    print(f"Name: {student.get_name()}")
    print(f"Age: {student.get_age()}")

    # Modify student details
    new_name = input("\nEnter a new name for the student: ").strip()
    student.set_name(new_name)

    while True:
        try:
            new_age = int(input("Enter a new age for the student: ").strip())
            if new_age > 0:
                student.set_age(new_age)
                break
            else:
                print("Age must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid age.")

    # Display updated details
    print("\nUpdated Student Details:")
    print(f"Name: {student.get_name()}")
    print(f"Age: {student.get_age()}")

if __name__ == "__main__":
    main()
