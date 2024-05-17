#!/usr/bin/python3
"""Square that based on 1-square.py
"""


class Square:
    """The Square class.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance with a given size.

        Args:
            size (int): The size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        # Private attibut to store the size
        self.__size = size
