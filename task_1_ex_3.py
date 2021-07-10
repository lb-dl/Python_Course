""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Sign = '+' | '-'
Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("user_input")


def check_formula(args):

    try:

        formula = args.user_input
        if formula[0] in ['+', '-']:
            return False, None
        formula_replaced = formula.replace('-','+')
        formula_splited = formula_replaced.split('+')
        if ' ' in formula_splited:
            return False, None
        return True, eval(formula)
    except:
        return False, None

def main():

    args = parser.parse_args()  # Hint: use methods from argparse module
    print(check_formula(args))


if __name__ == '__main__':
    main()
