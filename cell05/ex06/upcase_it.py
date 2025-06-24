#!/usr/bin/env python

import sys
parameters = sys.argv[1:]

if len(parameters) == 0:
    print("none")
else:
    print(parameters[0].upper())