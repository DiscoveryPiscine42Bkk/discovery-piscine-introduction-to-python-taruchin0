#!/usr/bin/env python

Original_arrays = [2 , 8 , 9 , 48 , 8 , 22 , -12 , 2]
New_arrays = set()
for number in Original_arrays:
    if number > 5:
        New_arrays.add(number+2)
print(Original_arrays)
print(New_arrays)