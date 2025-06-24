#!/usr/bin/env python

number = input("Give me a number: ")

answer = float(number)

if answer.is_integer():
    print("This number is an integer.")
else:
    print("This is a decimal number.")