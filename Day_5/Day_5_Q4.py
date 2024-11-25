'''4. Write a program that reads the percentage and then prints their corresponding letter grade (A, B, C, D, or F)'''


percentage = float(input("Enter the percentage: "))


if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'


print(f"The letter grade is: {grade}")
