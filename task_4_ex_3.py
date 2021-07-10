"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter=None) -> list:

    if not isinstance((str_to_split or delimiter), str):
        raise ValueError
    if delimiter == '':
        raise ValueError
    if str_to_split == '':
        return ''
    if delimiter == None:
        raise ValueError

    list_of_substr = []
    list = []

    for i in str_to_split:
        if i != delimiter:
            list_of_substr.append(i)
        else:
            string = ''.join([elem for elem in list_of_substr])
            list.append(string)
            list_of_substr = []
    if list_of_substr:
        string = ''.join([elem for elem in list_of_substr])
        list.append(string)

    if str_to_split[-1] == delimiter:
        list.append('')
    return list


