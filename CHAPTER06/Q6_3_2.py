class Rectangle:
    angle = 90

    def __init__(self, width, height):
        self.name = "rectangle"
        self.width = width
        self.height = height
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_perimeter(self):
        return (self.width + self.height) * 2

    def calc_area(self):
        return self.width * self.height

    def show_attributes(self):
        print("name: {}, width: {}, height: {}, angle: {}".format(self.name, self.width, self.height, self.angle))
        print("perimeter: {}, area: {}".format(self.perimeter, self.area))


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "square"


r1 = Rectangle(4, 3)
r1.show_attributes()
s1 = Square(4)
s1.show_attributes()

