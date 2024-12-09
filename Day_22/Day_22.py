#Write a function to remove duplicates from a list.

def remove_duplicates(lst):
    
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print("Original List:", my_list)
print("List without duplicates:", unique_list)
