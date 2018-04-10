# Number Guessing Game
import sys
from random import randint
mystery_number = randint(1, 100)
print ("I am thinking of a number between 1 and 100...")
def game():
    global mystery_number
    guess = input ("What is your guess? ")
    if guess == "":
        print ("Invalid Answer. Try again.") # Invalid answers start here
        game()
    if int(guess) > 100:
        print ("Invalid Answer. Try again.")
        game()
    if int(guess) < 1:
        print ("Invalid answer. Try again.") # Invalid answers end here
        game()
        # This part tells the game whether the guess is lower or higher than the guess
    if int(guess) < int(mystery_number):
        lower()
    if int(guess) > int(mystery_number):
        higher()
    if int(guess) == int(mystery_number):
        win()
        
def lower():
    print ("WRONG! Think of a higher number.")
    game()

def higher():
    print ("WRONG! Think of a lower number.")
    game()

def win():
    print ("CORRECT! Congratulations, you win!!")
    input ("Press enter to exit...")
    sys.exit()

game()
