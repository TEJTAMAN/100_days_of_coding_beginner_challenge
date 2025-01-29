#Implement polymorphism with a shape area calculator.


import math

class Shape:
    
    def area(self):
       
        pass

class Circle(Shape):
   
    def __init__(self, radius):
        self.radius = radius

    def area(self):
       
        return math.pi * self.radius ** 2

class Rectangle(Shape):
   
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
       
        return self.length * self.width

class Triangle(Shape):
   
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        
        return 0.5 * self.base * self.height

# Function to get user input and calculate area
def main():
    print("Shape Area Calculator")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Choose a shape (1-3): ").strip()

    if choice == "1":
        radius = float(input("Enter the radius of the circle: ").strip())
        shape = Circle(radius)

    elif choice == "2":
        length = float(input("Enter the length of the rectangle: ").strip())
        width = float(input("Enter the width of the rectangle: ").strip())
        shape = Rectangle(length, width)

    elif choice == "3":
        base = float(input("Enter the base of the triangle: ").strip())
        height = float(input("Enter the height of the triangle: ").strip())
        shape = Triangle(base, height)

    else:
        print("Invalid choice!")
        return

    print(f"The area of the shape is: {shape.area():.2f}")

if __name__ == "__main__":
    main()
