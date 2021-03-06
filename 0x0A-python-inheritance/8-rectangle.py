#!/usr/bin/python3
"""Module for Rectangle Class, contains BaseGeometry Class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle Class"""
    def __init__(self, width, height):
        """Rectangle Instantiation - Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
