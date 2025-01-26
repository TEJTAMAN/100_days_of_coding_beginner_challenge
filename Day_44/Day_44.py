#Create a class for a book with attributes like title and author.


class Book:
    """A simple class to represent a book."""

    def __init__(self, title, author):
        """Initialize the book with a title and author."""
        self.__title = title  # Private attribute
        self.__author = author  # Private attribute

    # Getter for the title
    def get_title(self):
        return self.__title

    # Setter for the title
    def set_title(self, title):
        if title.strip():
            self.__title = title
        else:
            print("Title cannot be empty.")

    # Getter for the author
    def get_author(self):
        return self.__author

    # Setter for the author
    def set_author(self, author):
        if author.strip():
            self.__author = author
        else:
            print("Author cannot be empty.")

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: '{self.__title}' by {self.__author}"


# Main program
def main():
    # Get user input for the book title and author
    title = input("Enter the book title: ").strip()
    author = input("Enter the book author: ").strip()

    # Create a Book object
    book = Book(title, author)

    # Display book details
    print("\nBook Details:")
    print(book)

    # Modify book details
    new_title = input("\nEnter a new title for the book: ").strip()
    book.set_title(new_title)

    new_author = input("Enter a new author for the book: ").strip()
    book.set_author(new_author)

    # Display updated book details
    print("\nUpdated Book Details:")
    print(book)


if __name__ == "__main__":
    main()
