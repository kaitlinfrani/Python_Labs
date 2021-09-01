# -*- coding: utf-8 -*-
"""

Kaitlin Frani
CPSC 223P-01
Mon Mar 8 13:14:07 2021
kaitlinfrani@csu.fullerton.edu

"""

#need to import random so that computer can give random choice for the game
import random

choices = ["R", "P", "S", "Q"]
computer_choices = ["R", "P", "S"]

game = True
score_player = 0
score_computer = 0
score_ties= 0

#while game runs, let player choose
while game:
    symbol_player = input("Make your choice: (R, P, S, Q) > ").upper()
    if symbol_player == "Q":
        break
    
    #if put something else other than given choices, let them try again
    while not symbol_player in choices:
        print("Invalid entry. Try again.")
        symbol_player = input("Make your choice: (R, P, S, Q) > ").upper()
    
    #random function allows computer to have random choice
    symbol_computer = random.choice(computer_choices)
    if symbol_computer == "R":
        choice_name = "Rock"
    
    if symbol_computer == "P":
        choice_name = "Paper"
    
    if symbol_computer == "S":
        choice_name == "Scissors"
        
    #used to figure out who wins based on index choice, use modulus to figure out remainder
    #[0] = R, [1] = P, [2] = S, [3] = Q
    #if both choose the same then (0-0)%3 = 0 = draw
    #if player chooses P[1], computer chooses R[0] = (1-0)%3 = 1 = winner
    #if player chooses P[1], computer chooses S[2] = (1-2)%3 = 2 = loser
    #if player chooses R[0], computer chooses P[1] = (0-1)%3 = 2 = loser
    #if player chooses R[0], computer chooses S[2] = (0-2)%3 = 1 = winner
    #if player chooses S[2], computer chooses R[0] = (2-0)%3 = 2 = loser
    #if player chooses S[2], computer chooses P[1] = (2-1)%3 = 1 = winner
    difference = (choices.index(symbol_player) - choices.index(symbol_computer)) % 3
    
    if difference == 0:
        print(f"Computer chose {choice_name}. Call it a draw.")    
        score_ties += 1
    
    if difference == 1:
        print(f"Computer chose {choice_name}. You win.")    
        score_player += 1
    
    if difference == 2:
        print(f"Computer chose {choice_name}. Computer wins.")
        score_computer += 1

#prints score when you enter "Q", says if you won, lost or tied
print("Computer:", score_computer, "\nYou:", score_player, "\nTies:", score_ties)
if score_player > score_computer:
    print("You won!")
    
elif score_player < score_computer:
    print("You lost.")

elif score_player == score_computer:
    print("You tied with computer!")
