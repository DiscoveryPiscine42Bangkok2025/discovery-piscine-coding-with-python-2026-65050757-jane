#!/usr/bin/env python3

import sys

if len(sys.argv) - 1 > 2:
    for arg in range(len(sys.argv) - 1, 0, -1):
        print(sys.argv[arg])
else:
    print("none")