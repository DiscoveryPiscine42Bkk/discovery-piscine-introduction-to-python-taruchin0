#!/usr/bin/env python

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
multiply_number = first_number * second_number
print(str(first_number) + " x " + str(second_number) + " = " + str(multiply_number))

if multiply_number < 0:
    print("The result is negative.")
elif multiply_number > 0:
    print("The result is positive.")
else :
    print("The result is zero.")