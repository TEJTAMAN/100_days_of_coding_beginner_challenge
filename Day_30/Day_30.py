#Sort a list of numbers in ascending order.

#Getting inputs from the user as list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

#using the sort operator to sort the numbers into ascending order
numbers.sort()

#Displaying the sorted list
print("Sorted list in ascending order:", numbers)

