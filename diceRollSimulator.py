# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:21:43 2022

@author: catal
"""
import random
"""
dice roll simulator

ask user what sort of dice they want to roll
d4
d6
d8
d10
d12
d20
d100

generate random num in range
"""


def main():
    """runs a dice rolling simulator"""
    keep_rolling = True
    while keep_rolling:
        d_type_available = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
        print("hello, I'll be assiting you in rolling dice today.")
        print("what sort of dice would you like to roll today?")
        # get validated dice type
        valid_d_type = False
        while not valid_d_type:
            d_type = input("I have d4, d6, d8, d10, d12, d20, and d100.\n\
    Please type your selection\n")
            if d_type in d_type_available:
                valid_d_type = True
            else:
                print("I'm sorry, that's not available right now.")
        # get validated rolls
        valid_roll_num = False
        while not valid_roll_num:
            roll_num = input("How many tumes would you like to roll your " + d_type + "?\n")
            try:
                roll_num = int(roll_num)
                if roll_num >= 1 and roll_num < 1000000:
                    valid_roll_num = True
            except ValueError:
                print("I'm sorry, I didn't understand that.\nPlease type an integer number.")
        # generate and print rolls
        print("Time to roll!")
        for i in range(roll_num):
            roll = random.randint(1, int(d_type[1:]))
            print(f"You {i+1}th roll is {roll}")
        # ask to roll again
        re_roll = input("If you want to roll again, please type 'yes'\n")
        if re_roll.lower() != "yes":
            keep_rolling = False


if __name__ == "__main__":
    main()
