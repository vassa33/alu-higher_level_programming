#!/usr/bin/python3
"""defines a Square class"""


import math
"""imports the math module"""


class MagicClass:
    """
    defines a circle
    """

    def __init__(self, radius=0):
        """
        initializes the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        returns area of circle
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        returns circumference of circle
        """
        return 2 * math.pi * self.__radius
