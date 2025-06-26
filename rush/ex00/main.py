#!/usr/bin/env python3

import sys 
from checkmate import checkmate

def main():
    #check input in terminal
    if len(sys.argv) == 1:
        board = """\
....
...K
....
....\
"""
        checkmate(board)
if __name__ == "__main__":
    main()
