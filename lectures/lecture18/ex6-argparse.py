#!/usr/bin/env python

import argparse

def main():
    parser = argparse.ArgumentParser(description="This is a test of argparse.")
    parser.add_argument("foo", type=int, help="This is an integer value")
    parser.add_argument("baz", type=str, help="This is a string value")
    parser.add_argument("bar", type=float, help="This is a floating point value")
    args = parser.parse_args()
    print(args.foo)
    print(type(args.foo))
    print(args.baz)
    print(type(args.baz))
    print(args.bar)
    print(type(args.bar))
    

if __name__ == "__main__":
    main()