#!/usr/bin/python3
"""A SubClass"""
from models.base import Base


class Rectangle(Base):
    """ A rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle object constructor
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Get width method/attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get height method/attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set attribute for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get x method/attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """ Set attribute for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get height method/attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """ Set attribute for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """ display # character"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"
