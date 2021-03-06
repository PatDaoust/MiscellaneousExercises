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


def searchLiteralLocation(a_string, patterns):
    """assumes a_string is a string, being searched in
    assumes patterns is a list of strings, to be search for in a_string
    returns a list of re span object, representing the found literal if it exists,
    else returns an empty list"""
    results = []
    for pattern in patterns:
        regex = pattern
        match = re.search(regex, a_string)
        if match:
            results.append((match, match.span()))
    return results


# print(searchLiteralLocation(string5, patterns))
# print(searchLiteralLocation(string1, patterns))
"""
21. Write a Python program to find the substrings within a string.

Sample text :

'Python exercises, PHP exercises, C# exercises'

Pattern :

'exercises'

Note: There are two instances of exercises in the input string.
"""


def findSubstring(a_string, substring):
    """assumes a_string is a string
    assumes substring is a string
    return a list of 2-tuples of ints, representing the span(s) where the substring is
    found, if it is found. Else returns an empty list"""
    pattern = substring
    results = re.finditer(pattern, a_string)
    spans = []
    for item in results:
        spans.append(item.span())
    return spans


string6 = "Python exercises, PHP exercises, C# exercises"
substring = "exercises"
# print(findSubstring(string6, substring))
# print(findSubstring(string2, substring))
"""
22. Write a Python program to find the occurrence and position of
the substrings within a string.
"""


def findSubstringLocation(a_string, substring):
    """assumes a_string is a string
    assumes substring is a string
    return a list of 2-tuple of string and 2-tuple of ints, representing the occurence
    and span where the substring is found, if it is found. Else returns an empty list"""
    pattern = substring
    results = re.finditer(pattern, a_string)
    spans = []
    for item in results:
        print(item)
        spans.append((pattern, item.span()))
    return spans


# print(findSubstringLocation(string6, substring))
# print(findSubstringLocation(string2, substring))
"""
23. Write a Python program to replace whitespaces with an underscore and vice versa.
"""


def swapWhitespaceUnderscores(a_string):
    """assumes a_string is a string
    returns a string, with underscores where a_string hadswhitespace, and whitespace
    where a_string has underscores"""
    new_string = re.sub(" ", "_", a_string)
    new_string = re.sub("_", " ", a_string)
    return new_string


# print(swapWhitespaceUnderscores(string1))
# print(swapWhitespaceUnderscores("hello_friends_and_enemies"))
# print(swapWhitespaceUnderscores("who_goes there?"))
# print(swapWhitespaceUnderscores("begone whiper-snapper!"))
# print(swapWhitespaceUnderscores("kittens"))
# print(swapWhitespaceUnderscores(""))
"""
24. Write a Python program to extract year, month and date from an url.
"""


def extractYearMonthDate(url):
    """Assumes url is a string, representing a url with a full date
    returns re match object, representing the full date from the url"""
    pattern = "\d{4}/\d{2}/\d{2}"
    result = re.search(pattern, url)
    return result


url1 = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
# print(extractYearMonthDate(url1))
"""
25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
"""


def convertDateFormat(date):
    """assumes date is a string, representing a date in yyyy-mm-dd format
    returns a string, representing a date in dd-mm-yyyy format"""
    pattern = "(\d{4})-(\d{2})-(\d{2})"
    result = re.sub(pattern, r"\3-\2-\1", date)
    return result


# print(convertDateFormat("1993-01-02"))
# print(convertDateFormat("2022-01-30"))
"""
26. Write a Python program to match if two words from a list of words
starting with letter 'P'.
"""


def matchPP(a_string):
    """assumes a_string is a string
    returns re match object if it finds two consecutive words that start with P,
    else returns None"""
    pattern = "[P|p]\w+\s[P|p]\w+"
    result = re.search(pattern, a_string)
    return result


# print(matchPP("Pretty ponies in the field"))
# print(matchPP("A field full of pretty ponies."))
# print(matchPP(string2))
"""
27. Write a Python program to separate and print the numbers of a given string.
"""


