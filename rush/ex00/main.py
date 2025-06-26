#!/usr/bin/env python3

import sys
from checkmate import checkmate

def main():
    
    if len(sys.argv) == 1:
        board = """\
....
...K
..P.
....\
"""
        checkmate(board)
    else:
        for filename in sys.argv[1:]:
            try:
                with open(filename, "r") as f:
                    board = f.read()
                    checkmate(board)
            except Exception:
                print("Error")

if __name__ == "__main__":
    main()
