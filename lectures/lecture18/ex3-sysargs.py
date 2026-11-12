#!/usr/bin/env python

import sys

def main():
    print(sys.argv)
    # this is a list so you can access each element like:
    print("this is the first (not zero'th argument)")
    print(sys.argv[1])
    

if __name__ == "__main__":
    main()