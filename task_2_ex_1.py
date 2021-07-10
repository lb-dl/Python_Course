"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""
import argparse
from itertools import chain, combinations

parser = argparse.ArgumentParser(description='Find the maximum capacity')
parser.add_argument('-W', '--capacity', type=int, help='capacity of a knapsack ')
parser.add_argument('-w', '--weights',  nargs='+', help='list of weights')
parser.add_argument('-n', '--number', type=int, help='the number of gold bars')

def bounded_knapsack(args):

    capacity = args.capacity
    weights = [int(weight) for weight in args.weights]
    number = args.number

    if number != len(weights) or number < 0 or capacity < 0:
        raise ValueError
    if any(weight < 0 for weight in weights):
        raise ValueError

    sum_of_weights = sum(weights)
    if sum_of_weights <= capacity:
        return sum_of_weights

    list_of_weights_comb = list(chain.from_iterable(combinations(weights, r) for r in range(number + 1)))
    max_sum = 0
    for i in list_of_weights_comb:
        sum_of_subset = sum(i)
        if sum_of_subset <= capacity:
            max_sum = max(sum_of_subset, max_sum)
    return max_sum


def main():

    args = parser.parse_args()
    print(bounded_knapsack(args))


if __name__ == '__main__':
    main()