def printTheNums(a_string):
    """Assumes a_string is a string
    prints the numbers in a_string"""
    pattern = "\D+"
    results = re.split(pattern, a_string)
    if results:
        for result in results:
            print(result)


# printTheNums("114387054870")
# printTheNums("mary had 1 little lamb")
# printTheNums("1 afjidsjlk")
# printTheNums("gWJL1")
# printTheNums("14 fsnjfa `231 dbijoja")
# printTheNums("Ten 10, Twenty 20, Thirty 30")
# printTheNums(string1)
"""
28. Write a Python program to find all words starting with 'a' or 'e' in a given string.
"""


def startWithAorE(a_string):
    """assumes a_string is a string
    returns a list of strings, representing the words in a_string starting with 'a' or 'e'
    if any are found. else returns an empty list"""
    pattern = "\s((a|e)+\w*)\s"
    results = re.finditer(pattern, a_string)
    results_list = [result.group(1) for result in results]
    return results_list


# print(startWithAorE(string1))
# print(startWithAorE(string2))
# print(startWithAorE("Write a Python program to abbreviate for each word"))
# print(startWithAorE("hello world"))
"""
29. Write a Python program to separate and print the numbers and their position
of a given string.
"""

def printTheNumsPositions(a_string):
    """Assumes a_string is a string
    prints the numbers and their span in a_string"""
    pattern = "\d+"
    results = re.finditer(pattern, a_string)
    if results:
        for result in results:
            print(str(result.group()) + " found at location " + str(result.span()))


# printTheNumsPositions("114387054870")
# printTheNumsPositions("mary had 1 little lamb")
# printTheNumsPositions("1 afjidsjlk")
# printTheNumsPositions("gWJL1")
# printTheNumsPositions("14 fsnjfa `231 dbijoja")
# printTheNumsPositions("Ten 10, Twenty 20, Thirty 30")
# printTheNumsPositions(string1)
"""
30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
"""


def replaceRoadWithRd(a_string):
    """assumes a_string is a string
    returns a string, with "Rd." where a_string has "Road" """
    pattern = "[Rr]oad"
    replacement = "Rd."
    result = re.sub(pattern, replacement, a_string)
    return result


# print(replaceRoadWithRd("A road is a linear way for the conveyance of traffic"))
# print(replaceRoadWithRd("Select the region or road where you plan to travel"))
# print(replaceRoadWithRd("Curvy Road"))
# print(replaceRoadWithRd(""))
"""
31. Write a Python program to replace all occurrences of space, comma, or dot with a colon
"""


def subColonForSpaceCommaDot(a_string):
    """assumes a_string is a string
    returns a new string, with a colon where a_string has a space, comma, or dot"""
    pattern = "[\s,.]"
    new_string = re.sub(pattern, ":", a_string)
    return new_string


# print(subColonForSpaceCommaDot(string1))
# print(subColonForSpaceCommaDot(string6))
# print(subColonForSpaceCommaDot(" ,."))
# print(subColonForSpaceCommaDot(" "))
# print(subColonForSpaceCommaDot(""))
"""
32. Write a Python program to replace maximum 2 occurrences of
space, comma, or dot with a colon.
"""


def subColonForSpaceCommaDotMax2(a_string):
    """assumes a_string is a string
    returns a new string, with a colon where a_string has 2 spaces, commas, or dots"""
    pattern = "[\s,.]"
    new_string = re.sub(pattern, ":", a_string, count=2)
    return new_string


# print(subColonForSpaceCommaDotMax2(string1))
# print(subColonForSpaceCommaDotMax2(string6))
# print(subColonForSpaceCommaDotMax2(" ,."))
# print(subColonForSpaceCommaDotMax2(" "))
# print(subColonForSpaceCommaDotMax2(""))
"""
33. Write a Python program to find all five characters long word in a string.
"""


def find5CharWords(a_string):
    """assumes a_string is a string
    returns a list of strings, representing all the 5 character long words in a_string"""
    pattern = r"(\b)(\w{5})(\b)"
    results = re.findall(pattern, a_string)
    return results


