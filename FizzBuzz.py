# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 15:10:13 2021

@author: catal
"""


# rules:
#     multiples of 3 = fizz
#     multiples of 5 = buzz
#     multiple of 3 and 5 = fizzbuzz

def fizzBuzz(upto):
    """asssumes upto is an int, represinting how far to fizzBuzz
    prints out a series of strings lenght = upto"""
    for num in range(upto+1):
        if num % 15 == 0:
            print("fizzbuzz")
        elif num % 5 == 0:
            print("buzz")
        elif num % 3 == 0:
            print("fizz")
        else:
            print(num)


fizzBuzz(16)

# whhat to do about 0:
#     count from 1?
#     print fizzbuzz?
#     print 0?
