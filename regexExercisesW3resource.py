# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 13:07:00 2022

@author: catal
"""
import re
import pdb

string1 = "His fingers rippled down Bran's cock, and Bran jerked his hips again, impaling himself on the three fingers with a groan."

string2 = "His master broke the kiss lingeringly and kissed down the line of his neck; at a bite to the hollow of his throat, Bran's hips jerked against his master's pelvis, his cock now fully hard."

string3 = "Bran curled in an unobtrusive corner of the sofa; his first night he had sat there frozen, trying to watch everyone at once to figure out what direction the danger would come from, but tonight he was content to sit, ignored, and watch the changing expressions on his master's face."

string4 = "abc"

"""
regex exercises from https://www.w3resource.com/python-exercises/re/
solutions by Pat Daoust
"""

"""
1. Write a Python program to check that a string contains only a certain set of characters
(in this case a-z, A-Z and 0-9).
"""


def containsAlphaNumeric(a_string):
    """Assumes a_string is a string
    returns a boolean, True if a_string contains only alphanumeric characters
    (a-z, A-Z and 0-9), else False
    """
    regex = "[a-zA-z0-9]+"
    results = re.search(regex, a_string)
    return bool(results)


def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)


# print("my results: ")
# print(containsAlphaNumeric("ABCDEFabcdef123450"))
# print(containsAlphaNumeric("*&%@#!}{"))
# print(" ")
# print("expected results: ")
# print(is_allowed_specific_char("ABCDEFabcdef123450"))
# print(is_allowed_specific_char("*&%@#!}{"))

"""
2. Write a Python program that matches a string that has an a followed by zero or more b's
"""


def aThenMaybeB(a_string):
    """Assumes a_string is a string
    returns a boolean, True is a_string contains n a followed by zero or more b's
    else False
    """
    regex = "ab*"
    results = re.search(regex, a_string)
    return bool(results)


# print(aThenMaybeB("a"))
# print(aThenMaybeB("ab"))
# print(aThenMaybeB("abacus"))
# print(aThenMaybeB("string1"))

"""
3. Write a Python program that matches a string that has an a followed by one or more b's.
"""


def aThenB(a_string):
    """Assumes a_string is a string
    returns a boolean, True is a_string contains n a followed by one or more b's
    else False
    """
    regex = "ab+"
    results = re.search(regex, a_string)
    return bool(results)


# print(aThenB("a"))
# print(aThenB("ab"))
# print(aThenB("abacus"))
# print(aThenB("string1"))

"""
4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
"""


def aThen01B(a_string):
    """Assumes a_string is a string
    returns a boolean, True is a_string contains n a followed by zero or one b's
    else False
    """
    regex = "ab?"
    results = re.search(regex, a_string)
    return bool(results)


# print(aThen01B("a"))  # expect True
# print(aThen01B("ab"))  # expect True
# print(aThen01B("abb"))  # expect False
# print(aThen01B("abacus"))  # expect True
# print(aThen01B("string1"))  # expect False

"""
5. Write a Python program that matches a string that has an a followed by three 'b'.
"""


def aThen3B(a_string):
    """Assumes a_string is a string
    returns a boolean, True is a_string contains n a followed by 3 b's
    else False
    """
    regex = "ab{3}"
    results = re.search(regex, a_string)
    return bool(results)


# print(aThen3B("a"))  # expect False
# print(aThen3B("ab"))  # expect False
# print(aThen3B("abbb"))  # expect True
# print(aThen3B("abacus"))  # expect False
# print(aThen3B("string1"))  # expect False

"""
6. Write a Python program that matches a string that has an a followed by two to three 'b'
"""


def aThen23B(a_string):
    """Assumes a_string is a string
    returns a boolean, True is a_string contains n a followed by 2 or 3 b's
    else False
    """
    regex = "ab{2,3}"
    results = re.search(regex, a_string)
    return bool(results)


# print(aThen23B("a"))  # expect False
# print(aThen23B("ab"))  # expect False
# print(aThen23B("abb"))  # expect True
# print(aThen23B("abbb"))  # expect True
# print(aThen23B("abacus"))  # expect False
# print(aThen23B("string1"))  # expect False
"""
7. Write a Python program to find sequences of lowercase letters joined with a underscore.
"""


def wordChars_(a_string):
    """Assumes a_string is a string
    returns a boolean, True is a_string contains lowercase letters joined with underscore
    else False
    """
    regex = "[a-z]+_[a-z]+"
    results = re.search(regex, a_string)
    return bool(results)


# print(wordChars_("adfkljlkj_aslnkl"))  # expect True
# print(wordChars_("adfkljlkj_"))  # expect False
# print(wordChars_("_aslnkl"))  # expect False
# print(wordChars_("ASDASD_aslnkl"))  # expect False
# print(wordChars_("asads_ASDS"))  # expect False
# print(wordChars_("adfkljlkjaslnkl"))  # expect False

"""
8. Write a Python program to find the sequences of one upper case letter
followed by lower case letters.
"""


def uppercase_lowercase(a_string):
    """Assumes a_string is a string
    returns a boolean, True is a_string contains one upper case letter
    followed by lower case letters
    else False
    """
    regex = "[A-Z][a-z]+"
    results = re.search(regex, a_string)
    return bool(results)


# print(uppercase_lowercase("Aadfa"))  # expect True
# print(uppercase_lowercase("asdaf"))  # expect False
# print(uppercase_lowercase("AAdsda"))  # expect True
# print(uppercase_lowercase("asdAasdf"))  # expect True

"""
9. Write a Python program that matches a string that has an 'a' followed by anything,
ending in 'b'.
"""


def aAnythingB(a_string):
    """Assumes a_string is a string
    returns a boolean, True if a_string contains an 'a' followed by anything,
    ending in 'b'
    else False
    """
    regex = "a.+b$"
    results = re.search(regex, a_string)
    return bool(results)


# print(aAnythingB("adb"))  # expect True
# print(aAnythingB("adfjldlfjlkjeijlefwb"))  # expect True
# print(aAnythingB("ab"))  # expect False
# print(aAnythingB("asdklndkldsv"))  # expect False
# print(aAnythingB("sdlknnlkdb"))  # expect False
# print(aAnythingB(""))  # expect False

"""
10. Write a Python program that matches a word at the beginning of a string.
"""


def wordString(a_string):
    """Assumes a_string is a string
    returns a boolean, True if a_string contains a word at the beginning of a string
    else False
    """
    regex = "^\w+ "
    results = re.search(regex, a_string)
    return bool(results)


# print(wordString("cats are"))  # expect True
# print(wordString("cats"))  # expect False
# print(wordString(" cats"))  # expect False
# print(wordString(" cats "))  # expect False
# print(wordString(""))  # expect False
"""
11. Write a Python program that matches a word at the end of string,
with optional punctuation.
"""


def wordStringEnd(a_string):
    """Assumes a_string is a string
    returns a boolean, True if a_string contains a word at the end of string,
    with optional punctuation
    else False
    """
    regex = " \w+\.*$"
    results = re.search(regex, a_string)
    return bool(results)


# print(wordStringEnd("cats"))  # expect False
# print(wordStringEnd(" cats"))  # expect True
# print(wordStringEnd(" cats."))  # expect True
# print(wordStringEnd(" cats "))  # expect False
# print(wordStringEnd(""))  # expect False

"""
12. Write a Python program that matches a word containing 'z'.
"""


def wordWithZ(a_string):
    """Assumes a_string is a string
    returns a boolean, True if a_string contains "z"
    else False
    """
    regex = "\w*z\w*"
    results = re.search(regex, a_string)
    return bool(results)


# print(wordWithZ("zoo"))  # expect True
# print(wordWithZ("mozzie"))  # expect True
# print(wordWithZ("boo!"))  # expect False
# print(wordWithZ(""))  # expect False
"""
13. Write a Python program that matches a word containing 'z',
not at the start or end of the word.
"""


def wordWithMiddleZ(a_string):
    """Assumes a_string is a string
    returns a boolean, True if a_string contains a word with "z"
    not at the start or end of the word.
    else False
    """
    regex = "[^z]z+[^z]"
    results = re.search(regex, a_string)
    return bool(results)


# print(wordWithMiddleZ("mozzie"))  # expect True
# print(wordWithMiddleZ("is mozzie a good puppy?"))  # expect True
# print(wordWithMiddleZ("autolyzed"))  # expect True
# print(wordWithMiddleZ("zoo"))  # expect False
# print(wordWithMiddleZ("zoom"))  # expect False
# print(wordWithMiddleZ("move"))  # expect False
# print(wordWithMiddleZ(""))  # expect False

"""
14. Write a Python program to match a string that contains only
upper and lowercase letters, numbers, and underscores.
"""


def wordCharWords(a_string):
    """Assumes a_string is a string
    returns a boolean, True if a_string contains only upper and lowercase letters,
    numbers, and underscores
    else False
    """
    regex = "^\w*$"
    results = re.search(regex, a_string)
    return bool(results)


# print(wordCharWords("hismasterbrokethekisslingeringly"))  # expect True
# print(wordCharWords("maple_syrup"))  # expect True
# print(wordCharWords("his master broke the kiss lingeringly"))  # expect False
# print(wordCharWords(string1))  # expect False
# print(wordCharWords("api-services-support@amazon.com."))  # expect False
# print(wordCharWords(""))   # expect False


"""
15. Write a Python program where a string will start with a specific number.
"""


def numString(a_string, num):
    """Assumes a_string is a string
    assumes num is a number
    returns a boolean, True if a_string starts with num
    else False
    """
    regex = "^" + str(num)
    results = re.search(regex, a_string)
    return bool(results)


# print(numString("123456789", 12))  # expect True
# print(numString("12", 12))  # expect True
# print(numString("12awdk;k", 12))  # expect True
# print(numString("345678912", 12))  # expect False
# print(numString("3456789", 12))  # expect False

"""
16. Write a Python program to remove leading zeros from an IP address.
"""


def removeLeading0(a_string):
    """assumes a_string is a string representing an IP address
    returns a string, a_string without leading 0s"""
    regex = "\.[0]+"
    results = re.sub(regex, ".", a_string)
    return results


# print(removeLeading0("69.144.50.56"))  # expect 69.144.50.56
# print(removeLeading0("69.144.50.56"))  # expect 69.144.50.56
# print(removeLeading0("69.144.050.056"))  # expect 69.144.50.56
# print(removeLeading0("69.144.50.056"))  # expect 69.144.50.56

"""
17. Write a Python program to check for a number at the end of a string.
"""


def numAtEnd(a_string):
    """assumes a_string is a string
    returns a bool, True if a_string ends with a number, else False"""
    regex = "[0-9]+$"
    results = re.search(regex, a_string)
    return bool(results)


# print(numAtEnd("aadfjifadkjl12"))  # expect True
# print(numAtEnd("aadfjifadkjl 12"))  # expect True
# print(numAtEnd("aadfjif  adkjl12"))  # expect True
# print(numAtEnd("q1e4aadfjifadkjl12"))  # expect True
# print(numAtEnd("567aadfjifadkjl12"))  # expect True
# print(numAtEnd("aadfjifadkjl"))  # expect False
# print(numAtEnd("2124aadfjifadkjl"))  # expect False
# print(numAtEnd("aadfjif34adkjl"))  # expect False
# print(numAtEnd(""))  # expect False
"""
18. Write a Python program to search the numbers (0-9) of length between 1 to 3
in a given string.