# print(find5CharWords(string1))
# print(find5CharWords("hello world"))
# print(find5CharWords("Bonjour toute le monde"))
# print(find5CharWords("The quick brown fox jumps over the lazy dog."))
# print(find5CharWords("jfhajEJLJFEW'IJOEGTHONETG57579YHGIIH;F EFR"))  # expect blank
# print(find5CharWords(""))  # expect blank
"""
34. Write a Python program to find all three, four, five characters long words in a string
"""


def find3to5CharWords(a_string):
    """assumes a_string is a string
    returns a list of strings, representing all the 5 character long words in a_string"""
    pattern = r"(\b)(\w{3,5})(\b)"
    results = re.findall(pattern, a_string)
    return results


# print(find3to5CharWords(string1))
# print(find3to5CharWords("hello world"))
# print(find3to5CharWords("Bonjour toute le monde"))
# print(find3to5CharWords("The quick brown fox jumps over the lazy dog."))
# print(find3to5CharWords("jfhajEJLJFEW'IJOEGTHONETG57579YHGIIH;F"))  # expect blank
# print(find3to5CharWords(""))  # expect blank
"""
35. Write a Python program to find all words which are at least 4 characters long
in a string.
"""


def find4PlusCharWords(a_string):
    """assumes a_string is a string
    returns a list of strings, representing all the words 4 or more characrers
    long in a_string"""
    pattern = r"(\b)(\w{4,})(\b)"
    results = re.findall(pattern, a_string)
    return results


# print(find4PlusCharWords(string1))
# print(find4PlusCharWords("hello world"))
# print(find4PlusCharWords("Bonjour toute le monde"))
# print(find4PlusCharWords("The quick brown fox jumps over the lazy dog."))
# print(find4PlusCharWords("jfhajEJLJFEW'IJOEGTHONETG57579YHGIIH;F"))  # expect blank
# print(find4PlusCharWords(""))  # expect blank
"""
36. Write a python program to convert camel case string to snake case string.
"""


def camelCaseToSnakeCase(a_string):
    """assumes a_string is a string in camelCase
    returns a new string, representing a_string in snake_case"""
    pattern = "([a-z]+)([A-Z]{1})"
    new_string = re.sub(pattern, r"\1_\2", a_string)
    return new_string


# print(camelCaseToSnakeCase("camelCase"))
# print(camelCaseToSnakeCase("NaNoWriMo"))
# print(camelCaseToSnakeCase("haveYouSeenThisPurrfectKitten"))
"""
37. Write a python program to convert snake case string to camel case string.
"""


def snakeCasetoCamelCase(a_string):
    """assumes a_string is a string in snake_case
    returns a new string, representing a_string in camelCase"""
    pattern = "(\w)(_)(\w)"
    new_string = re.sub(pattern, r"\1\3", a_string)
    return new_string


# print(snakeCasetoCamelCase("camel_case"))
# print(snakeCasetoCamelCase("Na_no_wri_mo"))
# print(snakeCasetoCamelCase("have_you_seen_this_purrfect_kitten"))
"""
38. Write a Python program to extract values between quotation marks of a string.
"""


def extractQuotes(a_string):
    """Assumes a_string is a string
    returns a new string, any values between quotation marks of a_string"""
    pattern = """'(.*)'"""
    result = re.search(pattern, a_string)
    if result:
        result = result.group(1)
    return result


# print(extractQuotes("'hello world'"))
# print(extractQuotes("say 'hello'"))
# print(extractQuotes("say 'hello' Curry"))
# print(extractQuotes(string2))
# print(extractQuotes(""))
"""
39. Write a Python program to remove multiple spaces in a string.
"""


def removeMultipleSpaces(a_string):
    """assumes a_string is a string
    returns a new string, a_string but with any multiple spaces removed"""
    pattern = "\s{2,}"
    replace = ""
    new_string = re.sub(pattern, replace, a_string)
    return new_string


