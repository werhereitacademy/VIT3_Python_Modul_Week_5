class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.boy = height

    def perimeter(self):
        return self.width * 2 + self.boy * 2

    def area(self):
        return self.width * self.boy


if __name__ == '__main__':
    r1 = Rectangle(5, 7)

    print(f'Perimeter of rectangle named r1 is: {r1.perimeter()}')

    print(f'Area of rectangle named r1 is: {r1.area()}')
