#Create a class hierarchy for different shapes (circle, square, triangle).


class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * 3.14159 * self.radius, 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side ** 2, 2)

    def perimeter(self):
        return round(4 * self.side, 2)


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        # Using Heron's formula
        s = (self.side_a + self.side_b + self.side_c) / 2
        return round((s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5, 2)

    def perimeter(self):
        return round(self.side_a + self.side_b + self.side_c, 2)


def main():
    print("Choose a shape: Circle, Square, Triangle")
    shape_type = input("Enter shape: ").strip().lower()

    if shape_type == "circle":
        radius = float(input("Enter radius: "))
        shape = Circle(radius)

    elif shape_type == "square":
        side = float(input("Enter side length: "))
        shape = Square(side)

    elif shape_type == "triangle":
        side_a = float(input("Enter side A: "))
        side_b = float(input("Enter side B: "))
        side_c = float(input("Enter side C: "))
        shape = Triangle(side_a, side_b, side_c)

    else:
        print("Invalid shape!")
        return

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    main()
