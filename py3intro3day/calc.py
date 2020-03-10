#!/usr/bin/python3

def add(x, y):
    return int(x) + int(y)

def sub(x, y):
    return int(x) - int(y)

def div(x, y):
    if int(y) == 0:
        return "Cannot divide by zero!"
    else:
        return int(x) / int(y)

def mul(x, y):
    return int(x) * int(y)

def pow2(x, y):
    return int(x) ** int(y)

def root(x, y):
    return int(x) ** (1/int(y))

funcs = {'+':add, '-':sub, '/':div, '*':mul, '^':pow2, '~':root}

while True:
    myinput = input("Enter operation: ")
    if myinput.lower() == 'q':
        exit(0)
    else:
        x, op, y = myinput.split()
        out = funcs[op](x,y)
        print(f"{x} {op} {y} = {out}")