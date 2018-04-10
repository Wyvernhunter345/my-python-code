# MATH GAME
from random import randint
from time import sleep
import sys
score = 0
# Numbers start here

# Question 1
ans_a = randint(1, 12)
ans_b = randint(1, 12)

# Question 2
ans_c = randint(1, 12)
ans_d = randint(1, 12)

# Question 3
ans_e = randint(1, 12)
ans_f = randint(1, 12)

# Question 4
ans_g = randint(1, 12)
ans_h = randint(1, 12)

# Question 5
ans_i = randint(1, 12)
ans_j = randint(1, 12)

# Question 6
ans_k = randint(1, 12)
ans_l = randint(1, 12)

# Question 7
ans_m = randint(1, 12)
ans_n = randint(1, 12)

# Question 8
ans_o = randint(1, 12)
ans_p = randint(1, 12)

# Question 9
ans_q = randint(1, 12)
ans_r = randint(1, 12)

# Question 10
ans_s = randint(1, 12)
ans_t = randint(1, 12)

# Numbers end here

# Intro starts here

print ("Welcome to the maths game!")
sleep(3)
print ("You will be given 10 multiplication questions.")
sleep(3)
print ("Your score will be shown at the end.")
sleep(3)
print ("Enjoy!")
sleep(3)
# Intro ends here
# Game starts here
print ("First question:") # First question
sleep(1)
answer_1 = input ("What is " + str(ans_a) + " x " + str(ans_b) + "? ")
if int(answer_1) == ans_a * ans_b:
    print ("Correct! +1 point!")
    score += 1
if int(answer_1) != ans_a * ans_b:
    print ("Incorrect! No points awarded.")
sleep(4)
print ("Second question:") # Second question
sleep(1)
answer_2 = input ("What is " + str(ans_c) + " x " + str(ans_d) + "? ")
if int(answer_2) == ans_c * ans_d:
    print ("Correct! +1 point!")
    score += 1
if int(answer_2) != ans_c * ans_d:
    print ("Incorrect! No points awarded.")
sleep(4)
print ("Third question:") # Third question
sleep(1)
answer_3 = input ("What is " + str(ans_e) + " x " + str(ans_f) + "? ")
if int(answer_3) == ans_e * ans_f:
    print ("Correct! +1 point!")
    score += 1
if int(answer_3) != ans_e * ans_f:
    print ("Incorrect! No points awarded.")
sleep(4)
print ("Fourth question:") # Fourth question
sleep(1)
answer_4 = input ("What is " + str(ans_g) + " x " + str(ans_h) + "? ")
if int(answer_4) == ans_g * ans_h:
    print ("Correct! +1 point!")
    score += 1
if int(answer_4) != ans_g * ans_h:
    print ("Incorrect! No points awarded.")
sleep(4)
print ("Fifth question:") # Fifth question
sleep(1)
answer_5 = input ("What is " + str(ans_i) + " x " + str(ans_j) + "? ")
if int(answer_5) == ans_i * ans_j:
    print ("Correct! +1 point!")
    score += 1
if int(answer_5) != ans_i * ans_j:
    print ("Incorrect! No points awarded.")
sleep(4)
print ("Sixth question:") # Sixth question
sleep(1)
answer_6 = input ("What is " + str(ans_k) + " x " + str(ans_l) + "? ")
if int(answer_6) == ans_k * ans_l:
    print ("Correct! +1 point!")
    score += 1
if int(answer_6) != ans_k * ans_l:
    print ("Incorrect! No points awarded.")
sleep(4)
print ("Seventh question:") # Seventh question
sleep(1)
answer_7 = input ("What is " + str(ans_m) + " x " + str(ans_n) + "? ")
if int(answer_7) == ans_m * ans_n:
    print ("Correct! +1 point!")
    score += 1
if int(answer_7) != ans_m * ans_n:
    print ("Incorrect! No points awarded.")
sleep(4)
print ("Eighth question:") # Eighth question
sleep(1)
answer_8 = input ("What is " + str(ans_o) + " x " + str(ans_p) + "? ")
if int(answer_8) == ans_o * ans_p:
    print ("Correct! +1 point!")
    score += 1
if int(answer_8) != ans_o * ans_p:
    print ("Incorrect! No points awarded.")
sleep(4)
print ("Ninth question:") # Ninth question
sleep(1)
answer_9 = input ("What is " + str(ans_q) + " x " + str(ans_r) + "? ")
if int(answer_9) == ans_q * ans_r:
    print ("Correct! +1 point!")
    score += 1
if int(answer_9) != ans_q * ans_r:
    print ("Incorrect! No points awarded.")
sleep(4)
print ("Last question:") # Last question
sleep(1)
answer_10 = input ("What is " + str(ans_s) + " x " + str(ans_t) + "? ")
if int(answer_10) == ans_s * ans_t:
       print ("Correct! +1 point!")
       score += 1
if int(answer_10) != ans_s * ans_t:
       print ("Incorrect! No points awarded.")
sleep(4)
# Questions ends here
# Ending starts here
print ("Game over!")
sleep(2)
if int(score) == 10:
       print ("Astounding job! You appear to be excellent with your Times Tables. You scored " + str(score) + " !")
if int(score) > 5:
       print ("Good job! Could do better. Remember, there's always room for improvement! Your scored " + str(score) + "!")
if int(score) < 5:
       print ("You did an OK job, a little more practice could be in order. You scored " + str(score) + "!")
if int(score) == 0:
       ("Are you even awake? Times tables should be your main priority now. You scored " + str(score) + ".")
sleep(3)
print ("Thanks for playing my game. Goodbye!")
sleep(2)
print ("Credits:")
print ("Programming: Jaiden")
print ("Design : Jaiden")
print ("Idea: Jaiden")
sleep(6)
sys.exit()      
       
