"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
  Note: use `string.ascii_lowercase` for list of alphabet letters

Note: raise TypeError in case of wrong data type

Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
>>> {'o'}
print(chars_in_one(*test_strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(chars_in_two(*test_strings))
>>> {'h', 'l', 'o'}
print(not_used_chars(*test_strings))
>>> {'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'}
"""


def chars_in_all(*strings):
    if not all(isinstance(string, str) for string in strings):
        raise TypeError
    set_of_strings = [set(string) for string in strings]
    if len(set_of_strings) < 2:
        raise ValueError

    return set(set_of_strings[0]).intersection(*set_of_strings)


def chars_in_one(*strings):
    if not all(isinstance(string, str) for string in strings):
        raise TypeError
    set_of_strings = [set(string) for string in strings]
    if len(set_of_strings) < 2:
        raise ValueError

    return set().union(*set_of_strings)


def chars_in_two(*strings):
    if not all(isinstance(string, str) for string in strings):
        raise TypeError
    set_of_strings = [set(string) for string in strings]
    if len(set_of_strings) < 2:
        raise ValueError

    result = set()
    for i in range(len(set_of_strings) - 1):
        for j in range(1+i, len(set_of_strings)):
            temp = set_of_strings[i].copy()
            temp.intersection_update(set_of_strings[j])
            result.update(temp)
    return result


def not_used_chars(*strings):

    import string

    if not all(isinstance(string, str) for string in strings):
        raise TypeError
    set_of_strings = [list(string) for string in strings]
    if len(set_of_strings) < 2:
        raise ValueError

    used_chars = set().union(*set_of_strings)
    alphabet_chars = set(string.ascii_lowercase)
    alphabet_chars.difference_update(used_chars)
    return alphabet_chars
