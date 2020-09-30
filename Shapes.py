# A program that a user can get the area of a rectangle by entering any desired length and width.

import math

class Rectangle:
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width

    def __area__(self):
        return 'Area = %r' % (self.length * self.width)

    def __perim__(self):
        return 'Perimeter = %r' % ((self.length)(2) + (self.width)(2))

class Square:
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = length

    def __area__(self):
        return 'Area = %r' % (self.length)(2)

    def __perim__(self):
        return 'Perimeter = %r' % (self.length)(4)

class Circle:
    def __init__(self, radius = 0, diameter = 0):
        self.radius = radius
        self.diameter = radius(2)

    def __area__(self):
        return 'Area = %r' % (math.pi * math.pow(self.radius, 2))

    def Circumf (self):
        return 'Circumference = %r' % (2 * math.pi * self.radius)
