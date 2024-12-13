#Write a function check if two strings are anagrams.

def are_anagrams(str1, str2):
    
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

   
    return sorted(str1) == sorted(str2)

# EXAMPLE
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("triangle", "integral"))  # True
print(are_anagrams("apple", "pale"))  # False
