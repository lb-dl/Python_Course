"""
Task04_6

Implement a function get_longest_word(s: str) -> str which returns the longest word in the given string.
The word can contain any symbols except whitespaces (`,\n,\tand so on).
If there are multiple longest words in the string with a same length return the word that occurs first.

Example: get_longest_word('Python is simple and effective!')
         #output: 'effective!'
         get_longest_word('Any pythonista like namespaces a lot.')
         #output: 'pythonista'

Note:
Raise ValueError in case of wrong data type
Usage of 're' library is prohibited
"""


def get_longest_word(str_to_parse: str) -> str:
    if not isinstance(str_to_parse, str):
        raise ValueError
    length = 0
    longest_word = ''
    str_to_parse = ''.join(c for c in str_to_parse if str(c) not in '\n\t\r')
    for word in str_to_parse.split():
        if len(word) > length:
            longest_word = word
            length = len(word)

    return longest_word
