#!/usr/bin/env python

def downcase_it(text):
    return text.lower()

import sys
parameters = sys.argv
if len(parameters) == 1:
        print("none")
else:
    for i in range(1 , len(parameters)):
        print(downcase_it(parameters[i]))
