#!/usr/bin/python3

import sys


if len(sys.argv) > 2:
    word = sys.argv[1]
    for rfile in sys.argv[2:]:
        count = 0
        with open(rfile,"r") as afile:
            for line in afile.readlines():
                if word.lower() in line.lower():
                    count+=1
        print(count)
else:
    count = 0
    with open("DATA/alice.txt","r") as afile:
        for line in afile.readlines():
            if "Alice" in line:
                count+=1
    print(count)
