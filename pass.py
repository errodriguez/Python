#! /usr/bin/env python

counter = 0 
pass_1 = str(input("Password: "))
while True:
    pass_2 = str(input("Repeat password: "))
    counter += 1
    if pass_1 == pass_2:
        print("User account created!")
        break
    else:
        print("They do not match!")
        if counter == 3:
            print("Too many tries.")
            break
