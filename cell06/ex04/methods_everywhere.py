#!/usr/bin/env python

import sys
parameters = sys.argv

def shrink(text):
    return text[:8]

def enlarge(text):
    n = len(text)
    for i in range(n, 8):
        text+='Z'
    return text

if len(parameters) <= 1:
    print('none')
else:
    for i in range (1, len(parameters)):
        if len(parameters[i])<8:
            print(enlarge(parameters[i]))
        elif len(parameters[i])>8:
            print(shrink(parameters[i]))
        else:
            print(parameters[i])

