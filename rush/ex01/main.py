#!/usr/bin/env python3

import sys 
from checkmate import checkmate

def main():
    #check input in terminal
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            try:
                with open(filename, "r") as f:
                    board = f.read()
                    checkmate(board)
            except Exception: #if no board in input
                print("Error: file cannot be read")

if __name__ == "__main__":
    main()
