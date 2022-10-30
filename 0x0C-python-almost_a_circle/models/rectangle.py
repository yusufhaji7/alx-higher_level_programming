#!/usr/bin/python3
"""
creating a class called rectangle that inherites from base class
"""


from models.base import Base

class Rectangle(Base):
    """
    private instances:
        __width
        __height
        __x
        __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor to initialize width, height, x and y"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def width(self):
        return self.__width
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <=0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def height(self):
        return self.__height

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def x(self):
        return self.__x

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def y(self):
        return self.__y

    def area(self):
        return self.__width * self.__height
