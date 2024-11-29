#Write a program to check if a number is even or odd.

number = int(input("Enter a number: "))
print(f"{number} is {'even' if number % 2 == 0 else 'odd'}.")
