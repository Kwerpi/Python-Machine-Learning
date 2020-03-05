#!/usr/bin/python3

import sys

if len(sys.argv) > 1:
    max_val = sys.argv[1]
else:
    max_val = input("Enter maximum number: ")

min_val = 0
cont = True

while cont:
    my_guess = (int(max_val) + min_val)//2 
    hint = input(f"is {my_guess} your number? ")
    if(hint.lower() == 'y'):
        cont = False
    elif(hint.lower() == 'l'):
        min_val = my_guess
    elif(hint.lower() == 'h'):
        max_val = my_guess
    else:
        print("Invalid input!")