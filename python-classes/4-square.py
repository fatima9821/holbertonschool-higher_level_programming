#!/usr/bin/python3
"""class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """The class Square.
    """

    def __init__(self, size=0):
        """Initailize the size.
        """

        self.size = size

    @property
    def size(self):
        """Getter method for retreiving the size
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method for setting the size.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square
        """

        return (self.__size ** 2)
