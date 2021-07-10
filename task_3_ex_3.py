"""
Write a Python-script that:
1. Searches for files by a given pattern (pattern can include: *, ?)
2. Displays the search result
3. Gets access rights for each file that is found and displays the result

The script should have 2 obligatory functions:
- finder - a generator function searches for files by a given pattern
 in a given path returns an absolute path of a found file.
- display_result - displays founded files and files' permission
by a given list of absolute paths (You can find an example below).

Example call:
python task_3_ex_3.py /usr/bin -p '?ython*'

Example result:
...
/usr/bin/python3.6m -rwxr-xr-x
/usr/bin/python3.7m -rwxr-xr-x
Found 12 file(s).

Note: use of glob module is prohibited.

Hint: use os.walk, stat, fnmatch
"""

import fnmatch, os, stat, sys


def finder(path, pattern):
    """Searches for files by a given pattern.

    :param path: Absolute path for searching.
    :param pattern: Can consist *, ?.
    :return: absolute path of found file.
    """
    files = fnmatch.filter(os.listdir(path), pattern)
    file_paths = [os.path.join(path, file) for file in files]
    return file_paths


def display_result(file_paths):
    """Displays founded file paths and file's permissions."""

    value_letters = [(4, 'r'), (2, 'w'), (1, 'x')]
    result = ""
    files_list = []
    try:
        for path in file_paths:
            st = os.stat(path)
            mode = st[stat.ST_MODE]
            octal = stat.S_IMODE(mode)
            for permission in [int(n) for n in str(octal)]:
                for value, letter in value_letters:
                    if permission >= value:
                        result += letter
                        permission -= value
                    else:
                        result += '-'
            files_list.extend((path, result))
            result = ''
        for i in range(0, len(files_list), 2):
            return files_list[i] + ' ' + files_list[i + 1]
    except FileNotFoundError:
        pass

def main():

    args = sys.argv
    try:
        path = os.path.abspath(args[1])
        pattern = args[-1]
    except:
        raise IndexError

    display_result(finder(path, pattern))


if __name__ == '__main__':
    main()
