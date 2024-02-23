# Question 1: Create a Python class named "Rectangle" representing a rectangle. The Rectangle class should have the following properties and methods:

# Properties:

# width (an integer)
# height (an integer)
# Methods:

# area(self): A method that calculates and returns the area of the rectangle.
# perimeter(self): A method that calculates and returns the perimeter of the rectangle.
# Create an instance of the Rectangle class, set its width to 5 and height to 7, then print out its area and perimeter.

class Rectangle:
    def __init__(self, short_side, long_side):
        self.short_side = short_side
        self.long_side = long_side
    
    def area(self, short_side, long_side):
        area = short_side * long_side
        return area
    
    def perimeter(self, short_side, long_side):
        perimeter = (short_side + long_side) * 2
        return perimeter

short_side = int(input("Enter the short side of the rectangle: "))
long_side = int(input("Enter the long side of the rectangle: "))

rectangle = Rectangle(short_side, long_side)
print(rectangle.area(short_side, long_side))
print(rectangle.perimeter(short_side, long_side))
