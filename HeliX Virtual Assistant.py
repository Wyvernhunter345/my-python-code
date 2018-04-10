# HeliX Virtual Assistant
import sys
from time import sleep
import webbrowser
from random import randint
url = "https://www.google.com"
print ("Hello! I am HeliX, Your virtual assistant. Just a little note before I can answer your questions. You can use punctuation with your questions, but no Question Marks or caps. Enjoy!")
print ("Excuse me if I have a few glithes. I am a WiP (Work in progress). My programmer will fix them as soon as he can (ask me \"who made you\" for more info!).")
def helix_main():
    helix_question = input ("What can I do for you? ")
    if helix_question == "hello":
        print ("Hello! I am HeliX, a WiP virtual assistant.")
        helix_main()
    if helix_question == "hi":
        print ("Hello! I am HeliX, a WiP virtual assistant.")
        helix_main()
    if helix_question == "time":
        print ("Really? if you wanna know, Look in the bottom right corner.")
        helix_main()
    if helix_question == "what is the time":
        print ("Really? if you wanna know, Look in the bottom right corner.")
        helix_main()
    if helix_question == "date":
        print ("Really? if you wanna know, Look in the bottom right corner.")
        helix_main()
    if helix_question == "what is the date":
        print ("Really? if you wanna know, Look in the bottom right corner.")
        helix_main()
    if helix_question == "help":
        print ("Maybe try \"hi/hello\", \"what is the time\", \"who made you\", \"what is this laptop's version\" or maybe even \"open google\"!")
        helix_main()
    if helix_question == "what is this laptop's version":
        print ("This a 64-bit Windows 10 computer running an Intel Core i5 chip.")
        helix_main
    if helix_question == "exit":
        print ("Goodbye. Glad to make your acquaintance.")
        sleep(2)
        sys.exit()
    if helix_question == "bye":
        print ("Goodbye. Glad to make your acquaintance.")
        sleep(2)
        sys.exit()
    if helix_question == "goodbye":
        print ("Goodbye. Glad to make your acquaintance.")
        sleep(2)
        sys.exit()
    if helix_question == "who made you":
        print ("Jaiden Spencer made and programmed me to be who I am now. Give all credit to him.")
        helix_main()
    if helix_question == "tell me a joke":
        print ("Why DIDN'T the skeleton cross the road?")
        sleep(2)
        print ("Because he didn't have the guts.")
        helix_main()
    if helix_question == "open google":
        print ("With pleasure...")
        webbrowser.open_new(url)
        print ("(Look down in your taskbar for your web browser. it should be flashing.)")
        helix_main()
    if helix_question == "flip a coin":
        coin = randint(1,2)
        if coin == 1:
            print ("Heads.")
            coin = randint(1,2)
        elif coin == 2:
            print ("Tails.")
            coin = randint(1,2)
        helix_main()
    if helix_question == "game":
        print ("Ok, here goes...")
        def game():
             fingers = randint(1,10)
             game_guess = input ("How many fingers am I holding up? (I will change fingers every guess!): ")
             if int(game_guess) == fingers:
                 print ("Correct! Good game.")
                 helix_main()
             if int(game_guess) != fingers:
                 print ("Incorrect! Try again.")
                 fingers = randint(1,10)
                 game()
        game()
        
        
    else:
        print ("That is an invalid question. I am currently a work in progress. Type \"help\" for some things you could ask me.")
        helix_main()
helix_main()
