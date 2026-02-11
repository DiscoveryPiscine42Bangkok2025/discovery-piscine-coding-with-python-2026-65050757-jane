#!/usr/bin/env python3
import sys
import re

if len(sys.argv) - 1 > 0:
    inp = input("What was the parameter? ")
    matching_count = len(re.findall(inp, sys.argv[1]))
    if matching_count > 0:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")