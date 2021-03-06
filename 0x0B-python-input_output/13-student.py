#!/usr/bin/python3
"""Module for Student Class"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Object Instantiation
          Args:
            first_name (string): First name of student
            last_name (string): Last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        Args:
            attrs: attributes list
        """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            attrsdict = {}
            for at in attrs:
                if at in self.__dict__:
                    attrsdict[at] = self.__dict__[at]
            return attrsdict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Loads attributes from json and replaces all attributes
        of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
