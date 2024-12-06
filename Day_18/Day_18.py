#Write a function to find the sum of all elements in a list.


def sum_of_elements():
   
    input_list = list(map(float, input("Enter numbers separated by spaces: ").split()))
    total = sum(input_list)
    print("The sum of the elements is:", total)

sum_of_elements()