# print(removeMultipleSpaces("hello    "))
# print(removeMultipleSpaces("...kittens"))
# print(removeMultipleSpaces("my  favorite food is salmon"))
# print(removeMultipleSpaces("   "))
# print(removeMultipleSpaces(""))
# print(removeMultipleSpaces(string1))

"""
40. Write a Python program to remove all whitespaces from a string.
"""


def removeWhitespace(a_string):
    """assumes a_string is a string
    returns a new string, a_string without whitespace"""
    pattern = "\s*"
    replace = ""
    new_string = re.sub(pattern, replace, a_string)
    return new_string


# print(removeWhitespace(string1))
# print(removeWhitespace(" "))
# print(removeWhitespace("                       "))
# print(removeWhitespace("hello     kitten"))
# print(removeWhitespace(" hello kitten "))
# print(removeWhitespace(" "))
# print(removeWhitespace(""))
"""
41. Write a Python program to remove everything except alphanumeric characters
from a string.
"""


def removeNonAlphanumeric(a_string):
    """assumes a_string is a string
    returns a new string, representing only the alphanumeric characters in a_string"""
    pattern = "[^a-zA-Z0-9]+"
    replace = ""
    new_string = re.sub(pattern, replace, a_string)
    return new_string


# print(removeNonAlphanumeric(string3))
# print(removeNonAlphanumeric("!$)(*&%*&@$)(@_$"))
# print(removeNonAlphanumeric("I have 1 cat!"))
# print(removeNonAlphanumeric(""))
"""
42. Write a Python program to find urls in a string.
"""


def findURL(a_string):
    """Assumes a_string is a string
    returns a list of strings, representing any potentual URLs found in a_string"""
    pattern = "(https?://www.\w+.com/*\S*)"
    results = re.finditer(pattern, a_string)
    results_list = [result.group(1) for result in results]
    return results_list


# print(findURL("http://www.example.com/index.html"))
# print(findURL("https://www.google.com/search?q=url+format&rlz=1C1ONGR_enCA931CA931&oq=url+format&aqs=chrome..69i57j0i512l3j0i20i263i512j0i512l5.1808j0j7&sourceid=chrome&ie=UTF-8"))
# print(findURL("https://www.youtube.com/playlist?list=PLui6Eyny-UzwIo3OBXV_KlsWaxUANvWhh"))
# print(findURL("https://leetcode.com/problems/add-two-numbers/"))
# print(findURL("https://www.ravelry.com/patterns/library/little-diamonds-cowl"))
# print(findURL("https://www.ravelry.com/patterns/library/little-diamonds-cowl or https://www.ravelry.com/patterns/library/cowl-66"))
# print(findURL(string1))
# print(findURL(""))
"""
43. Write a Python program to split a string at uppercase letters.
"""


def splitAtUppercase(a_string):
    """assumes a_string is a string
    returns a list of strings, a_string split at each uppercase letter"""
    pattern = "([A-Z])"
    string_list = re.split(pattern, a_string)
    return string_list


# print(splitAtUppercase(string1))
# print(splitAtUppercase(string2))
# print(splitAtUppercase(string3))
# print(splitAtUppercase("what if it is all lowercase?"))
# print(splitAtUppercase("what IF CONSECUTIVE uppercase?"))
# print(splitAtUppercase(""))
"""
44. Write a Python program to do a case-insensitive string replacement.
"""


def replaceCaseInsensitive(a_string, to_replace, replacement):
    """assumes a_string is a string
    assumes to_replace is a string
    assumes replacement is a string
    returns a new string, a_string with any instances of to_replace replased
    with replacement. case insinsitive."""
    pattern = re.compile(to_replace, re.IGNORECASE)
    new_string = re.sub(pattern, replacement, a_string)
    return new_string


# print(replaceCaseInsensitive(string1, "Bran", "Pat"))
# print(replaceCaseInsensitive(string1, "bran", "Pat"))
# print(replaceCaseInsensitive(string1, "BRAN", "Pat"))
"""
45. Write a Python program to remove the ANSI escape sequences from a string.
"""


