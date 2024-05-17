#!/usr/bin/python3
"""class Square that defines a square by: (based on 2-square.py)
"""


class Square:
    """The class Square.
    """

    def __init__(self, size=0):
        """Initailize the size.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square
        """

        return (self.__size ** 2)
