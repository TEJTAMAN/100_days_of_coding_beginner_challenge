#Write a function to find the maximum element in a list.

def find_max_element():
    
    input_list = list(map(float, input("Enter numbers separated by spaces: ").split()))
    if not input_list:
        print("The list is empty.")
        return
    max_value = max(input_list)
    print("The maximum element is:", max_value)

find_max_element()
