#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    max_val = int(sys.argv[1])+1
else:
    max_val = 1001

# is_prime = [True] * max_val

# for num in range(2,max_val):
#     if is_prime[num]:
#         print(f"{num} is prime")
#         for num2 in range(num,max_val,num):
#             is_prime[num2] = False

is_prime = set()
for num in range(2,max_val):
    if num not in is_prime:
        print(f"{num} is prime")
        for num2 in range(num,max_val,num):
            is_prime.add(num2)
