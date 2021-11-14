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

"""


def caseInsensitiveStringMatch(string1, string2):
    """assumes string1 and string 2 are strings
    returns a boolean, True if string1 and string2 match irrespective of case,
    else False
    """
    return string1.lower() == string2.lower()


# print(caseInsensitiveStringMatch('nice', 'nice'))  # expect True
# print(caseInsensitiveStringMatch('Hi there', 'hi there'))  # expect True
# print(caseInsensitiveStringMatch('GoOd DaY', 'gOOd dAy'))  # expect True
# print(caseInsensitiveStringMatch('foo', 'food'))  # expect False


"""
Q2c) Returns True/False - two strings are anagrams
    (assume input consists of alphabets only)
"""


def isAnagram(string1, string2):
    """assumes string1 and string2 are string of alphabetical chars of any case
    returns a boolean, True is string1 and string2 are casse insensite anagrams
    else False
    """
    return sorted(string1.lower()) == sorted(string2.lower())


# print(isAnagram('god', 'Dog'))  # expect True
# print(isAnagram('beat', 'table'))  # expect False
# print(isAnagram('Tap', 'paT'))  # expect True
# print(isAnagram('beat', 'abet'))  # expect True


"""
Q2d)  Returns corresponding integer or floating-point number
"""


def floatConverter(num):
    """assumes num is an int, float, or string representing a number
    returns a float, representing num"""
    if isinstance(num, float) or isinstance(num, int) or isinstance(num, str):
        return float(num)
    else:
        raise TypeError("not a valid input")


# print(floatConverter(3))  # expect 3
# print(floatConverter(0x1f))  # expect 31
# print(floatConverter(3.32))  # expect 3.32
# print(floatConverter('123'))  # expect 123
# print(floatConverter('-78'))  # expect -78
# print(floatConverter(" 42  \n "))  # expect 42
# print(floatConverter('3.982e5'))  # expect 398200.0
# print(floatConverter(['1', '2.3']))  # expect TypeError: not a valid input
# print(floatConverter('foo'))  # expect ValueError: could not convert string to float
