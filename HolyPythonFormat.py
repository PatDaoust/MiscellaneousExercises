# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:14:22 2021

@author: catal
"""

"""please see https://holypython.com/ for original exercises"""


"""
Place a curly bracket "{}" in the appropriate place
and fill inside .format()'s parenthesis so that "Hello!, Name" is printed.
"""


def printGreeting():
    """takes user input and prints a greeting"""
    name = input("Please enter your name: ")
    str = "Hello!, {}".format(name)
    print(str)


# printGreeting()

"""
Using a string and .format() method print the number: 1 only.
"""


def print1Only():
    print("{}".format(1))


print1Only()