"Exercises number 1, 12, 13, and 345 are important"
"""


def findNums1to3Digits(a_string):
    """assumes a_string is a string
    returns a re span object, representing the numbers of lenght 1 to 2 in a_string 
    if it exists, else None"""
    regex = "[^0-9]*([0-9]{1,3})[^0-9]*"
    results = re.search(regex, a_string)
    if results:
        results = results.group(1)
    return results


# print(findNums1to3Digits("123"))  # expect 123
# print(findNums1to3Digits("123aefkoakfl"))  # expect 123
# print(findNums1to3Digits("wfjadfkjl154"))  # expect 154
# print(findNums1to3Digits("eflafjl123sjljlasf"))  # expect 123
# print(findNums1to3Digits("1239afkjnjD"))  # expect None
# print(findNums1to3Digits("EFNNLWDSNAS123456789"))  # expect None
# print(findNums1to3Digits("afkjnjD"))  # expect None
# print(findNums1to3Digits(""))  # expect None

"""
19. Write a Python program to search some literals strings in a string.
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'
"""


def searchLiteral(a_string, patterns):
    """assumes a_string is a string, being searched in
    assumes patterns is a list of strings, to be search for in a_string
    returns a re span object, representing the found literal if it exists,
    else None"""
    results = []
    for pattern in patterns:
        regex = pattern
        results.append(re.search(regex, a_string))
    return results


string5 = "The quick brown fox jumps over the lazy dog."
patterns = ["fox", "dog", "horse"]
# print(searchLiteral(string5, patterns))
# print(searchLiteral(string1, patterns))

"""
20. Write a Python program to search a literals string in a string
and also find the location within the original string where the pattern occurs.

Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'
"""

"""
21. Write a Python program to find the substrings within a string.

