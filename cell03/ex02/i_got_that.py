#!/usr/bin/env python
text = input("What you gotta say? : ")
while True:
    if text == "STOP":
        break
    print("I got that! Anything else? :", end=" ")
    text = input()