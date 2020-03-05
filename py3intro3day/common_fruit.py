#!/usr/bin/python3

with open("DATA/fruit1.txt","r") as ffile1, open("DATA/fruit2.txt","r") as ffile2:
    fset1 = {line.lower().strip() for line in ffile1.readlines()}
    fset2 = {line.lower().strip() for line in ffile2.readlines()}

print(fset1 & fset2)