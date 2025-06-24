#!/usr/bin/env python

Original_arrays = [-11, 45, 45, 23, 23, -87, 2, 30]
New_arrays = [number + 2 for number in Original_arrays]

New_arrays = set()
Duplicate = set()

for number in New_arrays:
    if number in New_arrays:
        Duplicate.add(number)
    else:
        New_arrays.add(number)
result = [number for number in New_arrays if number not in Duplicate and number > 5]
for number in result:
    print(number, end=' ')