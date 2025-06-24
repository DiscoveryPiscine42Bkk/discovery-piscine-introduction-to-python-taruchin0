#!/usr/bin/env python

import sys
parameter = sys.argv
if len(parameter) != 2:
    print("none")
else:
    password = parameter[1]
    word = input("What was the parameter?").strip()
    
    if word == password:
       print("Good job!")
    else :
       print("Nope, sorry...")