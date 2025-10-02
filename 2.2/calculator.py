"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""
# ChatBot witha Loop
# Author: Salomi Aiyathurai

# we have a list of the top 5 most sold cars in 2024
car_5 = ["Ford F-Series", "Chevrolet Silverado", "Toyota RAV4", "Honda CR-V", "Tesla Model Y"]

# this is the person who is playing's starting score
score = 0

# explain the game to the player and tell them how the game works
print("Hi, let's play a game, wher you have to guess the top 5 most sold cars in 2024. Every time you guess a car correctly your score gets boosted by one point of you guess it incorrectly then your score gets dropped by one. Your starting score is 0.")

# ask them to guess
print("Guess one of the cars that you think was the top 5 most sold cars in 2024?")

# give them an opputunity to guess
guess_1 = input()

# if they guess coreectly they get a point
if guess_1 in car_5:
    print("You got " + guess_1 + " correct! Your score just got boosted by one point" )
    score = score + 1
    
else: 
    print("You got " + guess_1 + " incorrect! Your score is " + score + ".")
    score = score - 1
    
print("Guess another car that you think is in the top 5 most sold cars in 2024?")

guess_2 = input()

# if they guess coreectly they get a point
if guess_2 in car_5:
    print("You got " + guess_2 + " correct! Your score just got boosted by one point" )
    score = score + 1
    
else: 
    print("You got " + guess_2 + " incorrect! Your score is " + score + ".")
    score = score - 1
    
guess_3 = input()

# if they guess coreectly they get a point
if guess_3 in car_5:
    print("You got " + guess_3 + " correct! Your score just got boosted by one point" )
    score = score + 1
    
else: 
    print("You got " + guess_3 + " incorrect! Your score is " + score + ".")
    score = score - 1
    
print("Guess another car that you think is in the top 5 most sold cars in 2024?")

guess_4 = input()

# if they guess coreectly they get a point
if guess_4 in car_5:
    print("You got " + guess_4 + " correct! Your score just got boosted by one point" )
    score = score + 1
    
else: 
    print("You got " + guess_4 + " incorrect! Your score is " + score + ".")
    score = score - 1
    
print("Guess another car that you think is in the top 5 most sold cars in 2024?")

guess_5 = input()

# if they guess coreectly they get a point
if guess_5 in car_5:
    print("You got " + guess_5 + " correct! Your score just got boosted by one point. Now we are going to show your final score! Can we ask you a question about our game, reply yes or no." )
    score = score + 1
    
else: 
    print("You got " + guess_5 + " incorrect! Your score is  " + score + ". Now we are going to show your final score!")
    score = score - 1

print("Your score is " + str(score) + ". Can we ask you a question about our game, reply yes or no.")

question = ["Do you like this game, can you rate out of 100?", "Rate this game from 1 to 100", "How good was this game out of 100?"]

response = ["Thank you for writing the review!", "Thanks for your opinion!", "Thanks so much for finishing this survey."]

import random

for question in question:
    print(question)
    
    rating = int(reply)
    print("You rated this game " + str(rating) + " out of 100.")
    print(random.choice(responses))
    break

    reply = input().lower().strip()

    if reply == "no":
        print("Okay, no worries. Thanks for playing!")
        break

    else: 
        print(random.choice(responses))