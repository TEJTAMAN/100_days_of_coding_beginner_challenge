#Use class decorators in Python.


def log_methods(cls):
    """Class decorator to log method calls."""
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)

        def __getattr__(self, name):
            attr = getattr(self.instance, name)
            if callable(attr):
                def logged_method(*args, **kwargs):
                    print(f"Calling method: {name} with arguments {args}, {kwargs}")
                    result = attr(*args, **kwargs)
                    print(f"Method {name} returned: {result}")
                    return result
                return logged_method
            return attr

    return Wrapper

@log_methods
class Book:
    """A simple Book class with a class decorator."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        """Returns book details."""
        return f"'{self.title}' by {self.author}"

# Example usage
book = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(book.get_details())  # The method call is logged
