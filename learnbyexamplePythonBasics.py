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


"""Q3a) Write a function that returns

'Good' for numbers divisible by 7
'Food' for numbers divisible by 6
'Universe' for numbers divisible by 42
'Oops' for all other numbers
Only one output, divisible by 42 takes precedence

bonus: use a loop to print number and corresponding string for numbers 1 to 100

"""


def sixBySeven(num):
    """assumes num is an integer
    returns a string
    if num is divisible by 42, returns "universe"
    elif num is divisible by 6, returns "food"
    elif num is divisible by 7, returns "good"
    else returns "oops"
    """
    if num % 42 == 0:
        return "universe"
    elif num % 6 == 0:
        return "food"
    elif num % 7 == 0:
        return "good"
    else:
        return "oops"


# print(sixBySeven(66))  # expect "food"
# print(sixBySeven(13))  # expect "oops"
# print(sixBySeven(42))  # expect "universe"
# print(sixBySeven(14))  # expect "good"
# print(sixBySeven(84))  # expect "universe"
# print(sixBySeven(235432))  # expect "oops"


def sixBySevenSequence(lower_limit, upper_limit):
    """assumes lower_limit is an int, representing the smallest number to test
    assumes upper_limit is an int, representing the largest number to test
    prints the result of sixBySeven()
    for each number in the ranger lower_limit to upper_limit, inclusive
    """
    for num in range(lower_limit, upper_limit + 1):
        print(str(num) + " " + sixBySeven(num))


# sixBySevenSequence(1, 100)


"""
Q3b) Print all numbers from 1 to 1000 which reads the same in reversed form
    in both binary and decimal format

bonus: add octal and hexadecimal checks as well
"""


def isDecimalPalindrome(num):
    """assumes num is an integer
    returns True if num in decimal form is a palindrome, else False"""
    return str(num) == str(num)[::-1]


# print(isDecimalPalindrome(1))  # expect True
# print(isDecimalPalindrome(2))  # expect True
# print(isDecimalPalindrome(99))  # expect True
# print(isDecimalPalindrome(100))  # expect False


def isBinaryPalindrome(num):
    """assumes num is an integer
    returns True if num in binary form is a palindrome, else False"""
    return str(bin(num))[2::] == str(bin(num))[:1:-1]


# print(isBinaryPalindrome(1))  # expect True
# print(isBinaryPalindrome(2))  # expect False
# print(isBinaryPalindrome(99))  # expect True
# print(isBinaryPalindrome(100))  # expect False


def isOctalPalindrome(num):
    """assumes num is an integer
    returns True if num in octal form is a palindrome, else False"""
    return str(oct(num))[2::] == str(oct(num))[:1:-1]


# print(isOctalPalindrome(1))  # expect True
# print(isOctalPalindrome(2))  # expect True
# print(isOctalPalindrome(99))  # expect False
# print(isOctalPalindrome(100))  # expect False
# print(isOctalPalindrome(585))  # expect True


def isHexadecimalPalindrome(num):
    """assumes num is an integer
    returns True if num in hexadecimal form is a palindrome, else False"""
    return str(hex(num))[2::] == str(hex(num))[:1:-1]


# print(isHexadecimalPalindrome(1))  # expect True
# print(isHexadecimalPalindrome(2))  # expect True
# print(isHexadecimalPalindrome(34))  # expect True
# print(isHexadecimalPalindrome(99))  # expect False
# print(isHexadecimalPalindrome(100))  # expect False
# print(isHexadecimalPalindrome(585))  # expect False


def decimalAndBinaryPalindromes():
    """prints the decimal and binary form of numbers 1-1000 which
    are palindromes in both decimal and binary format"""
    for num in range(1, 1001):
        if isBinaryPalindrome(num) and isDecimalPalindrome(num):
            print(num, bin(num))


# decimalAndBinaryPalindromes()


def decimalBinaryOctalPalindromes():
    """prints the decimal, binary, and octal form of numbers 1-1000 which
    are palindromes in decimal, binary, and octal format"""
    for num in range(1, 1001):
        if isBinaryPalindrome(num) and isDecimalPalindrome(num) and\
                isOctalPalindrome(num):
            print(num, bin(num), oct(num))


# decimalBinaryOctalPalindromes()


def decimalBinaryOctalHexaPalindromes():
    """prints the decimal, binary, octal, and hexadecimal form of numbers 1-1000 which
    are palindromes in decimal, binary, octal, and hexadecimal format"""
    for num in range(1, 1001):
        if isBinaryPalindrome(num) and isDecimalPalindrome(num) and\
                isOctalPalindrome(num) and isHexadecimalPalindrome(num):
            print(num, bin(num), oct(num), hex(num))


# decimalBinaryOctalHexaPalindromes()


"""
Q4a) Write a function that returns product of all numbers of a list
bonus: works on any kind of iterable
"""


def listProduct(an_iterable):
    """assumes an_iterable is an iteraqble of numerics
    returns a numeric, the product of the elements of a_list"""
    # innitialize product variable
    product = 1
    # multiply by elements of iterables
    for num in an_iterable:
        product *= num
    return product


# print(listProduct([1, 4, 21]))  # expect 84
# print(listProduct([-4, 2.3e12, 77.23, 982, 0b101]))  # expect -3.48863356e+18
# print(listProduct((-3, 11, 2)))  # expect -66
# print(listProduct({8, 300}))  # expect 2400
# print(listProduct([234, 121, 23, 945, 0]))  # expect 0
# print(listProduct(range(2, 6)))  # expect 120


"""
Q4b) Write a function that returns nth lowest number of a list (or iterable in general).
Return the lowest if second argument not specified

if a list contains duplicates, they should be handled before determining nth lowest
"""


def returnNthElement(an_iterable, n=1):
    """assumes an_iterable is an iterable, containing at least n elements
    assumes n is an integer, representing which element is to be returned
    default n is 1, representing the lowest elements
    ignores repeated values
    returns an element of an_iterable
    """
    return sorted(set(an_iterable))[n-1]


# nums1 = [42, 23421341, 234.2e3, 21, 232, 12312, -2343]
# print(returnNthElement(nums1))  # expect -2343
# print(returnNthElement(nums1, 3))  # expect 42
# print(returnNthElement(nums1, n=5))  # expect  12312
# print(returnNthElement(nums1, n=15))  # expect IndexError

# nums2 = [1, -2, 4, 2, 1, 3, 3, 5]
# print(returnNthElement(nums2))  # expect -2
# print(returnNthElement(nums2, 4))  # expect 3
# print(returnNthElement(nums2, 5))  # expect 4

# print(returnNthElement('unrecognizable', 3))  # expect "c"
# print(returnNthElement('abracadabra', 4))  # expect "d"
