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

"""Using a string and .format() method print the number: 1"""


def print1Only():
    """print '1' """
    string = "{}".format(1)
    print(string)


# print1Only()

"""
using a string and .format() method and three curly brackets, print the numbers:
    1, 2, 3 each separated with a comma.
"""


def print123():
    """prints '1, 2, 3' """
    string = "{}, {}, {}".format(1, 2, 3)
    print(string)


# print123()

"""Fill in the values for months, weeks and days accordingly."""


def monthsWeeksDays():
    """print 'One year has 12 months, 52 weeks and 365 days.' """
    str = "One year has {} months, {} weeks and {} days.".format(12, 52, 365)
    print(str)


# monthsWeeksDays()


"""
You can also use indexing inside your curly brackets so that you will decide
the position instead of a default order.

By filling inside the curly brackets,
make sure each bracket is matched to the appropriate value.
"""


def monthsWeeksDaysv2():
    """print 'One year has 12 months, 52 weeks and 365 days.' """
    str = "One year has {2} months, {0} weeks and {1} days.".format(52, 365, 12)
    print(str)


# monthsWeeksDaysv2()

"""Fill inside .format()'s parenthesis so that it matches the correct values."""


def scores():
    John = 75
    Ann = 80
    Ally = 60
    str1 = "Scores were as following: John:{}, Ann:{}, Ally:{}"

    # Type your code here.
    str2 = str1.format(John, Ann, Ally)
    print(str2)


scores()
