#!/usr/bin/python3
alist = list()
blist = list()
with open('DATA/alt.txt','r') as rfile:
    for line in rfile.readlines():
        if line.startswith('a'):
            alist.append(line)
        elif line.startswith('b'):
            blist.append(line)

with open('DATA/a_sorted.txt','w') as afile:
    for aline in sorted(alist):
        afile.write(f"{aline}\n")

with open('DATA/b_sorted.txt','w') as bfile:
    for bline in sorted(blist, reverse=True):
        bfile.write(f"{bline}\n")