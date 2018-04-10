def inputpassword():
    password = 1234
    password_ask = input ("Password: ")
    if int(password_ask) != int(password):
        print ("Incorrect Password!")
        inputpassword()
    elif int(password_ask) == int(password):
        print ("Correct! You now have access.")
inputpassword()
'''Insert what you want after the password here :)
If you want a different password, change the variable "password" \
to something different.
If you want a password that includes letters, change the int() functions around
the password to str().'''


    
    
