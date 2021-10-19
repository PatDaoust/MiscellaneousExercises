# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 18:07:12 2021

@author: catal
"""

"""
given random() which generate random numbewr from 0 to 1
calculate pi 

monte carlo simulation of circle in square 
"""
import random 
import pdb

def randomPiSimulator(large_num):
    """
    assumes large_num is an int, a large number used a the number of trials for the simulation
    returns a float, an estimation of pi 
    based on Monte Carlo simulation
    recommended minuming large_num is 10000"""
    in_circle_counter = 0
    in_square_counter = 0
    for trial in range(large_num):
        x= random.random()
        y = random.random()
        in_square_counter += 1
        if ((x**2)+(y**2))<1:
            in_circle_counter += 1
    return 4 * (in_circle_counter / in_square_counter)
    
for num in range(10):
    print(randomPiSimulator(10000000000))