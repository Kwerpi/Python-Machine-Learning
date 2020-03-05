#!/usr/bin/python3

while True:
    try:
        tempC = input("Enter Celsius: ")
        if tempC.lower() == 'q':
            exit(0)
        tempF = ((9*float(tempC)/5)+32)
        print(f"{tempC}\u2103  is {tempF}\u2109")
    except ValueError:
        print("Invalid Input!")