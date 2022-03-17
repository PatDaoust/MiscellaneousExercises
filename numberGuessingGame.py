# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:46:43 2022

@author: catal
"""
import random
"""
guess the number game
goal = commande line gameplay

c: ask user if want to play
    if true: start game
    else: goodbye, close program
guess_ count = 1
c: ask user for desired range
=    option: easy 1-10, hard -1000-1000
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
    option: track guesses that are too high and two low, display
    display last guess
"""


def main():
    """plays a numbetr guessing game in the console"""
    play_game = input("would you like to play a game with me? \n\
I'll pick a number, and you have to guess it!\n\
If you want to play, type 'yes'\n")
    # initialize gameplay
    if play_game.lower == "yes":
        play_game = True
    if play_game is not True:
        print("Okay. Let's play another time!")
        # program ends
    # pick mode
    mode = None
    easy_valid = ['easy', 'easy mode']
    hard_valid = ['hard', 'hard mode']
    while mode is None:
        mode = input("Okay! Would you like to play in easy mode or hard mode?\n")
        mode = mode.lower()
        if mode in easy_valid:
            mode = "easy"
            print("you've chosen easy mode. I'll pick a random number between 1 and 100")
            random_num = random.randint(1, 100)
        elif mode in hard_valid:
            mode = "hard"
            print("you've chosen hard mode. I'll pick a random number between -1000 and 1000")
            random_num = random.randint(-1000, 1000)
        else:
            mode = None
            print("I'm sorry, I didn't understand that. \n\
Please type 'easy' for easy mode, or 'hard' for hard mode\n")
    # guessing loop
    guesses_count = 0
    guess = None
    while guess != random_num:
        # take guess
        while guess is None:
            guess = input("Please type a number\n")
            try:
                guess = int(guess)
            except ValueError:
                print("I'm sorry, I didn't understand that. \nPlease type a number\n")
        # evaluate guess
        if guess > random_num:
            print("Nope, your guess of " + str(guess) + " was too high")
            guess = None
            guesses_count += 1
        elif guess < random_num:
            print("Nope, your guess of " + str(guess) + " was too low")
        else:
            print("you guessed the random number " + str(random_num) + " in "
                  + str(guesses_count) + " guesses.")
            print(pickAWinningMessage())
            break
        guess = None
        guesses_count += 1


def pickAWinningMessage():
    """returns a string, a congratulatory message"""
    messages = ["You won!",
                "Congratulations, champ!",
                "You did it!",
                "I knew it was only a matter of time",
                "Well done!",
                "What an impressive achievement!",
                "You’re awesome! Way to go!",
                "Keep it up!",
                "You have the determination to do whatever you can dream.",
                "I commend you on this latest success",
                "The reward of a thing well done is to have done it",
                "Hats off to you",
                "Attagamer",
                "Good job",
                "Way to shine"]
    random_index = random.randint(0, len(messages)-1)
    return messages[random_index]


if __name__ == "__main__":
    main()
