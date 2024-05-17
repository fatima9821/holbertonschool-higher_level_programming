#!/usr/bin/python3
"""Square class with a private size attribute
"""


class Square:
    """Square class with a private size attribute.

    Attributes:
        size.

    Methods:
        init.
    """

    def __init__(self, size):
        """Initialize a new Square instance with a given size."""
        self.__size = size
