"""
many thanks to github.com/learnbyexample for these exercises
full exercises at https://github.com/learnbyexample/Python_Basics/blob/master/Exercises.md
"""

"""
Q1a) Ask user information, for ex: name, department, college etc
and display them using print function
"""


def userDetailsCollector():
    """prints out details the user inputs"""
    print("Please provide the following details")
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    college = input("Enter your college: ")
    print(f"Name       : {name}")
    print(f"College    : {college}")
    print(f"Department : {department}")


# userDetailsCollector()


"""
Q2a Returns length of integer numbers
"""


def integerLenght(num):
    """assumes num is an integer
    returns an int, representing the lenght of num"""
    if not isinstance(num, int):
        raise TypeError("provide only integer input")
    num_str = str(num)
    lenght = len(num_str)
    if num_str[0] == "-":
        lenght -= 1
    return lenght


# print(integerLenght(42))  #expected 2
# print(integerLenght(962306349871524124750813401378124))   #expected 33
# print(integerLenght(+42))  #expected 2
# print(integerLenght(-42))  #expected 2
# print(integerLenght("a"))  #expected TypeError
# print(integerLenght(2.4))  #expected TypeError

"""
Q2b) Returns True/False - two strings are same irrespective of lowercase/uppercase

>>> str_cmp('nice', 'nice')
True
>>> str_cmp('Hi there', 'hi there')
True
>>> str_cmp('GoOd DaY', 'gOOd dAy')
True
>>> str_cmp('foo', 'food')
False
"""


def caseInsensitiveStringMatch():
    pass
