# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:30:42 2021

@author: catal
"""
import pdb 
import unittest

# 1Let min = 0 and max = n-1.
# 2If max < min, then stop: target is not present in array. Return -1.
# 3Compute guess as the average of max and min, rounded down (so that it is an integer).
# 4If array[guess] equals target, then stop. You found it! Return guess.
# 5If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
# 6Otherwise, the guess was too high. Set max = guess - 1.
# 7Go back to step 2.

def binarySearch(array, target_value):
    '''
    assumes array is a list of ints
    assumes target_value is an int, the int to search for 
    Returns an int, either the index of the location in the array,
    or -1 if the array did not contain the targetValue */'''
    #initialize values
    min_i = 0
    max_i = len(array) -1 
    not_found = True
    #binary search loop
    while not_found == True:
        guess_i =  (min_i + max_i)//2
        if max_i <= min_i:
            return -1 
        if array[guess_i] == target_value:
            return guess_i
        if array[guess_i] < target_value:
            min_i = guess_i + 1
        if array[guess_i] > target_value:
            max_i = guess_i - 1

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
# print(binarySearch(primes, 13))

def swap(a_list, index1, index2):
    """assumes a_list is a list, 
    assumes index1 is an int representing the index of one of the two values to be swaped 
    assumes index1 is an int representing the index of one of the two values to be swaped
    does not modify the inputed list
    returns a list, equivalent to a_list with index1 and index2 swapped
    e.g. swap(['a','b','c'], 0, 2) -> ['c','b','a'] 
    """
    b_list = a_list.copy()
    b_list[index1] = a_list[index2]
    b_list[index2] = a_list[index1]
    return b_list

# print(swap(["a","b","c"], 0, 2))

def findMinIndex(a_list,start_index, verbose=False):
    """assumes that a_list is a list of numbers
    assumes start)index is an int, representing the index where to start looking
    returns a tuple (int,number)
    the index of the smallest number found between start_index and the end of the list, inclusive,
    and the value of this smallest number
    if there is a tie for smallest valye, returns the 1st occurence
    """
    min_index =  start_index
    min_value = a_list[start_index]
    for index in range(start_index,len(a_list)):
        if a_list[index] < min_value:
            min_index = index
            min_value = a_list[index]
    if verbose:
        print("The index of the minimum value of the subarray starting at index " + str(start_index)
              +" is " + str(min_index) + "."  )
    return min_index

# some_list = [18, 6, 66, 44, 9, 22, 14]
# findMinIndex(some_list,2)

def selectionSort(a_list):
    """assumes a_list is a list of numbers
    returns a list of the numbers in a_list, sorted from smallest to largest
    does not modify the inputed a_list
    """
    list_b = a_list.copy()
    for index in range(len(a_list)):
        local_min_index = findMinIndex(list_b,index)
        list_b = swap(list_b,index, local_min_index)
    return list_b

# some_list = [22, 11, 99, 88, 9, 7, 42]
# print(selectionSort(some_list))

def insert(a_list, value):
    """assumes a_list is a list of numbers, already sorted in accending order
    assumes value is a number
    modifies the inputed a_list
    returns a_list
    """
    # pdb.set_trace()
    index = len(a_list)
    a_list.append(None)
    while index > 0:
        if (a_list[index-1]<=value):
            a_list[index] = value
            return a_list
        #shift value 1 up 1 spot
        a_list[index] = a_list[index-1]
        index -= 1
    a_list[index] = value
    return a_list


# print(insert([1,2,3], 0))

# some_list = [2, 3, 5, 6, 7, 9, 11, 13]
# print(insert(some_list, 1))

def insertionSort(a_list):
    """assumes a_list is a list of numbers
    does not modify the inputed a_list
    returns a list, the sorted version of a_list
    """
    mod_list = a_list[:1]
    for index in range(1,len(a_list)):
        mod_list = insert(mod_list,a_list[index])
    return mod_list

# print(insertionSort([22, 11, 99, 88, 9, 7, 42]))

def iterativeFactorial(num):
    """assumes num is a positive int
    returns an int, num! (the factorial of n)
    """
    factorial = 1
    while num > 0:
        factorial = factorial*num
        num -= 1
    return factorial
    
# num = 6
# iterativeFactorial(num)
# print(num)

def recursiveFactorial(num):
    """assumes num is a positive int
    returns an int, num! (the factorial of n)
    """
    if num == 0:
        return 1
    else: 
        return num * recursiveFactorial(num-1)

# print(recursiveFactorial(10))

def isPalindrome(a_string):
    """assumes a_string is a string
    returns a boolean, true if a_string is a palindrome(including lenght 0), else false
    """
    if len(a_string) <=1:
        return True 
    if a_string[0] == a_string[-1]:
        return isPalindrome(a_string[1:-1])
    else:
        return False
    
# print(isPalindrome("cat"))
# print(isPalindrome(""))
# print(isPalindrome("c"))
# print(isPalindrome("cac"))
# print(isPalindrome("tacocat"))

def powers(x,n):
    """assume x is
    assumes n is
    returns an number, x**n
    """
    # // base case
    if n==0:
        return 1
    # // recursive case: n is negative 
    if n<0:
        return 1/(powers(x,-n))
    # // recursive case: n is positive odd
    if (n>0) and (n%2!=0):
        return x*(powers(x,n-1))
    # // recursive case: n is positive even
    if (n>0) and (n%2==0):
        y = powers(x,n/2)
        return y*y
    
# print(powers(2,0))
# print(powers(2,4))
# print(powers(2,3))
# print(powers(2,-7))



def partition(a_list):
    """assumes a_list is a list of numbers
    modifies a_list by internally moving its elements, 
    such that the rightmost element (the pivot) 
    has to its right only greater or equal elements, 
    and has to its left only lesser or equalelements
    returns an int, the index of the pivot
    """
    #partition list around pivot
    pivot = a_list[-1]
    list_lenght = len(a_list)
    for i in range(list_lenght-1,-1, -1):
        if a_list[i] > pivot:
            a_list.insert(list_lenght, a_list.pop(i))
    #find pivot index
    return a_list.index(pivot)

# print(partition([9, 7, 5, 11, 12, 2, 14, 3, 10, 4, 6]))

def quickSort(a_list, index1,index2):
    """assumes a_list is a list of numbers
    assumes index1 is an int, the starting index
    assumes index1 is an int, the ending index
    returns a list of numbers, the section of a_list[index1;index2] sorted and otherwise unchanges
    """
    if len(a_list) < 2:
        return a_list
    else:
        # print(a_list)
        pivot = partition(a_list)
        # print(a_list)
        # print(pivot)
        quickSort(a_list,0,pivot-1) #fix overriding
        quickSort(a_list, pivot+1,len(a_list)) #fix overriding
        # print(a_list)
    return a_list

# quickSort([3,4,1,2])
# quickSort([3,4,5,1,2],0,4)
# quickSort([9, 7, 5, 11, 12, 2, 14, 3, 10, 4, 6])
































