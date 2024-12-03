#Write a function to check if a given string is a palindrome.

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is the same when reversed
    return cleaned == cleaned[::-1]

# Input a string
input_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')


