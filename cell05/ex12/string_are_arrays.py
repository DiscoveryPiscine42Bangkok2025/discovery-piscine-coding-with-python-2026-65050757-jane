#!/usr/bin/env python3
import sys

if len(sys.argv) - 1 > 0:
    if 'z' in sys.argv[1]:
        for char in sys.argv[1]:
            if char == 'z':
                print("z", end='')
        print()
    else:
        print("none")
else:
    print("none")