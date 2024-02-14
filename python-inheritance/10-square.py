#!/usr/bin/python3
"""
define a square class that inherit
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class rectangle """
    def __init__(self, size):
        """ initialize a square with a given size """
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ calculate the area of the square """
        return self.__size ** 2
