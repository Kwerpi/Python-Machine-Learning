#!/usr/bin/python3

# sorted by name case-sensitively
# with open('DATA/fruit.txt','r') as fruit_file:
#     for line in sorted(fruit_file.readlines()):
#         print(line)

#sorted by name case-insensitively
# with open('DATA/fruit.txt','r') as fruit_file:
#     for line in sorted(fruit_file.readlines(), key=lambda e : e.lower()):
#         print(line)

#sorted by length of name, then by name
# with open('DATA/fruit.txt','r') as fruit_file:
#     for line in sorted(fruit_file.readlines(), key=lambda e : (len(e), e.lower())):
#         print(line)

#sorted by the 2nd letter of the name, then the first letter
with open('DATA/fruit.txt','r') as fruit_file:
    for line in sortled(fruit_file.readlines(), key=lambda e : (e[1].lower(),e[0].lower()) ):
        print(line) 