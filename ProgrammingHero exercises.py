# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 12:05:01 2021

@author: catal
"""

import random
import pdb
import math
from itertools import count, islice


def userInputToNumber():
    """returns a float, the product of the two user inputs"""
    an_int = int(input("please input an integer: "))
    a_float = float(input("please input a float: "))
    return an_int * a_float


# print(userInputToNumber())


def mathPower():
    """returns a float, input1**input2"""
    input1 = float(input("please input the base: "))
    input2 = float(input("please input the exponent: "))
    return input1**input2


# print(mathPower())


def randomNumber():
    """returns a random number between 0 and 10"""
    return random.random()*10


# for x in range(100):
#     print(randomNumber())


def floorDivision():
    num1 = float(input("please give me the quotient: "))
    num2 = float(input("please give me a divisor: "))
    return num1//num2


# print(floorDivision())


def swapTwoVariables(var1, var2):
    """assumes var 1 and var 2 are objects
    swaps the values of var1 and var2
    returns None
    """
    print(var1, var2)
    var1, var2 = var2, var1
    print(var1, var2)


# swapTwoVariables("a", "b")


def maxOfTwo():
    """returns a number, the larger of the two inputs"""
    num1 = float(input("please give me a number: "))
    num2 = float(input("please give me a number: "))
    return max(num1, num2)


# print(maxOfTwo())


def MaxOFThree():
    """returns a number, the largeest of the three inputs"""
    num1 = float(input("please give me a number: "))
    num2 = float(input("please give me a number: "))
    num3 = float(input("please give me a number: "))
    return max(num1, num2, num3)


def averageOfNumbers():
    """returns a number, the arithmetic average of all the inputs"""
    amount_numbers = int(input("how many numbers would you like to enter?: "))
    number_sum = 0
    for i in range(amount_numbers):
        num = float(input("please give me a number: "))
        number_sum += num
    return number_sum/amount_numbers


# print(averageOfNumbers())


def divisibleBy3And5(num):
    """assumes num is a number
    returns True is num is divisible by 3 and 5, else 5
    """
    return num % 3 == 0 and num % 5 == 0


def sumOfDigits():
    """returns an int, the sum of all the digits of the input int"""
    num = input("please give me an integer: ")
    digit_sum = 0
    for digit in num:
        digit_sum += int(digit)
    return digit_sum


# print(sumOfDigits())

def sumOfElements(a_list):
    """assumes a_list is a list of numbers
    returns a number, the sum of the elements of a_list
    """
    return sum(a_list)


# print(sumOfElements)


def largestElementOfAList(a_list):
    """assumes a_list is a list of numbers
    returns a number, the maximum element of a_list
    """
    return max(a_list)


# print(largestElementOfAList)


def sumOfSquares(a_list):
    """assumes a_list is a list of numbers
    returns a number, the sum of each element**2  of a_list
    """
    return sum([x**2 for x in a_list])


# print(sumOfSquares([1, 2, 3]))


def secondLargest(a_list):
    """assumes a_list is a list of numbers
    returns the second largest element of a_list
    """
    largest = max(a_list)
    a_list.remove(largest)
    return max(a_list)


# print(secondLargest([1, 2, 3, 4]))


def secondSmallestElement(a_list):
    """assumes a_list is a list of numbers
    returns the second smallest element of a_list
    """
    smallest = min(a_list)
    a_list.remove(smallest)
    return min(a_list)


# print(secondSmallestElement())


def removeDuplicateChars(a_string):
    """assumes a-string is a string
    returns a string, a_string with any duplicate characters removed
    """
    duplicateless_string = ""
    char_set = set()
    for char in a_string:
        if char not in char_set:
            char_set.add(char)
            duplicateless_string += char
    return duplicateless_string


# print(removeDuplicateChars("kittenssssk"))


def milesToKilometers(miles):
    """assumes miles in a number
    returns a float, the amount of kilometers equivalent to miles
    """
    return 1.609344*miles


# print(milesToKilometers(1))


def celciusToFahrenheit(celcius):
    """assumes celcius is a number
    returns a floar, the equivalent temperature in Farenheit
    """
    return (celcius*9/5)+32


# print(celciusToFahrenheit(22))


def decimalToBinaryv1(decimal):
    """assumes decimal is an int, representing a number in base 10
    returns an int, representing the same number in base 2
    """
    return bin(decimal)


# print(decimalToBinaryv1(16))


def decimalToBinaryv2(decimal):
    """assumes decimal is an int, representing a number in base 10
    returns an int, representing the same number in base 2
    """
    digits = []
    reminder = decimal
    while reminder > 0:
        digits.append(str(reminder % 2))
        reminder = reminder // 2
    return "".join(digits[::-1])


# print(decimalToBinaryv2(10))


def decimalToBinaryRecursive(decimal, digits=[]):
    """assumes decimal is an int, representing a number in base 10
    assumes digits is a list of ints, representing the number in base 2
    returns an int, representing the same number in base 2
    """
    if decimal <= 0:
        return "".join(digits[::-1])
    else:
        digits += (str(decimal % 2))
        decimal = decimal // 2
        return (decimalToBinaryRecursive(decimal, digits))


# print(decimalToBinaryRecursive(22, []))


def binaryToDecimal(binary):
    """assumes binary is a string or int representing a number in base 2
    returns an int, the same number represented in base 10
    """
    multiple = 1
    decimal = 0
    for digit in str(binary)[::-1]:
        decimal += int(digit) * multiple
        multiple = multiple * 2
    return decimal


# print(binaryToDecimal(10011110))

def simpleInterest(amount_borrowed, years_borrowed, interest_rate_percent):
    """assumes amount_borrowed in an int, representing the amoutn fo money borrowed
    assumes year+borrowed is an int, representing the years the amount was borrowed for
    assumes interest_rate_percent is a number, representing the interest rate
    returns a float, the simple yearly interest
    """
    return amount_borrowed * years_borrowed * interest_rate_percent / 100


# print(simpleInterest(5000, 2, 2))


def compoundInterest(amount_borrowed, years_borrowed, interest_rate_percent):
    """assumes amount_borrowed in an int, representing the amoutn fo money borrowed
    assumes year+borrowed is an int, representing the years the amount was borrowed for
    assumes interest_rate_percent is a number, representing the interest rate
    returns a float, the compound interest
    """
    return amount_borrowed * ((1 + (interest_rate_percent/100)) ** (years_borrowed))


# print(compoundInterest(5000, 2, 2))


def calculateGrades(grade1, grade2, grade3, grade4, grade5):
    """assumes grade1 to grade5 are numbers
    returns a string lenght 1, the letter grade
    """
    average_grade = (grade1 + grade2 + grade3 + grade4 + grade5) / 5
    if average_grade > 90:
        return "A"
    elif average_grade > 80:
        return "B"
    elif average_grade > 70:
        return "C"
    elif average_grade > 60:
        return "D"
    else:
        return "F"


# print(calculateGrades(90, 85, 50, 95, 99))


def gravitationalForce(mass1, mass2, distance):
    """assumes mass1 is a number, representing the mass of an object, in kilograms
    assumes mass2 is a number, representing the mass of another object, in kilograms
    assumes distance is a number, representing the distance between the objects, in meters
    """
    gravitational_constant = 6.673 * (10**-11)
    return gravitational_constant * mass1 * mass2 / (distance ** 2)


# print(gravitationalForce(10, 5, 20))


def triangleArea(side1, side2, side3):
    """assumes side1, side 2, and side3 are numbers, the lenghts of the side of a triangle
    returns a float, representing the area of the triangle
    """
    half_peri = (side1 + side2 + side3) / 2
    return (half_peri*(half_peri-side1)*(half_peri-side2)*(half_peri-side3))**0.5


# print(triangleArea(24, 30, 18))


def checkPrime(n):
    """assumes n is an integer
    returns a boolean,
    true if n is a prime number,
    false if n is not a prime number
    """
    return n > 1 and all(n % i for i in islice(count(2), int(math.sqrt(n)-1)))


# print(check_prime(1))


def allPrimeNumbers(upper_limit):
    """assumes upper_limit is an int, representing the largest number to look for primes
    returns a list of ints, the primes less than upper_limit
    """
    prime_list = []
    for num in range(upper_limit):
        if checkPrime(num):
            prime_list.append(num)
    return prime_list


# print(allPrimeNumbers(10))


def primeFactors(num):
    """assumes num is an integer
    returns a list of ints, representing the prime factors of num"""
    prime_factors_list = []
    for divisor in range(num):
        if checkPrime(divisor):
            if num % divisor == 0:
                prime_factors_list.append(divisor)
    return prime_factors_list


# print(primeFactors(30))


def smallestPrimeFactorv1(num):
    """assumes num is an integer
    returns an int, representing the smallest prime factor of num"""
    return min(primeFactors(num))


# print(smallestPrimeFactorv1(30))


def smallestPrimeFactorv2(num):
    """assumes num is an integer
    returns an int, representing the smallest prime factor of num"""
    for divisor in range(num):
        if checkPrime(divisor):
            if num % divisor == 0:
                return divisor


# print(smallestPrimeFactorv1(30))


def reverseStringv1(a_string):
    """assumes a_string is a string
    returns a string, the reverse of a_string"""
    return a_string[::-1]


# print(reverseStringv1("kittens"))


def reverseStringv2(a_string):
    """assumes a_string is a string
    returns a string, the reverse of a_string"""
    reverse_string_list = []
    for i in range(1, len(a_string)+1):
        reverse_string_list.append(a_string[-i])
    return "".join(reverse_string_list)


# print(reverseStringv2("kittens"))


def reverseStringStackv1(a_string):
    """assumes a_string is a string
    returns a string, the reverse of a_string"""
    letters_list = list(a_string)
    reversed_letters_list = []
    for i in range(len(letters_list)):
        reversed_letters_list.append(letters_list.pop())
    return "".join(reversed_letters_list)


def reverseStringStackv2(a_string):
    """assumes a_string is a string
    returns a string, the reverse of a_string"""
    letters_list = list(a_string)
    reversed_string = ""
    for i in range(len(letters_list)):
        reversed_string += letters_list.pop()
    return reversed_string


# print(reverseStringStackv1("abcdefg"))
# print(reverseStringStackv2("abcdefg"))


def reverseStringRecursive(a_string):
    """assumes a_string is a string
    returns a string, the reverse of a_string"""
    # base case
    if len(a_string) <= 1:
        return a_string
    # recursive case
    else:
        return a_string[-1] + reverseStringRecursive(a_string[:-1])


# print(reverseStringRecursive("cats"))


def reverseNumberv1(num):
    """assumes num is a int
    returns an int, the reverse of num"""
    return int(str(num)[::-1])


# print(reverseNumberv1(123))


def reverseNumberv2(num):
    """assumes num is a int
    returns an int, the reverse of num"""
    holding_num = num
    return_string = ""
    while holding_num > 0:
        return_string += str(holding_num % 10)
        holding_num //= 10
    return int(return_string)


# print(reverseNumberv2(123))


def reverseNumberv3(num):
    """assumes num is a int
    returns an int, the reverse of num"""
    holding_num = num
    return_num = 0
    while holding_num > 0:
        return_num += (holding_num % 10) * (10 ** (len(str(holding_num)) - 1))
        holding_num //= 10
    return return_num


# print(reverseNumberv3(123))


def reverseWord(a_sentence):
    """assumes a_sentence is a string of characters and spaces
    treats spaces as delimeters between "words" (not checked to be "real" words)
    returns a string, with the same "words" in reverse order
    e.g. reverseWord("cats are purrfect") -> "purrfect are cats"
    """
    words_list = a_sentence.split(" ")
    return " ".join(words_list[::-1])


# print(reverseWord("cats are purrfect"))


def checkPalindrome(word):
    """assumes word is a string
    returns a boolean, True if word is a palindrome, else False"""
    return word == reverseStringv1(word)


# print(checkPalindrome("eye"))
# print(checkPalindrome("cat"))
# print(checkPalindrome("tacocat"))


def cubeSum(num):
    """assumes num is an int
    returns an int, the sum of cubes of the ints 1 to n"""
    cube_sum = 0
    for i in range(1, num+1):
        cube_sum += i**2
    return cube_sum


# print(cubeSum(9))


def armstrongNumber(num):
    """assumes num is an int
    returns a boolean, True if num is an armstrong number, else False.
    An armstrong number = sum of digits ** number of digits
    e.g. 371 = 3**3 + 7**3 + 1**3
    """
    digit_sum = 0
    for digit in str(num):
        digit_sum += int(digit) ** 3
    return num == digit_sum


# print(armstrongNumber(371))
# print(armstrongNumber(369))


def GCD(num1, num2):
    """assumes num1 and num2 are ints
    returns an int, the greatest common divisor of num1 and num2"""
    for i in range(min(num1, num2), 0, -1):
        if (num1 % i == 0) and (num2 % i == 0):
            return i


# print(GCD(15, 45))  # 15
# print(GCD(14, 49))  # 7
# print(GCD(5, 11))  # None


def divisibleBy(i, nums):
    """assumes nums is a list of ints
    assumes i is an int
    returns a boolean, True if all the ints in nums are divisible by i. else false
    """
    for num in nums:
        if num % i != 0:
            return False
    return True


# print(divisibleBy(5, [5, 15, 20, 25]))
# print(divisibleBy(5, [5, 15, 20, 24]))


def GCDMulti(nums):
    """assumes nums is a list of ints
    returns an int, the greatest common divisor of nums"""
    for i in range(min(nums), 0, -1):
        if divisibleBy(i, nums):
            return i


# print(GCDMulti([15, 45]))  # 15
# print(GCDMulti([14, 21, 49]))  # 7
# print(GCDMulti([5, 11]))  # None


def LCM(num1, num2):
    """assumes num1 and num2 are ints
    returns an int, representing the least common multiple of num1 and num2
    """
    # return smallest elem in both num1 and num2 multiples
    max_possible_LCM = num1 * num2
    multiples_num1 = set("")
    multiples_num2 = set("")
    for i in range(max_possible_LCM, 1, -1):
        if i % num1 == 0:
            multiples_num1.add(i)
        if i % num2 == 0:
            multiples_num2.add(i)
    return min(multiples_num1.intersection(multiples_num2))


# print(LCM(4, 5))
# print(LCM(4, 8))


def guessGame():
    """plays an interactive number guessing game in the console
    enter a numer 1 through 10 to make a guess
    if you guess right, you get points
    To end the game, press q or interrupt the script
    """
    # innitialize gameplay variables
    play_game = True
    points = 0
    valid_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    # play the game
    while play_game:
        user_num = input("Please input a whole number 1 to 10: ")
        if user_num in valid_nums:
            random_num = str(random.randint(1, 10))
            if user_num == random_num:
                points += 10
                print("That's correct!")
                print(f"The random number was {random_num}")
                print("You've gained 10 points")
                print(f"You have {points} points")
            else:
                points -= 1
                print("Sorry, that's not the random number")
                print(f"The random number was {random_num}")
                print("You've lost 1 point")
                print(f"You have {points} points")
        elif user_num == 'q' or user_num == 'Q':
            play_game = False
            print("You have pressed 'q', the game is ending now")
            print("Please play again soon")
        else:
            print("Sorry, thats not a valid input")
            print("To play make sure to enter a whole number 1 to 10")
            print("Or press 'q' to stop playing")


# guessGame()

def userResultsRockPaperScissors(user_action, random_action):
    """assumes user_action and random_action are strings
    matching "rock" or "paper" or "scissors"
    returns a string; "win", "draw", or "loose"
    """
    if user_action == "rock":
        if random_action == "paper":
            return "lose"
        elif random_action == "scissors":
            return "win"
        elif random_action == "rock":
            return "draw"
        else:
            return None
    elif user_action == "paper":
        if random_action == "rock":
            return "win"
        elif random_action == "scissors":
            return "lose"
        elif random_action == "paper":
            return "draw"
        else:
            return None
    elif user_action == "scissors":
        if random_action == "paper":
            return "win"
        elif random_action == "rock":
            return "lose"
        elif random_action == "scissors":
            return "draw"
        else:
            return None
    else:
        return None


def rockPaperScissors():
    """plays an interactive game of rock-paper-sisscors in the console
    if you win the round, you get a point
    if you loose the round, you get knocked out
    """
    # infinite loop to play:
    #     user input rock, paper, sissors
    #         q to quit
    #     randomly pick r/p/s
    #         (list with 3 options, random gen int 0/1/2 and call list[randon int])
    #     logic for who wins
    #     win
    #         point += 1
    #     tie
    #        pass
    #     lose
    #         knockout
    #         offer to play again
    #             points = 0
    #             rounds += 1
    # innitialize gameplay variables
    play_game = True
    points = 0
    rounds = 0
    valid_actions = ["rock", "paper", "scissors"]
    while play_game:
        user_action = input("please type 'rock', 'paper', or 'scissors': ")
        # TODO figure out why not recognize 'rock' as valid input'
        if user_action in valid_actions:
            random_action = valid_actions[random.randint(0, 2)]
            user_result = userResultsRockPaperScissors(user_action, random_action)
            if user_result == "win":
                points += 1
                print(f"The computer played {random_action}")
                print("Congradulations! You won this hand. You gained a point")
                print(f"You have {points} points")
                print(f"You are on round {rounds}")
            elif user_result == "draw":
                print(f"The computer played {random_action}")
                print("This hand was a draw")
                print(f"You still have {points} points")
                print(f"You are on round {rounds}")
            elif user_result == "lose":
                points = 0
                rounds += 1
                print(f"The computer played {random_action}")
                print("Sorry, you lost this hand and got knocked out.")
                print("Let's play another round. If you want to quit here, press 'q'")
            else:
                print("Sorry, something has gone drastically wrong\nPlease try again")
        elif user_action == "q" or user_action == "Q":
            play_game = False
            print("You have pressed 'q', the game is ending now")
            print("Please play again soon")
        else:
            print("Sorry, thats not a valid input")
            print("To play, make sure to type 'rock' or 'paper' or 'scissors' correctly")
            print("Or press 'q' to stop playing")


rockPaperScissors()


def cowsAndBulls():
    pass


def cowsAndBulls4Digits():
    pass


def wordCompletion():
    pass


def wordHangman():
    pass
