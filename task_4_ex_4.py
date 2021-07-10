"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]`
which splits the `string` by indexes specified in `indexes`. 
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```
"""


def split_by_index(string, indexes):
    previous_index = 0
    list = []
    for i in indexes:
        if isinstance(i, int) and i > 0 and i > previous_index:
            sub_string = string[previous_index:i]
            list.append(sub_string)
            previous_index = i

    if previous_index < len(string) - 1:
        sub_string = string[previous_index:len(string)]
        list.append(sub_string)

    return list
