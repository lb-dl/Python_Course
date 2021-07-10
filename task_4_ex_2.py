"""
Task04_1_2
Write `is_palindrome` function that checks whether a string is a palindrome or not
Returns 'True' if it is palindrome, else 'False'

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

Note:
Usage of any reversing functions is prohibited.
The function has to ignore special characters, whitespaces and different cases
Raise ValueError in case of wrong data type
"""
import math

def is_palindrome(test_string: str) -> bool:

    if not isinstance(test_string, str):
        raise ValueError

    test_string = test_string.lower()
    clear_string = ''.join([elem for elem in test_string if elem.isalnum()])
    result = None

    for i in range(0, math.floor(len(clear_string) / 2)):
        if clear_string[i] != clear_string[len(clear_string) - 1 - i]:
            result = False
            break
        else:
            result = True

    return result
