#!/usr/bin/env python3
import sys

str_added = "ism"

if len(sys.argv) - 1 > 0:
    end = ""
    for argv in sys.argv:
        if argv[-3:] == str_added:
            continue
        else:
            argv += str_added
            print(argv)
            
else:
    print("none")