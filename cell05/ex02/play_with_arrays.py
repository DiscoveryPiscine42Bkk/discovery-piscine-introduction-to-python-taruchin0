#!/usr/bin/env python

Original_arrays = [-11, 45, 23, -87, 2, 30]
New_arrays = []
for number in Original_arrays:
    New_arrays.append(number + 2)
for number in New_arrays:
    if number > 5:
        print(number, end=' ')
print()