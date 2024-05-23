#!/usr/bin/python3
"""
Module 10-square
Defines a Square class that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square
        """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
