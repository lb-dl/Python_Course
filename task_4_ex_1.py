"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(string: str) -> str:
    list = []
    replaced_string = ''
    for i in string:
        if i == '"':
            i = "'"
            list.append(i)
        elif i == "'":
            i = '"'
            list.append(i)
        else:
            list.append(i)
        replaced_string = ''.join([elem for elem in list])

    return replaced_string
