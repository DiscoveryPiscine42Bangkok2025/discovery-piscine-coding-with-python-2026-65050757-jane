#!/usr/bin/env python3

import sys

if len(sys.argv) - 1 > 0:
    upper_args = []
    for arg in sys.argv[1:]:
        upper_args.append(arg.upper())
    print(*upper_args)
else:
    print("none")