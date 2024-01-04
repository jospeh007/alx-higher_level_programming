#!/usr/bin/python3
"""
Display a Rectangle
"""



class Rectangle:
    """Display of a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes of the rectangle"""
        self.height = height
        self.width = width
    @property
    def width(self):
        """The private instance attribute width"""
        return self.__width
    @width.setter
    def width(self, value):
        """The private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """The private instance attribute height"""
        return self.__height
    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
