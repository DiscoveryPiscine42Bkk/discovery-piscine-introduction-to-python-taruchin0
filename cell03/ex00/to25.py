#!/usr/bin/env python

number = int(input("Enter a number less than 25: "))

if number > 25:
    print("Error")
else:
    while(number < 26):
        print("Inside the loop, my variable is " , number)
        number += 1