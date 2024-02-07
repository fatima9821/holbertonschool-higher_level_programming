#!/usr/bin/python3
"""
This module define an empty square
"""


class Square:
    """
    This class represents a square.
    """
    def __init__(self, size=0):

        """
        Check if the size is an integer
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """
        check if size is egale to zero
        """

        if size < 0:
            raise TypeError("size must be >= 0")
        """
        attribute private for stock a size of square
        """

        self.__size = size
