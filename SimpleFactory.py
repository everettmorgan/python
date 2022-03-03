import math


class Shape:
    def area(self):
        raise Exception('Shape must implement area()!')


class Square(Shape):
    def __init__(self, length, width):
        Shape.__init__(self)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class ShapeFactory:
    def get_shape(self, shape, *args):
        if shape == 'SQUARE':
            return Square(*args)
        elif shape == 'CIRCLE':
            return Circle(*args)


if __name__ == '__main__':
    factory = ShapeFactory()

    square = factory.get_shape('SQUARE', 3, 3)
    circle = factory.get_shape('CIRCLE', 34)

    print(square.area())
    print(circle.area())
