"""
Write a function that checks whether a string is a palindrome or not.
Return 'True' if it is a palindrome, else 'False'.

Note:
Usage of reversing functions is required.
Raise ValueError in case of wrong data type

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
"""


def is_palindrome(test_string: str) -> bool:
    if not isinstance(test_string, str):
        raise ValueError
    list1 = [char.lower() for char in test_string if char.isalnum()]
    list2 = list1.copy()
    reversed(list2)

    return list1 == list2

print(is_palindrome(" 161"))
