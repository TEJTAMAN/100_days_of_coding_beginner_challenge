#Write a function to reverse a list.

def reverse_list(lst):
   
    return lst[::-1]

my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print("Original List:", my_list)
print("Reversed List:", reversed_list)
