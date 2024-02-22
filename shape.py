class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def calculate_area(self):
        return self.width ** 2

# Create instances for Rectangle and Square
rectangle = Rectangle(width=5, height=7)
square = Square(width=4, height=4)

# Calculate areas and print the results
print(f"Area of the Rectangle: {rectangle.calculate_area()}")
print(f"Area of the Square: {square.calculate_area()}")
