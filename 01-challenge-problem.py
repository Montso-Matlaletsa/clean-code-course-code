class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, starting_point, width, height):
        self.starting_point = starting_point
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def print_coordinates(self):
        top_right = self.starting_point.x + self.width
        bottom_left = self.starting_point.y + self.height
        print('Starting Point (X)): ' + str(self.starting_point.x))
        print('Starting Point (Y)): ' + str(self.starting_point.y))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def createRectangle():
    rectangle_starting_point = Point(50, 100)
    rectangle = Rectangle(rectangle_starting_point , 90, 10)

    return rectangle


rectangle =createRectangle()

print(rectangle.getArea())
rectangle.print_coordinates()
