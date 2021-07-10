"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('roman_numeral', type=str, help='Converting a given Roman numeral into Arabic one')


def from_roman_numerals(args):
    numerals = (
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    )
    roman_numeral = args.roman_numeral

    if len(roman_numeral) > 1 and roman_numeral[0] == 'C':
        raise ValueError
    for elem in roman_numeral:
        if elem not in ['I', 'V', 'X', 'C', 'L']:
            raise ValueError

    result = 0
    index = 0

    for numeral, integer in numerals:
        while roman_numeral[index:index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result


def main():
    args = parser.parse_args()
    print(from_roman_numerals(args))


if __name__ == "__main__":
    main()
