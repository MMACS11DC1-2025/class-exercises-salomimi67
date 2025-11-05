# Title: Guess Number
# Author: Salomi Aiyathurai
# Date: October 28, 2025

import random
number = int(random.choice(range(101)))
guess_count = 1
print("I have a number in mind from 0-100. Can you guess what number I'm thinking of?")
guess = int(input())



while guess != number:  

    if guess > number:
        print("The number that I am thinking of is lower than " + str(guess))
        guess_count += 1

    elif guess < number:
        print("The number that I am thinking of is higher than " + str(guess))
        guess_count += 1

    elif guess == number:
        guess_count += 1
        break

    print("I have a number in mind from 0-100. Can you guess what number I'm thinking of?")
    guess = int(input())
    
print("You have guessed the right number! It took you " + str(guess_count) + " times to guess.") 