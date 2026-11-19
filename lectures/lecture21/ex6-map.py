def power(nums, power):
    return nums**power


def main():
    nums = range(0,10)
    result = map(power, nums, [4]*len(nums))
    print(list(result))

if __name__ == "__main__":
    main()