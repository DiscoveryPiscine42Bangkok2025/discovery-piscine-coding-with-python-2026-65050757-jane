#!/usr/bin/env python3
import sys

base = [0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0]
plus = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0
j = 0
if len(sys.argv) - 1 == 0:
    while i < 11:
        j = 0
        if i == 0:
            print(f"Table de {i}: ", *base)
            i += 1
            continue
        while j < len(base) - 1:
            base[j + 1] = base[j + 1] + plus[j + 1]
            j += 1
        print(f"Table de {i}: ", *base)
        i += 1
else:
    print("none")


        