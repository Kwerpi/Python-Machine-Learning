#!/usr/bin/python3

with open("DATA/alt.txt","r") as rfile:
    afile = open("a.txt","w")
    bfile = open("b.txt","w")
    for line in rfile.readlines():
        if line.startswith("a"):
            afile.write(f"{line}\n")
        elif line.startswith("b"):
            bfile.write(f"{line}\n")
    afile.close()
    bfile.close()