#!/usr/bin/env python

def power(nums):
    result = []
    for num in nums:
        result.append(num**2)
    return result


def main():
    nums = range(0,10)
    result = power(nums)
    print(result)

if __name__ == "__main__":
    main()
