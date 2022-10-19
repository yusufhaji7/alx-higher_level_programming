#!/usr/bin/python3
"""Defining a class Rectangle"""


class Rectangle:
    """
    attributes:
        width, height
    methods: 
        getter and setter methods for height and width
    """

    def __init__(self, width=0, height=0):
        """inistantiate width and height"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def width(self):
        """getter method to return width instance"""
        return self.__width
    def width(self, value):
        """setter method to set width to value"""
        self.__width = value
    def height(self):
        """getter method to return height instance"""
        return self.__height
    def height(self, value):
        """setter method to set height to value"""
        self.__height = value
