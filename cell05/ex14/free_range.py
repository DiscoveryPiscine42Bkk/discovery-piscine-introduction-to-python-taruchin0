#!/usr/bin/env python

import sys
parameters = sys.argv

if len(parameters) -1 != 2:
    print("none")
else:
    numbers = []
    number1 = int(parameters[1])
    number2 = int(parameters[2])
    for i in range(number1, number2+1):
        numbers.append(i)
    print(numbers)
