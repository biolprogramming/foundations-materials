#!/usr/bin/env python

def get_user_input():
    result = input("Please provide some input here: ")
    return result

def main():
    result = get_user_input()
    print(result)
    # we can do some things to the input, but what we do is sort of limited
    rs = result.split(" ")
    print(rs)

if __name__ == "__main__":
    main()