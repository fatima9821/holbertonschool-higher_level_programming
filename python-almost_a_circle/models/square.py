#!/usr/bin/python3
"""
module inherits from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class represent the square """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize an square with size specifice
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return a string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
