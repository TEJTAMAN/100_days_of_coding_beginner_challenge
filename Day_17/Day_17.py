#Write a function to count the number of vowels in a string.

def count_vowels(string):
    """
    Count the number of vowels in a given string.

    Parameters:
    string (str): The input string.

    Returns:
    int: The count of vowels in the string.
    """
    vowels = "aeiou"  
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ").lower()
vowel_count = count_vowels(user_input)
print(f"Number of vowels in the string: {vowel_count}")
