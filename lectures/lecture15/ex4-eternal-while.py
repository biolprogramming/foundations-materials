#!/usr/bin/env python


def main():
    while True:
        response = input("What is the velocity of an unladen sparrow? ")
        if 13.0 <= float(response) < 14.0:
            break
        else:
            print(response)
    print("Correct!")


if __name__ == "__main__":
    main()