Sample text :

'Python exercises, PHP exercises, C# exercises'

Pattern :

'exercises'

Note: There are two instances of exercises in the input string.
"""

"""
22. Write a Python program to find the occurrence and position of
the substrings within a string.
"""

"""
23. Write a Python program to replace whitespaces with an underscore and vice versa.
"""

"""
24. Write a Python program to extract year, month and date from an url.
"""

"""
25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
"""

"""
26. Write a Python program to match if two words from a list of words
starting with letter 'P'.
"""

"""
27. Write a Python program to separate and print the numbers of a given string.
"""

"""
28. Write a Python program to find all words starting with 'a' or 'e' in a given string.
"""


"""
29. Write a Python program to separate and print the numbers and their position
of a given string.
"""

"""
30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
"""

"""
31. Write a Python program to replace all occurrences of space, comma, or dot with a colon
"""

"""
32. Write a Python program to replace maximum 2 occurrences of
space, comma, or dot with a colon.
"""

"""
33. Write a Python program to find all five characters long word in a string.
"""

"""
34. Write a Python program to find all three, four, five characters long words in a string
"""

"""
35. Write a Python program to find all words which are at least 4 characters long
in a string.
"""

"""
36. Write a python program to convert camel case string to snake case string.
"""

"""
37. Write a python program to convert snake case string to camel case string.
"""

"""
38. Write a Python program to extract values between quotation marks of a string.
"""


"""
39. Write a Python program to remove multiple spaces in a string.
"""

"""
40. Write a Python program to remove all whitespaces from a string.
"""

"""
41. Write a Python program to remove everything except alphanumeric characters
from a string.
"""

"""
42. Write a Python program to find urls in a string.
"""

"""
43. Write a Python program to split a string at uppercase letters.
"""

"""
44. Write a Python program to do a case-insensitive string replacement.
"""

"""
45. Write a Python program to remove the ANSI escape sequences from a string.
"""

"""
46. Write a Python program to find all adverbs and their positions in a given sentence.

