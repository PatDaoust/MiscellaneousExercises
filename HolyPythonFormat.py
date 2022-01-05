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


# scores()

"""Exercise 2-a: Join method of strings w/lists"""


def joinList():
    """prints a list of strings"""
    lst = ["Hawaii", "Phuket", "Aruba", "Keys"]
    # Type your answer here
    joined = "+++".join(lst)
    print(joined)


# joinList()


"""Exercise 2-b: Join method of strings w/tuples"""


def joinTuples():
    """prints this email address"""
    addresses = ("Mr.Hathaway", "amymail.com")
    # Type your code here.
    email = "@".join(addresses)
    print(email)


# joinTuples()

""""Exercise 2-c: Join method with a special character " " """


def joinSpace():
    """print elements of list with space in between"""
    lst = ['Everything', 'has', 'beauty,', 'but', 'not', 'everyone', 'can', 'see.']
    # Type your code here
    str = " ".join(lst)
    print(str)


# joinSpace()


"""Exercise 2-d: Join method of strings w/dictionaries"""


def joinDict():
    """prints keys and values in dict"""
    economic_growth = {"India": 7.0,
                       "Cambodia": 7,
                       "Tanzania": 6.9,
                       "Bangladesh": 6.6,
                       "Senegal": 6.6}
    # Type your code here
    str = ",".join(economic_growth)
    print(str)


# joinDict()


"""Exercise 2-e: Python join method with new line character"""


def joinEscapeReturn():
    """prints elements of list with return"""
    poem_lst = ["Not enjoyment, and not sorrow,",
                "Is our destined end or way;",
                "But to act, that each tomorrow",
                "Find us farther than today."]
    # Type your code here.
    poem_str = "\n".join(poem_lst)
    print(poem_str)


# joinEscapeReturn()

"""Exercise 3-a: Splitting Up Words Using Split Method"""


def splitString():
    """prints a list"""
    # Type your answer here.
    stra = "Hello World!"
    lst = stra.split()
    print(lst)


# splitString()

"""Exercise 3-b: Splitting based on a specific character (:) split method"""


def splitOnChar():
    stra = "101:102:103:201:202"
    # Type your code here.
    lst = stra.split(":")
    print(lst)


# splitOnChar()

"""Exercise 3-c: Splitting based on special character (;)"""


def splitOnChar2():
    stra = "Arsenal:0-Chelsea:1;Barcelona:2-Bayern Munich:2"
    # Type your code here.
    lst = stra.split(";")
    ans_1 = lst[-1]
    print(ans_1)


# splitOnChar2()


"""Exercise 4-a: Strip method to remove whitespace on both sides"""


def stripWhitespace():
    stra = "     Hello World!   "
    # Type your answer here.
    stra = stra.strip()
    print(stra)


# stripWhitespace()


"""Exercise 4-b: Strip method to remove specific characters from a string"""


def stripBabylon():
    a_str = "#$^&#@%$& Babylon #@$&@#"
    # Type your code here.
    a_str = a_str.strip("#$^&#@%$& ")
    print(a_str)


# stripBabylon()


"""Exercise 4-c: Rstrip method to remove from the right side only"""


def stripRight():
    a_str = "@Bloomberg@@@@@###"
    a_str = a_str.rstrip("@#")

    print(a_str)


# stripRight()


"""Exercise 4-d: Lstrip method to remove from the left side only"""


def stripLeft():
    a_str = "......Macroeconomics,...........Derivatives"

    a_str = a_str.split(",")
    ans_1 = a_str[1].lstrip(".,")

    print(ans_1)


# stripLeft()


"""Exercise 5-a"""


def methodsAndAttributes():
    str = "Hello World!"
    print(dir(str))


# methodsAndAttributes()


"""Exercise 5-b print the attributes and methods of a list"""


def printAttributes():
    lst = list()
    print(dir(lst))


# printAttributes()


"""Exercise 5-c print the attributes and methods of a dict"""


def printAttributesDict():
    print(dir(dict()))


# printAttributesDict()


"""Exercise 6-a Print 5 by accessing the nested data."""


def print5():
    nested_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ans_1 = nested_lst[1][1]
    print(ans_1)


# print5()


"""Exercise 6-b Print "Z" from the nested data."""


def printZ():
    nested_lst = [["Hat", "Glove", "Goggle"], ["Button", "Zipper", "Hook"]]
    ans_1 = nested_lst[1][1][0]
    print(ans_1)


# printZ()


"""Exercise 6-c What color is the violet?"""


def violetColor():
    nested_lst = [{"orange": "orange"}, {"rose": "red"}, {"violet": "blue"}]
    ans_1 = nested_lst[2]["violet"]
    print(ans_1)


violetColor()
