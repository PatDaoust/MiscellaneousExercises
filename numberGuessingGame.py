# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:46:43 2022

@author: catal
"""
"""
guess the number game
goal = commande line gameplay

c: ask user if want to play
    if true: start game
    else: goodbye, close program
guess_ count = 1
c: ask user for desired range
    option: enter ints
    option: easy 1-10, medium 1-100, hard -1000-1000
c : select random number in range
c: ask user to guess
u: submit guess
    guess_count += 1
c: if guess = num:
    congrats, you got it in guess_count guesses
        optional: sub program to give random congrats message
    do you want to play anoyher round?
        if true: restart variables
    if guess < num:
        your guess is too low
    if guess > num:
        your guess is too high
"""


def main():
    """plays a numbetr guessing game in the console"""
    play_game = input("would you like to play a game with me? \n\
I'll pick a number, and you have to guess it!\n\
If you want to play, type 'yes'\n")
    # initialize gameplay
    if play_game == "Yes" or play_game == "yes":
        play_game = True
    if play_game is not True:
        print("Okay. Let's play another time!")
        # program ends
    # pick mode
    mode = None
    easy_valid = ['easy', 'easy mode']
    hard_valid = ['hard', 'hard mode']
    if mode is None:
        mode = input("Okay! Would you like to play in easy mode or hard mode?\n")
        mode = mode.lower()
        if mode in easy_valid:
            mode = "easy"
            print("you've chosen easy mode. I'll pick a random number between 1 and 100")
        elif mode in hard_valid:
            mode = "hard"
            print("you've chosen hard mode. I'll pick a random number between -1000 and 1000")
        else:
            mode = None
            print("I'm sorry, I didn't understand that. \n\
Please type 'easy' for easy mode, or 'hard' for hard mode")
    # guessing loop
    guesses_count = 0

if __name__ == "__main__":
    main()
