"""
Write a function `fibonacci_loop(seq: list)`, which accepts a list of values and
prints out values in one line on these conditions:
 - floating point numbers should be ignored
 - string values should stop the iteration
 - loop control statements should be used

Example:
>>> fibonacci_loop([0, 1, 1.1, 1, 2, 99.9, 3, 0.0, 5, 8, "stop", 13, 21, 34])
0 1 1 2 3 5 8
"""


def fibonacci_loop(seq):
    result = []
    for elem in seq:
        if isinstance(elem, float):
            continue
        elif isinstance(elem, str):
            break
        else:
            result.append(elem)
    print(*result)
