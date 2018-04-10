# The best game in the history of the univers (or something)
level = 1
xp = 0


    
import sys

def start():
    global xp
    print ("Note: If the game requires you to answer, make sure you answer in lower-case letters, with no punctuation, except for yes or no. Thanks!")
    print ("Hello " + name + "! You have been selected to help a hero on his journey to find treasure.")

def begin():
    print ("Brilliant! For your bravery, you have been given an iron sword to help out on your journey. Good luck!!")

def bossfight():
    global xp
    global level
    choice6 = input ("What do you do? fight/run: ")
    if choice6 == "run":
        bfrun()
    if choice6 == "fight":
        print ("You bravely stand up to the monster and accept the fight. The battle is on!!")
        print ("You are fighting him, dodging most of his attacks. Then, when he is low health, he forces you to the ground with his giant hand!!")
        print (" You are thinking \"This is the end, This is the end!\"  When you suddenly get an idea!")
        choice7 = input ("Is your idea to fight or to run? fight/run: ")
        if choice7 == "fight":
            print ("You sneak out of his hand while he is laughing. Then, just before he realises, you jump and deliver the final blow! He falls to the ground with a great thud. Great job, " + name + " ! +120 xp!")
            xp += 120
            if xp >= 100:
                level += 1
                xp = xp - 100
                print("Congratulations! you have ranked up to level " + str(level) + "! Good work.")
            print ("You now have " + str(xp) + " xp!")
            input ("Press enter to continue...")
        if choice7 == "run":
            print ("You decide to sneak out of his hand while he is laughing. It works! You manage to run away in time before he realises. +50 xp.")
            xp += 50
            if xp >= 100:
                level += 1
                xp = xp - 100
                print("Congratulations! you have ranked up to level " + str(level) + "! Good work.")
            print ("You now have " + str(xp) + " xp!")
        
def bfrun():
    print ("You try to run, but the monster grabs and pulls you back into the fight. There's no escape this time!")
    bossfight()
    
def choiceright():
    print ("You go right. You come across a mysterious house.")

def choiceright2():
    print ("You push the door. It's stuck. Bad Luck.")
    input ("Press enter to continue..")
    global xp
    xp += 10
    print ("But that's not it! You give the door a hard kick. It opens. You decide to have a walk around.")
    print ("You don't find anything, but you feel more confident now that you kicked open the door. +10 xp.")
    print ("You now have " + str(xp) + " xp!")
    input ("Press enter to continue...")

# Definitions end here
# Game starts here
    
name = input ("Please enter your name/nickname before you start: ")
start()
choice = input ("Will you help him? Y/N: ")
if choice == "Y":
    begin()
if choice == "N":
    print ("Oh well. See you next time!")
    input ("Press Enter to exit...")
    sys.exit()

print ("Your hero leaves base. The path splits into two directions.")
choice2 = input ("Which way do you choose? left/right: ")
if choice2 == "left":
    print ("Dead end. You head back and turn right.")
    input ("Press enter to continue...")
    choiceright()
if choice2 == "right":
    choiceright()

choice3 = input ("Do you wish to venture into the house? Y/N: ")
if choice3 == "Y":
    choiceright2()

if choice3 == "N":
    print ("You ignore the house. it will probably be no use to you anyway.")
    input ("Press enter to continue...")

print ("The path leads you into a dark forest. Suddenly, a tree slime jumps in front of you! It looks as if it's made out of demonicus acid, an extremely corrosive acid.")
choice4 = input ("What do you do? fight/run: ")
if choice4 == "fight":
    print ("You slice the slime in half with your sword. The acid soaks into the ground. You are very happy you killed your first enemy. +50 xp.")
    xp += 50
    print ("You now have " + str(xp) + " xp!")
    if xp >= 100:
        level += 1
        xp = xp - 100
        print("Congratulations! you have ranked up to level " + str(level) + "! Good work.")
    input ("Press enter to continue...")
    
if choice4 == "run":
    print ("You run as fast as your legs can take you. Fortunately, the slime is not fast enough, and you escape safely. +20 xp.")
    xp += 20
    print ("You now have " + str(xp) + " xp!")
    input ("Press enter to continue...")
    if xp >= 100:
        level += 1
        xp = xp - 100
        print("Congratulations! you have ranked up to level " + str(level) + "! Good work.")
           
print  ("The path continues through the forest, until it comes to an abrupt stop.")
choice5 = input ("What do you do? continue/turn_back: ")
if choice5 == "continue":
    print ("You feel a strong surge of bravery. Your body encourages you to move on. You decide bravely to move on.")

if choice5 == "turn_back":
    print ("You decide to stop here. Better be on the safe side! You turn and head back home.")
    print ("When you reach home, you have a nice rest and help yourself to some food. Although it was (VERY) disappointing that you didn't find treasure, you sure felt comfortable here. Good job, " + name + " !")
    print ("The End!")
    print ("Your final amount of xp was " + str(xp) + " !")
    print ("Programmming and design: Jaiden Spencer")
    print ("Character Design: Jaiden Spencer")
    input ("Press enter to continue...")
    sys.exit()

print ("You make your way through the forest until you come to a clearing. It' s a beautiful view! But not until the Giant Goblin Monster jumps in front of you!")
print ("This is your first boss. He is much harder than normal enemies and he is much harder to attack.")
input ("Press enter to FIGHT...")
bossfight()



