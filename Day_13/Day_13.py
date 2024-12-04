#Write a program to find the largest of three numbers.

def find_largest(num1, num2, num3):
    """Function to find the largest of three numbers."""
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print("Enter three numbers:")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))

largest = find_largest(number1, number2, number3)
print(f"The largest number is: {largest}")
