#!/usr/bin/env python3
import sys
import re

if len(sys.argv) - 1 > 1:
    first_arg = sys.argv[1]
    second_arg = sys.argv[2]

    print(len(re.findall(first_arg, second_arg)))
else:
    print("none")