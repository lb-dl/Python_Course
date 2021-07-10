"""
Implement a function `sort_names(input_file_path: str, output_file_path: str) -> None`, which sorts names from
`file_path` and write them to a new file `output_file_path`. Each name should start with a new line as in the
following example:
Example:

Adele
Adrienne
...
Willodean
Xavier
"""


def sort_names(input_file_path: str, output_file_path: str) -> None:
    with open(input_file_path, 'r') as reader, open(output_file_path, 'a') as writer:
        list_of_names = (reader.read().split('\n'))
        print(type(list_of_names))
        for line in list_of_names:
            writer.write(line+'\n')

print(sort_names('../names.txt', 'sorted_names.txt'))
