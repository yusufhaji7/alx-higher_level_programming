#!/usr/bin/python3
"""
creating a class called Base.
"""


class Base:
    """class attribute:
        __nb_objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor with attribute ID"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
