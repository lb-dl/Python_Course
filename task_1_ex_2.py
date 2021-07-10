"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""


import argparse


parser = argparse.ArgumentParser(description='Perform simple arithmetic operations')
parser.add_argument('operator', type=str, help='math function')
parser.add_argument('operand1', type=float, help='first operand')
parser.add_argument('operand2', type=float, help='second operand')


def calculate(args):

   operator = args.operator
   operand1 = args.operand1
   operand2 = args.operand2

   math_operations = {
       'add': lambda op1, op2: op1+op2,
       'sub': lambda op1, op2: op1-op2,
       'mul': lambda op1, op2: op1*op2,
       'truediv': lambda op1, op2: op1/op2,
       'floordiv': lambda op1, op2: op1 // op2,
       'pow': lambda op1, op2: op1**op2,
       'mod': lambda op1, op2: op1 % op2,
       'lt': lambda op1, op2: op1 < op2,
       'gt': lambda op1, op2: op1 > op2,
       'le': lambda op1, op2: op1 <= op2,
       'ge': lambda op1, op2: op1 >= op2,
       'eq': lambda op1, op2: op1 == op2,
       'ne': lambda op1, op2: op1 != op2,
       'is_': lambda op1, op2: op1 is op2,
       'is_not': lambda op1, op2: op1 is not op2,
       'and_': lambda op1, op2: op1 & op2,
       'xor': lambda op1, op2: op1 ^ op2,
       'or_': lambda op1, op2: op1 | op2,
       'lshift': lambda op1, op2: op1 << op2,
       'rshift': lambda op1, op2: op1 >> op2,
       'matmul': lambda op1, op2: op1@op2
   }

   if operand2 == 0 and (operator == 'truediv' or operator == 'floordiv'):
       raise ZeroDivisionError(f'Division by zero not implemented')
   if operation := math_operations.get(operator):
       return operation(operand1, operand2)
   raise NotImplementedError(f'Passed operation {operator} not implemented')

def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
