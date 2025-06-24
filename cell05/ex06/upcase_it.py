#!/usr/bin/env python

import sys
parameters = sys.argv[1:]

if len(parameters) != 1:
    print("none")
else:
    print(parameters[0].upper())