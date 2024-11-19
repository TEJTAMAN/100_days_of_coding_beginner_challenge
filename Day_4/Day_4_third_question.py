'''3. Modify the 2nd question program to read decimal numbers as the length and width, and output the area to two decimal points'''


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

# Print the result
print("The area of the rectangle is:{:.2f}",format(area))

