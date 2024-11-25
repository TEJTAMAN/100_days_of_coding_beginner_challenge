#Write a program that takes radius of the circle and outputs the area of the circle to 2 decimal digits


radius = float(input("Enter the radius of the circle: "))

if radius < 0:
    print("Radius cannot be negative. Please enter a positive value.")
else:
    area_of_the_circle = 3.14 * radius ** 2
    print(f"The area of the circle is: {area_of_the_circle:.2f}")
