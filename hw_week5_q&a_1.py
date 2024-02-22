class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def area(self):
        return self.width * self.height


if __name__ == '__main__':
    r1 = Rectangle(5, 7)

    print(f'The perimeter of the rectangle named r1 is: {r1.perimeter()}')

    print(f'The area of the rectangle named r1 is     : {r1.area()}')

