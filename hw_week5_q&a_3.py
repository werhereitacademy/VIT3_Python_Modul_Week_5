class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def cal_area(self):
        return self.width * self.height


class Rectangle(Shape):
    pass


class Square(Shape):
    def cal_area(self):
        if self.width == self.height:
            return self.width ** 2
        else:
            return 'This is not a square!'


if __name__ == '__main__':
    r1 = Rectangle(5, 6)
    sq1 = Square(5, 6)
    sq2 = Square(7, 7)

    print(f'The area of the rectangle named r1 is: {r1.cal_area()}')

    print(f'The area of the square named sq1 is  : {sq1.cal_area()}')

    print(f'The area of the square named sq2 is  : {sq2.cal_area()}')
