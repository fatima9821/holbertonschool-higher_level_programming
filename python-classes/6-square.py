#!/usr/bin/python3
"""class Square that defines a square by: (based on 4-square.py)
"""


class Square:
    """The class Square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initailize the size and position.

        Args:
            size (int): The size of the square.
            position (tuple): the position of the square.
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method for retreiving the position.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for setting the position.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.
        """

        return (self.__size ** 2)

    def my_print(self):
        """Print the square using '#' character.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
