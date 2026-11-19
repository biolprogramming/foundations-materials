#!/usr/bin/env python

def power(nums):
    return nums**2


def main():
    nums = range(0,10)
    result = map(power, nums)
    # remember to talk about this for a minute!! remind me if i don't!
    print(list(result))

if __name__ == "__main__":
    main()