def removeANSIEscapeSequences(a_string):
    """assumes a_string is a string
    returns a new string, like a_string with any ANSI escape sequences removed"""
    pattern = "(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]"
    new_string = re.sub(pattern, "", a_string)
    return new_string


# string7 = "\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m"
# print(removeANSIEscapeSequences(string7))  # expect "google.com 216.58.218.206"
# print(removeANSIEscapeSequences(""))
"""
46. Write a Python program to find all adverbs and their positions in a given sentence.

Sample text : "Clearly, he has no excuse for such behavior."
"""


def findAdverbs(a_string):
    """assumes a_string is a string
    returns a list of re.match objects, representing all the adverbs ending in "ly"
    in a_string, and their position"""
    pattern = re.compile("[A-Za-z]+ly", re.IGNORECASE)
    results = re.finditer(pattern, a_string)
    results_list = [result for result in results]
    return results_list


# print(findAdverbs("Clearly, he has no excuse for such behavior."))
# print(findAdverbs(string1))
# print(findAdverbs(string2))
# print(findAdverbs(string3))
# print(findAdverbs(" "))
"""
47. Write a Python program to split a string with multiple delimiters.

Note : A delimiter is a sequence of one or more characters used to specify
the boundary between separate, independent regions in plain text or other data streams.
An example of a delimiter is the comma character,
which acts as a field delimiter in a sequence of comma-separated values.
"""


def splitAtDelimiter(a_string, delimeters):
    """assumes a_string is a string
    assumes delimeters is a string sconsisting of the desired delimiters
    returns a list of strings, a_string split at the delimeters"""
    pattern = "("
    for item in delimeters:
        pattern += (item+"|")
    pattern = pattern[:-1]
    pattern += ")"
    results = re.split(pattern, a_string)
    return results


# print(splitAtDelimiter(string1, ",:;"))
# print(splitAtDelimiter(string1, ","))
# print(splitAtDelimiter(string2, ",;:"))
# print(splitAtDelimiter(string3, ",;:"))
# print(splitAtDelimiter("To github.com:PatDaoust/MiscellaneousExercises.git", ",:;"))
# print(splitAtDelimiter("", ",:;"))
"""
48. Write a Python program to check a decimal with a precision of 2.
"""


def isDecimalPrecision2(num):
    """assumes num is a float or a string representing a float
    returns a boolean, True if num is a decial with a precision of 2,
    else False"""
    num = str(num)
    pattern = "\d+\.(\d+)"
    result = re.match(pattern, num)
    if result:
        decimal_len = len(result.group(1))
        if decimal_len == 2:
            return True
        else:
            return False
    else:
        return False


# print(isDecimalPrecision2(2.22))  # expect True
# print(isDecimalPrecision2("2.22"))  # expect True
# print(isDecimalPrecision2(2.2))  # expect False
# print(isDecimalPrecision2(2.222))  # expect False
# print(isDecimalPrecision2(222))  # expect False
# print(isDecimalPrecision2("2.222222"))  # expect False
# print(isDecimalPrecision2("kittens"))  # expect False
# print(isDecimalPrecision2(""))  # expect False
"""
49. Write a Python program to remove words from a string of length
between 1 and a given number.
"""


def removeWordsLenghtNum(a_string, lenght_x):
    """assumes a_string is a string
    assumes lenght_x is an int
    returns a new string, like a_string with every word of lenght 1 to x removed"""
    # import pdb
    # pdb.set_trace()
    if not isinstance(lenght_x, int):
        raise ValueError("lenght_x must me an int")
    pattern = r"\b\w{1," + str(lenght_x) + r"}\b"
    new_string = re.sub(pattern, "", a_string)
    return new_string


# print(removeWordsLenghtNum(string1, 1))
# print(removeWordsLenghtNum(string1, 2))
# print(removeWordsLenghtNum(string1, 3))
# print(removeWordsLenghtNum(string1, 20))
# print(removeWordsLenghtNum(string1, "kittens"))
"""
50. Write a Python program to remove the parenthesis area in a string.
Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
Expected Output:
example
w3resource
github
stackoverflow
"""


