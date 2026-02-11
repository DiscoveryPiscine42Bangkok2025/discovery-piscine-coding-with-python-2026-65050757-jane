#!/usr/bin/env python3

import sys

if len(sys.argv) - 1 > 0:
    lower_args = []
    for arg in sys.argv[1:]:
        lower_args.append(arg.lower())
    print(*lower_args)
else:
    print("none")