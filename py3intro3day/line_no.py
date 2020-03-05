#!/usr/bin/python3

import sys

for filename in sys.argv[1:]:
    with open(filename,"r") as rfile:
        for num, line in enumerate(rfile.readlines(),1):
            print(f"{num} {line}")