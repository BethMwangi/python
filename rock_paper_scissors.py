#!/usr/bin/python
# Rock, paper ,scissors game 
# The rules apply, i.e , 
# * Rock beats scissors
# * Paper beats rock
# * Scissors beats paper

import sys
print "Let's get started!"

player1 =raw_input("Enter your name please:") #prompts the user to input their name
player2 = raw_input("Enter your name please:")

player1_ans = raw_input ("%s, do you want to choose rock, paper or scissors?" % player1)
player2_ans = raw_input ("%s, do you want to choose rock, paper or scissors?" % player2)

def compare(a,b):
    if a == b:
        return "Oops! it is a tie"
    elif a == "rock":
        if b == "scissors":  #nested if statement to cover all the outcomes
           return "Rock wins"
        else:
           return "paper wins"
    elif a == "paper":
        if b == "scissors":
           return "scissors wins"
        else:
            return "paper wins"
            
    elif a == "scissors":
        if b == "rock":
            return "rock wins"
        else:
            return "scissors win"
    else:
        return ("Wrong input, kindly choose either rock, paper or scissors to play")
        sys.exit()
print (compare(player1_ans, player2_ans))
