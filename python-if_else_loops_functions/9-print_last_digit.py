#!/usr/bin/python3
def print_last_digit(number):
    numer = abs(number)
    ld = number % 10
    print("{:d}".format(ld), end="")
    return ld
