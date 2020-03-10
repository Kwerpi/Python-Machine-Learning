#!/usr/bin/python3

spam = [ 
    "Spam", 
    "eggs  ",
    "   spam    ",
    "     spam spam     ", 
    "SPAM	", 
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

def cleanup(input):
    return input.strip().lower()

for item in spam:
    print(f"before : {item}")
    item = cleanup(item)
    print(f"after  : {item}")