def removeParentesised(a_string):
    """assumes a_string is a string
    returns a new string, as a_string with any sub-string contained in parenthesis removed
    e.g. "example" --> "example" """
    pattern = "(\(.*\))"
    new_string = re.sub(pattern, "", a_string)
    return new_string


# print(removeParentesised("example (.com)"))
# print(removeParentesised("github(.com)/hellow"))
# print(removeParentesised("my (favorite) cat"))
# print(removeParentesised(string2))
# print(removeParentesised(""))
"""
51. Write a Python program to insert spaces between words starting with capital letters.
"""


def insertCapitalSpace(a_string):
    """assumes a_string is a string
    returns a new string, with space between words starting with capital letters"""
    pattern = "([A-Z].*)([A-Z])"
    new_string = re.sub(pattern, r"\1 \2", a_string)
    return new_string


# print(insertCapitalSpace("HelloWorld"))
# print(insertCapitalSpace("Hello World"))
# print(insertCapitalSpace("World Wide Web"))
# print(insertCapitalSpace("pretty kittens"))
# print(insertCapitalSpace("ABCDEFU"))
# print(insertCapitalSpace(""))
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


def evaluateString(a_string):
    """Assumes a_string is a string that consists of numerical values, operators
    and parentheses, and ends with '='
    returns a numeric, the evaluation of a_string"""
    expression = a_string[:-1]
    return eval(expression)


# print(evaluateString("4-2*3="))
# print(evaluateString("4*(8+4+3)="))
"""
53. Write a Python program to remove lowercase substrings from a given string.
"""


def removeLowercase(a_string):
    """assumes a_string is a string
    returns a new string, like a_string with any requences of 2 or more
    lowercase characters removed"""
    pattern = "[a-z]{2,}"
    new_string = re.sub(pattern, "", a_string)
    return new_string


# print(removeLowercase(string2))
# print(removeLowercase("HELLO WORLD"))
# print(removeLowercase("MY pRETTY kITTEN"))
# print(removeLowercase(" "))
"""
54. Write a Python program to concatenate the consecutive numbers in a given string.
Original string:
Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6.
Please have your identification ready.
After concatenating the consecutive numbers in the said string:
Enter at 120 Kearny Street. The security desk can direct you to floor 16.
Please have your identification ready.
"""


def concatNums(a_string):
    """assumes a_string is a string
    returns a new string, like a_string but without any spaces seperating numbers"""
    pattern = "(\d)(\s+)(\d)"
    new_string = re.sub(pattern, r"\1\3", a_string)
    return new_string


string8 = """Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6.
Please have your identification ready."""
# print(concatNums(string8))
"""
55. Write a Python program to convert a given string to snake case.
Sample Output:
java-script
gd-script
btw...-what-*-do*-you-call-that-naming-style?-snake-case?
"""


def convertToDashCase(a_string):
    """assumes a_string is a string
    returns a new string, with dashes where a_string has whitespace"""
    pattern = "\s"
    replacement = "-"
    new_string = re.sub(pattern, replacement, a_string)
    return new_string


# print(convertToDashCase(string2))
# print(convertToDashCase("java script"))
# print(convertToDashCase("gd script"))
# print(convertToDashCase(" "))
# print(convertToDashCase("\n"))
# print(convertToDashCase(""))
"""
56. Write a Python program that takes any number of iterable objects or objects
with a length property and returns the longest one.
Sample Output:
Orange
[1, 2, 3, 4, 5]
Java
Python
"""


def returnLongestIterable(iterable_list):
    """assumes iterables_list is a list of iterables
    returns the longest iterable in iterables_list,
    if iterable_list has at least one element with lenght
    note: if there is a tie, will return the 1st element of that lenght encountered
    else returnes None"""
    max_elem = None
    for elem in iterable_list:
        if (max_elem is None) or (len(elem) > len(max_elem)):
            max_elem = elem
    return max_elem


iterables_list = ["Orange",
                  [1, 2, 3, 4, 5],
                  "Java",
                  "Python",
                  ("a", "b", "c")]
# print(returnLongestIterable(iterables_list))
