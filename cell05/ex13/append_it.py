#!/usr/bin/env python

import sys
parameters = sys.argv[1:]

if len(parameters) != 1:
    print("none")
else:
    word = input(parameters)
    if word == 'ism':
        print("")
    else:
         print(word, +"ism")
