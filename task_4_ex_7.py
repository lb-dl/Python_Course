"""
Task04_1_7
Implement a function foo(List[int]) -> List[int] which, given a list of integers, returns a new  or modified list
in which every element at index i of the new list is the product of all the numbers in the original array except the one at i.
Example:
`python

foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

foo([3, 2, 1])
[2, 3, 6]`
"""

import math
from typing import List


def product_array(num_list: List[int]) -> List[int]:
    list_of_products = []
    for i in range(0, len(num_list)):
        temp_list = num_list[:i]+num_list[i+1:]
        result = math.prod(temp_list)
        list_of_products.append(result)
    return list_of_products
