#!/usr/bin/env python


def is_valid_dna(sequence):
    if "N" or "X" in sequence:
        return(False)
    else:
        return(True)


def main():
    sequence = "ACGTNNNNNGTAGCACTACG"
    if is_valid_dna(sequence):
        print("Hell yeah!")
    else:
        print("No. So sorry.")


if __name__ == "__main__":
    main()