#!/usr/bin/python3
"""contains class BaseGeometry"""


class BaseGeometry:
    """defines class BaseGeometry"""
    
    def __init__(self, area):
        """initializes area"""
        self.area = area
        pass
    
    def area(self):
        """raises exception"""
        raise Exception('area() is not implememented')
