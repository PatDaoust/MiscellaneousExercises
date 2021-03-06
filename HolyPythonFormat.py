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


# violetColor()


"""Exercise 6-d Print the values of the "roads" key from the nested dictionary."""


def printRoads():
    nested_dict = {"Dakar": {"weather": "sunny", "roads": "dry"}}
    ans_1 = nested_dict["Dakar"]["roads"]
    print(ans_1)


# printRoads()


"""Exercise 6-e Print the first element of the weather for Tokyo."""


def printweather():
    nested_dict = {"Tokyo": {"weather": ["sunny", "cloudy"], "roads": "dry"},
                   "Dakar": {"weather": ["foggy", "windy"], "roads": "sandy"}}
    ans_1 = nested_dict["Tokyo"]["weather"][0]
    print(ans_1)


# printweather()


"""Exercise 7-a
Write an if statement that asks for the user's name via input() function.
If the name is "Bond" make it print "Welcome on board 007."
Otherwise make it print "Good morning NAME". (Replace Name with user's name)
    """


def goodMorning():
    """uses input() to gather name. prints a greeting"""
    name = input("Please type your name: ")
    if name == "Bond":
        print("Welcome on board 007.")
    else:
        print(f"Good morning {name}")


# goodMorning()


"""Exercise 7-b
Do the same thing as exercise 7-a this time making sure if the name is
bond with lower case b it still prints "Welcome on board 007."
"""


def goodmorningv2():
    """uses input() to gather name. prints a greeting"""
    name = input("Please type your name: ")
    if name == "Bond" or name == "bond":
        print("Welcome on board 007.")
    else:
        print(f"Good morning {name}")


# goodmorningv2()


"""Exercise 7-c Write a function named "evens"
which returns True if a number is even and otherwise returns False."""


def evens(i):
    """assumes i is a number
    returns a boolean, True if i is even, else False"""
    if i % 2 == 0:
        return True
    else:
        return False


# print(evens(99))
# print(evens(98))


"""Exercise 7-d Write a function named "thedecimal"
which returns the decimal part of a number.
If decimal part is zero function should return this string: "INTEGER"."""


def thedecimal(num):
    """assumes num is a numeric
    returns an int representing the decimal part of num, if it exists,
    else returns a string 'INTEGER' """
    rounded = int(num)
    if rounded == num:
        return "INTEGER"
    else:
        return num - rounded


# print(thedecimal(99.09))
# print(thedecimal(99.00))


"""Exercise 7-e
treepersqkm is a dictionary showing the tree number of countries per square kilometer
for random countries with sizeable population numbers.
Write a function named "moretrees" that returns
a list of country names with more than 20.000 trees per square kilometer."""


def moretrees(a_dict):
    """assumes a_dict is a dictionary of key strings and value ints,
    representing country names and number of tree per square kilometer
    returns a list of strings, representing the name of countries
    with more than 20.000 trees per square kilometer"""
    green_contries_list = []
    for key, value in a_dict.items():
        if value >= 20000:
            green_contries_list.append(key)
    return green_contries_list


treepersqkm = {"Finland": 90652,
               "Taiwan": 69593,
               "Japan": 49894,
               "Russia": 41396,
               "Brazil": 39542,
               "Canada": 36388,
               "Bulgaria": 24987,
               "France": 24436,
               "Greece": 24323,
               "United States": 23513,
               "Turkey": 11126,
               "India": 11109,
               "Denmark": 6129,
               "Syria": 534,
               "Saudi Arabia": 1}

# print(moretrees(treepersqkm))


"""Exercise 7-f Write a function named "count_l"
that counts the number of words that contain the letter: "l" in a given string."""

string = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"


def count_l(a):
    """assumes a in a string
    returns an int, representing the number of words in a with an "l"
    treats sequences of characters seperated by a space as a word
    """
    word_list = a.split()
    l_count = 0
    for word in word_list:
        if "l" in word:
            l_count += 1
    return l_count


# print(count_l(string))


"""Exercise 7-g
Write a similar function to 7-e
which returns the number of words that start with letter "A" in a string.
 (Make sure it counts lower case a's as well.)."""


