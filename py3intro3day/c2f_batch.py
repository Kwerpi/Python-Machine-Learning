#!/usr/bin/python3

import sys

for tempC in sys.argv[1:]:
    tempF = ((9*float(tempC)/5)+32)
    print(f"{tempC}\u2103  is {tempF}\u2109")
        