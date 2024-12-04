#Write a function to check if a given string is a palindrome.

def is_palindrome(s):
    
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
   
    return cleaned == cleaned[::-1]

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')


