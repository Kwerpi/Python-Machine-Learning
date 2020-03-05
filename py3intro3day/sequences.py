#!/usr/bin/python3

ctemps = [-40, 0, 37, 75, 100]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

for tempC in ctemps:
    tempF = ((9*float(tempC)/5)+32)
    print(f"{tempC}\u2103  is {tempF}\u2109")

clean_fruits = [item.strip().lower() for item in fruits]
print(clean_fruits)