Sample text : "Clearly, he has no excuse for such behavior."
"""

"""
47. Write a Python program to split a string with multiple delimiters.

Note : A delimiter is a sequence of one or more characters used to specify
the boundary between separate, independent regions in plain text or other data streams.
An example of a delimiter is the comma character,
which acts as a field delimiter in a sequence of comma-separated values.
"""

"""
48. Write a Python program to check a decimal with a precision of 2.
"""

"""
49. Write a Python program to remove words from a string of length
between 1 and a given number.
"""

"""
50. Write a Python program to remove the parenthesis area in a string.
Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
Expected Output:
example
w3resource
github
stackoverflow
"""

"""
51. Write a Python program to insert spaces between words starting with capital letters.
"""

"""
52. Write a Python program that reads a given expression and evaluates it.
Terms and conditions:
The expression consists of numerical values, operators and parentheses, and ends with '='
The operators includes +, -, *, / where, represents, addition, subtraction,
multiplication and division.
When two operators have the same precedence, they are applied to left to right.
You may assume that there is no division by zero.
All calculation is performed as integers, and after the decimal point should be truncated
Length of the expression will not exceed 100.
-1 ? 10 9 = intermediate results of computation = 10 9
"""

"""
53. Write a Python program to remove lowercase substrings from a given string.
"""

"""
54. Write a Python program to concatenate the consecutive numbers in a given string.
Original string:
Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6.
Please have your identification ready.
After concatenating the consecutive numbers in the said string:
Enter at 120 Kearny Street. The security desk can direct you to floor 16.
Please have your identification ready.
"""

"""
55. Write a Python program to convert a given string to snake case.
Sample Output:
java-script
gd-script
btw...-what-*-do*-you-call-that-naming-style?-snake-case?
"""

"""
56. Write a Python program that takes any number of iterable objects or objects
with a length property and returns the longest one.
Sample Output:
Orange
[1, 2, 3, 4, 5]
Java
Python
"""
