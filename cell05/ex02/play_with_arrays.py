#!/usr/bin/env python

Original_arrays = [2 , 8 , 9 , 48 , 8 , 22 , -12 , 2]
New_arrays = []
for number in Original_arrays:
    New_arrays.append(number + 2)
for number in New_arrays:
    if number > 5:
        print(number, end=' ')
print()