# Question 3: Create a "Shape" class. Under this class, create two subclasses, "Rectangle" and "Square".

# The "Shape" class should have two properties: "width" and "height."
# The "Rectangle" class should inherit from the "Shape" class and additionally add a method called "calculate_area()."
# The "Square" class should also inherit from the "Shape" class and calculate the area of the square using the same "calculate_area()" method.
# Create an instance of a "Rectangle" and a "Square", specify their width and height for each, and print out their areas by calculating them.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area_calculator(self):
        area = self.width * self.height
        return area

class Rectangle(Shape):
    shape_type = "rectangle"
    def __init__(self, width, height):
        super.__init__(self, width, height)

class Square(Shape):
    shape_type = "square"
    def __init__(self, side):
        super.__init__(self, side)

shape = Shape(10, 20)
print("Area: ", shape.calculate_area())
rectangle = Rectangle(30, 40)
print("Area: ", rectangle.calculate_area())
print("Shape type: ", rectangle.shape_type) #rectangle.shape_type

square = Square(20)
print("Area: ", square.calculate_area())
print("Shape type: ", square.shape_type) #square.shape_type