# Handle exceptions for file not found.


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found in the system.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# EXAMPLE
file_path = "example.txt"
read_file(file_path)
