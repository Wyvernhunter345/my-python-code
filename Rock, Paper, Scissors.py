# Rock, Paper, Scissors
# Setup
from random import randint
import sys
from time import sleep
mystery_action = randint(1,3)
score = 0
opponent_score = 0
print ("Note: 1 is Rock, 2 is paper, 3 is scissors. Type the phrase \"endgame\" to end the game.")
# All the code underneath "def gameloop()" is the entire game except for the while True function; the "def" command is assigning the code to "gameloop()"
def gameloop():
    global mystery_action
    global opponent_score
    global score
    mystery_action = randint(1,3)
    selected_action = input ("Rock, Paper or Scissors? ")
    if selected_action == "rock":
         if mystery_action == 1:
            print ("Tie! The opponent chose Rock.")
         if mystery_action == 2:
            print ("You lost! The opponent chose Paper.")
            opponent_score += 1
         if mystery_action == 3:
            print ("You won! The opponent chose Scissors.")
            score += 1
    elif selected_action == "paper":
         if mystery_action == 1:
            print ("You won! The opponent chose Rock.")
            score += 1
         if mystery_action == 2:
            print ("Tie! The opponent chose Paper.")
         if mystery_action == 3:
            print ("You lost! The opponent chose Scissors.")
            opponent_score += 1
    elif selected_action == "scissors":
         if mystery_action == 1:
            print ("You lost! The opponent chose Rock.")
            opponent_score += 1
         if mystery_action == 2:
            print ("You won! The opponent chose Paper.")
            score += 1
         if mystery_action == 3:
            print ("Tie! The opponent chose Scissors.")
    elif selected_action == "endgame":
        print ("Thanks for playing! You won " + str(score) + " game(s) and the opponent won " + str(opponent_score) + " game(s). GG!")
        sleep(5)
        sys.exit()
    elif "rock" not in selected_action or "paper" not in selected_action or "scissors" not in selected_action or "endgame" not in selected_action:
        print ("That is not a valid action.")
# The loop that keeps it running
while True:
    gameloop()


# Copyright Jaiden Spencer 2016© All rights reserved.
        
        
    

        
