#!/usr/bin/python3
"""
class of Mylist
"""


class MyList(list):
    """ mylist class """

    def print_sorted(self):
        """ print list """

        sorted_list = sorted(self)
        print(sorted_list)
