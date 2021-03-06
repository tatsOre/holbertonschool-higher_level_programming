#!/usr/bin/python3
"""Module for Rectangle Class"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Constructor
        Args:
            width (int): width of a rectangle
            height (int): length of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property for width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Property for height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter of a rectangle"""
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2
