#2. Write a program that generates random number between 2 integers



import random

num1 = int(input("Enter the starting integer: "))
num2 = int(input("Enter the ending integer: "))

random_number = random.randint(num1, num2)

print(f"The random number between {num1} and {num2} is: {random_number}")