def count_a(a):
    """assumes a in a string
    returns an int, representing the number of words in a with an "l"
    treats sequences of characters seperated by a space as a word
    """
    word_list = a.split()
    a_count = 0
    for word in word_list:
        if "a" in word or "A" in word:
            a_count += 1
    return a_count


# print(count_a(string))


"""Exercise 8-b Write a for loop which print "Hello!, " plus each name in the list."""


def helloLoop(name_list):
    """assumes name_list is a list of strings, representing names
    prints a greeting for each name in name_list"""
    for name in name_list:
        print("Hello!, " + name)


lst = ["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
# helloLoop(lst)


"""Exercise 8-a Write a for loop so that every item in the list is printed."""


def printList(a_list):
    """assumes a_list is a list of strings
    prints all the elements in a_list"""
    for elem in a_list:
        print(elem)


list_a = ["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
# printList(list_a)


"""Exercise 8-c Write a for loop that iterates through a string and prints every letter"""


def printString(a_string):
    """assumes a_string is a string
    prints the characters of a_string"""
    for char in a_string:
        print(char)


str_a = "Antarctica"
# printString(str_a)


"""Exercise 8-d
Type a code inside the for loop so that counter variable named c
is increased by one each time loop iterates.
Can you guess how many times it will add 1?."""


def countC():
    str_ = "Civilization"
    c = 0
    for i in str_:
        c += 1
        print(c)


# countC()


"""Exercise 8-e
Using a for loop and .append() method append each item with a Dr. prefix to the lst.
"""


def Dr(a_list):
    """assumes a_list is a list of strings
    returns a new list, of the elements of a_list prepended with 'Dr.' """
    list2 = []
    for elem in a_list:
        mod_elem = "Dr." + elem
        list2.append(mod_elem)
    return list2


lst1 = ["Phil", "Oz", "Seuss", "Dre"]
# print(Dr(lst1))


"""Exercise 8-f Write a for loop which appends the square of each number to a new list"""


def squares(num_list):
    """assumes num_list is a list of numerics
    returns a list of squares of each elem of num_list"""
    square_list = []
    for num in num_list:
        square = num**2
        square_list.append(square)
    return square_list


lst2 = [3, 7, 6, 8, 9, 11, 15, 25]
# print(squares(lst2))


"""Exercise 8-g Write a for loop using an if statement,
that appends each number to the new list if it's positive."""


def appendPositives(num_list):
    """assumes num_list is a list of numerics
    returns a list of numerics, the positive numerics of num_list"""
    pos_list = []
    for num in num_list:
        if num > 0:
            pos_list.append(num)
    return pos_list


lst4 = [111, 32, -9, -45, -17, 9, 85, -10]
# print(appendPositives(lst4))


"""Exercise 8-h Using for loop and if statement,
append the value minus 1000 for each key to the new list if the value is above 1000.
 i.e.: if the value is 1500, 500 should be added to the new list."""


def over1000minus1000(num_dict):
    """assumes num_list is a dictionary whose values are numerics
    returns a list of numerics, of the values over 1000 of num_dict minus 1000"""
    minus_list = []
    for key, value in num_dict.items():
        mod_num = value - 1000
        if mod_num > 0:
            minus_list.append(mod_num)
    return minus_list


dict1 = {"z1": 900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
# print(over1000minus1000(dict1))


"""Exercise 8-i Write a for loop which appends the type of each element in
the first list to the second list."""


def typeList(a_list):
    """assumes a_list is a list with at least 1 element
    returns a list of the types of all the elements of a_list"""
    type_list = []
    for elem in a_list:
        type_list.append(type(elem))
    return type_list


# print(typeList([3.01, 66, "teddy bear", True, [], {}]))


"""Exercise 9-a Write a while loop that adds all the numbers up to 100 (inclusive)."""


def whileAdd100():
    """returns an int, the sum of all the integers up to 100 (inclusive)"""
    n = 0
    my_sum = 0
    while n <= 100:
        my_sum += n
        n += 1
    return my_sum


# print(whileAdd100())


"""Exercise 9-b Using while loop, if statement and str() function;
iterate through the list and if there is a 100, print it with its index number.
 i.e.: "There is a 100 at index no: 5"""


def index100(num_list):
    """asssumes num_list is a list of numerics
    prints "there is a 100 at index no: " for each 100 found"""
    i = 0
    while i < len(num_list):
        if num_list[i] == 100:
            print("There is a 100 at index no: " + str(i))
        i += 1


# index100([10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95])


"""Exercise 9-c Using while loop and an if statement write a function named
name_adder which appends all the elements in a list to a new list
unless the element is an empty string: "". """


def name_adder(a_list):
    """assumes a_list is a list of strings (possibly including empty strings)
    returns a list of the non-empty strings in a_list"""
    non_empty_list = []
    for elem in a_list:
        if elem:
            non_empty_list.append(elem)
    return non_empty_list


# print(name_adder(["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]))


"""Exercise 9-d inside a function named name_adder,
 write a while loop that stops appending items to the new list as soon as
 it encounters an empty string: "".
 And prints "There is an empty string and returns the new list."
"""


def name_adder_stop(a_list):
    """assumes a_list is a list of strings (possibly including empty strings)
    returns a list of the non-empty strings in a_list up to the first empty string"""
    i = 0
    new_list = []
    while i < len(a_list):
        if a_list[i]:
            new_list.append(a_list[i])
        else:
            print("There is an empty string")
            return new_list
        i += 1
    return new_list


# print(name_adder_stop(["Sam", "", "Ben", "Olivia", "Alicia"]))


"""Exercise 10-a: Break statement inside a For Loop
Place a break statement in the for loop so that it prints from 0 to 7 only (including 7)
"""

def break7():
    for i in range(100):
        print(i)
        if i >= 7:
            break


# break7()


"""Exercise 10-b: If and Continue statements inside a For Loop
Add an if statement and a continue statement to the loop so that
it skips when iterator equals "sun"."""


def skipSun(a_list):
    """asssumes a_list is a list of strings
    prints strings != "sun" """
    for elem in a_list:
        if elem == "sun":
            continue
        print(elem)


# skipSun(["snow", "rain", "sun", "clouds"])


"""Exercise 11-a
Write a lambda function that takes x as parameter and returns x+2.
 Then assign it to a variable named L."""


L = lambda x: x + 2
# print(L(5))


"""Exercise 11-b
Write a lambda function which takes z as a parameter and returns z*11
Assign it to variable named: f."""

f = lambda z: z * 11
# print(f(2))


"""Exercise 11-c
Write a function which takes two arguments: a and b
and returns the multiplication of them: a*b.
Assign it to a variable named: f."""

f = lambda a, b: a * b
# print(f(2,3))


"""Exercise 11-d
Using .sort() method, create a lambda function that sorts the list in descending order.
Refrain from using the reverse parameter.

(Hint: lambda will be passed to sort method's key parameter as argument)

Please check out Hint 0 below to be informed about a glitch regarding this exercise.
"""

list5 = [100, 10, 10000, 1, 9, 999, 99]
list5.sort(key=lambda a: 100/a)
# print(list5)


"""Exercise 11-e
use the sorted() function to sort the list in ascending order with lambda."""

lst6 = [100, 10, 10000, 1, 9, 999, 99]

new_list = sorted(lst6)
# print(new_list)


"""Exercise 11-f
Using sorted() function and lambda sort the words in the list based on
their second letter from a to z."""


lst7 = ["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]

lst8 = sorted(lst7, key=lambda a: a[1])
# print(lst8)


"""Exercise 11-g
Using sorted() function and lambda sort the tuples in the list based on
the second items."""

lst9 = [(19542209, "New York"),
        (4887871, "Alabama"),
        (1420491, "Hawaii"),
        (626299, "Vermont"),
        (1805832, "West Virginia"),
        (39865590, "California")]

lst10 = sorted(lst9, key=lambda a: a[1])
# print(lst10)


"""Exercise 11-h
Using sorted() function and lambda sort the tuples in the list based on
the last character of the second items."""

lst11 = sorted(lst9, key=lambda a: a[1][-1])
# print(lst11)


"""Exercise 11-i
Using sorted() function, reverse parameter and lambda sort the tuples in the list
based on the last character of the second items in reverse order."""

lst12 = sorted(lst9, key=lambda a: a[1][-1], reverse=True)
# print(lst12)


"""Exercise 12-a: Merging 2 Lists with Zip Function
Using zip() function and list() function, create a merged list of tuples
from the two lists given."""


def mergeLists(lst1, lst2):
    """asssumes lst1 and lst2 are lists
    returns a list of tuples of the elementsts of lst1 and lst2"""
    return list(zip(lst1, lst2))


lst13 = [19542209, 4887871, 1420491, 626299, 1805832, 39865590]
lst14 = ["New York", "Alabama", "Hawaii", "Vermont", "West Virginia",  "California"]
# print(mergeLists(lst13, lst14))


"""Exercise 12-b: Merging a List and a Range with Zip Function
First create a range from 1 to 8. Then using zip,
merge the given list and the range together to create a new list of tuples."""


def mergeRangeList(lst):
    """Assumes lst is a list
    returns a list of tuples of int and the elements of lst,n of lenght = len(lst)"""
    return list(zip(list(range(1, len(lst)+1)), lst))


lst15 = ["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry",
         "Transport"]
# print(mergeRangeList(lst15))


"""Exercise 12-c: Creating a Dictionary by Merging 2 Lists Using Zip Function
Using zip and dict functions create a dictionary which has its key-value pairs
coming from lst1 and lst2."""


def mergeListsToDict(list1, list2):
    """assumes list1 is a list of immutable elements
    assumes list 2 is a list
    returns a dict using list1 as keys and list2 as values"""
    return dict(zip(list1, list2))


lst16 = ["Netflix", "Hulu", "Sling", "Hbo"]
lst17 = [198, 166, 237, 125]
# print(mergeListsToDict(lst16, lst17))


"""Exercise 12-d: 2 Lists Zip Merged and Sorted
Using zip, list and sorted functions create a sorted list of tuples from lst1 and lst2.
"""


def sortedMerge(list1, list2):
    """assumes list1 and list2 are lists
    returns a list of tuples, from the elements of list1 and list2"""
    # zip lists
    combo_list = list(zip(list1, list2))
    # sort list by 2nd elem
    combo_list = sorted(combo_list, key=lambda a: a[1])
    return combo_list


lst18 = ["Mike", "Danny", "Jim", "Annie"]
lst19 = [4, 12, 7, 19]
# print(sortedMerge(lst18, lst19))


"""Exercise 13-a
Write a map function that adds plus 5 to each item in the list."""


def plus5(num):
    """assumes num is a numeric
    returns a numeric, num + 5"""
    return num + 5


lst20 = [10, 20, 30, 40, 50, 60]
lst21 = list(map(plus5, lst20))
# print(lst21)


"""Exercise 13-b
Write a map function that returns the squares of the items in the list."""


def squares2(num):
    """assumes num is a list of numerics
    returns a numeric, the square of num"""
    return num ** 2


lst22 = [10, 20, 30, 40, 50, 60]
lst23 = list(map(squares2, lst22))
# print(lst23)


"""Exercise 13-c
Write a map function that adds "Hello, " in front of each item in the list.
"""


def addHello(a_string):
    """assumes that a_string is a string
    returns a string, "hello, " + string"""
    return "Hello, " + a_string


lst24 = ["Jane", "Lee", "Will", "Brie"]
lst25 = list(map(addHello, lst24))
# print(lst25)


"""Exercise 13-d
Using map() function and len() function create a list that's consisted of
lengths of each element in the first list."""

lst26 = ["Alpine", "Avalanche", "Powder", "Snowflake", "Summit"]
lst27 = list(map(len, lst26))
# print(lst27)


"""Exercise 13-e
Using map() function and lambda add each elements of two lists together.
Use a lambda with two arguments."""

lst28 = [100, 200, 300, 400, 500]
lst29 = [1, 10, 100, 1000, 10000]

lst30 = list(map(lambda a, b: a+b, lst28, lst29))
# print(lst30)


"""Exercise 13-f
Using map() function and lambda and count() function create a list
which consists of the number of occurence of letter: a."""

lst31 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
lst32 = list(map(lambda x: x.count("a"), lst31))
# print(lst32)

"""Exercise 13-g
Using map() function and lambda and count() function create a list consisted of
the number of occurence of both letters: A and a."""

lst33 = list(map(lambda x: x.count("a") + x.count("A"), lst31))
# print(lst33)


"""Exercise 13-h
Using map() function, first return a new list with absolute values of existing list.
Then for ans_1, find the total sum of the new list's elements."""

lst34 = [99.3890, -3.5, 5, -0.7123, -9, -0.003]
# new_lst = list(map(abs, lst34))
# print(sum(new_lst))


"""Exercise 14-a
Using filter() function filter the list so that only negative numbers are left."""


def negative(num):
    """assumes num is a numeric
    returns a boolean, True if num is negative, else False"""
    return num < 0


lst35 = [12, -1, 9, 8, -0.5, -0.2, -100]
lst36 = list(filter(negative, lst35))
# print(lst36)


"""Exercise 14-b
Using filter function, filter the even numbers so that only odd numbers
are passed to the new list."""

lst37 = [22, 100, 19, 13, 11, 1, 4, 66]
lst38 = list(filter(lambda a: a % 2 != 0, lst37))
# print(lst38)


"""Exercise 14-c
Using filter() and list() functions and .lower() method filter all the vowels
in a given string."""


def isVowel(char):
    """Assumes char is a single character
    returns a boolean; True if char is a vowel (aeiou), else False
    not case sensitive"""
    vowels = "aeiouAEIOU"
    return char in vowels


str1 = "Winter Olympics in 2022 will take place in Beijing China"
lst37 = list(filter(isVowel, str1))
# print(lst37)


"""Exercise 14-d
This time using filter() and list() functions filter all the positive integers
in the string."""


def isDigit(char):
    """assumes char is a single character
    returns a boolean, True is char is a digit, else False"""
    digits = "0123456789"
    return char in digits


lst38 = list(filter(isDigit, str1))
# print(lst38)


"""Exercise 14-e
Using map() and filter() functions add 2000 to the values below 8000."""


lst39 = [1000, 500, 600, 700, 5000, 90000, 17500]
lst40 = list(map(lambda b: b + 2000, (filter(lambda a: a < 8000, lst39))))
# print((lst40))


"""Exercise 14-f
This time swap the map() and filter() functions so that map() function is
inside filter() function.
Convert a number to positive if it's negative in the list.
Only pass those that are converted from negative to positive to the new list."""


lst41 = [-1000, 500, -600, 700, 5000, -90000, -17500]
lst42 = list(map(abs, filter(lambda a: a < 0, lst41)))
# print((lst42))


"""
Exercise 15-a
Using sorted() function, sort the list in ascending order."""

lst43 = [500, 1000, 400, 40000, 999, 2, 0.5, 17]
lst44 = sorted(lst43)
# print(lst44)


"""Exercise 15-b
Using sorted() function, sort the list from a to z."""

lst45 = ["zebra", "bird", "ant", "porcupine", "giraffe"]
lst46 = sorted(lst45)


"""Exercise 15-c
Using sorted() function sort the list from z to a."""


lst47 = ["zebra", "bird", "ant", "porcupine", "giraffe"]
list48 = sorted(lst47, reverse=True)
# print(list48)


"""Exercise 15-d
Using sorted() function sort the list in descending order."""

lst49 = [500, 1000, 400, 40000, 999, 2, 0.5, 17]
lst50 = sorted(lst49, reverse=True)
# print(lst50)


"""Exercise 15-e
Using len function and sorted() function, sort the list based on the length of the strings
(In ascending order)"""

lakes1 = ["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]
lakes2 = sorted(lakes1, key=len)
# print(lakes2)


"""Exercise 15-f
Using len function and sorted() function, sort the list based on the length of the strings
this time in descending order."""

lakes3 = sorted(lakes1, key=len, reverse=True)
# print(lakes3)


"""Exercise 15-g
Using lambda and sorted() function,
sort the list based on last characters of the items from z to a."""

lakes4 = sorted(lakes1, key=lambda a: a[-1], reverse=True)
# print(lakes4)


"""Exercise 15-h
Using lambda and sorted() function,sort the list based on
the remainder from dividing each element to 5 (From greater to smaller)."""

lst51 = [1000, 50, 66, 101, 333, 9999, 19, 300, 200, 250]
lst52 = sorted(lst51, key=lambda a: a % 5, reverse=True)
# print(lst52)


"""Exercise 16-a
Create an identical list from the first list using list comprehension"""

lst53 = [1, 2, 3, 4, 5]
lst54 = [x for x in lst53]
# print(lst54)


"""Exercise 16-b
Create a list from the elements of a range from 1200 to 2000 with steps of 130,
using list comprehension."""

rng = range(1200, 2000, 130)
lst55 = [x for x in rng]
# print(lst55)


"""Exercise 16-c
Use list comprehension to contruct a new list but add 6 to each item."""

lst56 = [44, 54, 64, 74, 104]
lst57 = [x+6 for x in lst56]
# print(lst57)


"""Exercise 16-d
Using list comprehension, construct a list from the squares of each element in the list"""

lst58 = [2, 4, 6, 8, 10, 12, 14]
lst59 = [x**2 for x in lst58]
# print(lst59)


"""Exercise 16-e
Using list comprehension, construct a list from the squares of each element in the list,
if the square is greater than 50."""

lst60 = [x**2 for x in lst59 if x**2 > 50]
# print(lst60)


"""Exercise 16-f
Given dictionary is consisted of vehicles and their weights in kilograms.
Contruct a list of the names of vehicles with weight below 5000 kilograms.
In the same list comprehension make the key names all upper case."""

dict2 = {"Sedan": 1500,
         "SUV": 2000,
         "Pickup": 2500,
         "Minivan": 1600,
         "Van": 2400,
         "Semi": 13600,
         "Bicycle": 7,
         "Motorcycle": 110}

lst61 = [x.upper() for x in dict2 if dict2[x] < 5000]
# print(lst61)


"""Exercise 17-a
Create a dictionary from the list with same key:value pairs, such as: {"key": "key"}"""

lst62 = ["NY", "FL", "CA", "VT"]

dict3 = {key: key for key in lst62}
# print(dict3)


"""Exercise 17-b
First, create a range from 100 to 160 with steps of 10.
Second, using dict comprehension, create a dictionary where each number in the range
is the key and each item divided by 100 is the value."""

rng = range(100, 160, 10)
dict4 = {key: key/100 for key in rng}
# print(dict4)


"""Exercise 17-c
Using dict comprehension and a conditional argument create a dictionary from the current
dictionary where only the key:value pairs with value above 2000 are taken to the new
dictionary."""

dict5 = {"NFLX": 4950, "TREX": 2400, "FIZZ": 1800, "XPO": 1700}
dict6 = {key: dict5[key] for key in dict5 if dict5[key] > 2000}
# print(dict6)


"""Exercise 18"""

# help(str)
# help(dict)
# help(list)
# help(tuple)


"""Exercise 6-a
Use strip method to strip the whitespaces on both sides of the string."""

str3 = "     Hello World!   "
str4 = str3.strip()
# print(str4)

"""Exercise 20-a
Place a pass statement so that if block won't throw an error."""


# name = input("Please enter your name.")
# if len(name) > 0:
#     print(name)
# else:
#     pass


"""Exercise 20-b
Place pass statement in your function so that you can leave it unfinished
and it doesn't throw an error."""


def f_1(x):
    pass


f_1(1)


"""Exercise 20-c
Put a pass statement in your for loop to avoid an error."""

lst63 = [9, 10, 100, 999]
for i in lst:
    pass


"""Exercise 20-d
Put a pass statement in the while loop so it doesn't throw an error."""


i = 0
while i < 20:
    i = i + 1
    if i**2 < 49:
        print(i * 100)
    else:
        pass
