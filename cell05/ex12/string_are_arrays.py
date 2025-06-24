#!/usr/bin/env python

import sys
parameters = sys.argv[1:]

if len(parameters) != 1 or 'z' not in parameters[0]:
    print("none")
else:
    for char in parameters[0]:
        if char == 'z':
            print("z", end='')
    print()