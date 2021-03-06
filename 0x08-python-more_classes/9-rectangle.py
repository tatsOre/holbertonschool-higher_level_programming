#!/usr/bin/python3
"""Module for Rectangle Class"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    """(int) number of active instances"""
    print_symbol = '#'
    """Used as symbol for string representation. Can be any type"""

    def __init__(self, width=0, height=0):
        """Constructor
        Args:
            width (int): width of a rectangle
            height (int): length of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        Returns a printable string representation of an object
        """
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_symbol) * self.__width + '\n') *
                self.__height)[:-1]

    def __repr__(self):
        """
        Returns official string representation of an object
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes a instance-object - Finalizer
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares two Rectangle instances
        Args:
            (Rectangle)rect_1 - Rectangle instance No. 1
            (Rectangle)rect_2 - Rectangle instance No. 2
        Raises:
            TypeError: if rect_1 or rect_2 are not instances of Rectangle
        Returns:
            biggest rectangle based on the area, or rect_1 if both have
            the same area value
        """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance as square
        Args:
        (int)size of the square == width == height == size
        """
        return cls(size, size)
