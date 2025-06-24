#!/usr/bin/env python

import sys
parameters = sys.argv[1:]

if len(parameters) < 2:
    print("none")
else:
    print(' '.join(reversed(parameters)))