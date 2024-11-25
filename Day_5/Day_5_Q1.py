'''1. Write a program that reads an integer as user input and prints whether the number is Odd or Even to the console'''


number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(f"The number {number} is Even.")
else:
    print(f"The number {number} is Odd.")
