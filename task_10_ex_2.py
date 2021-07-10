"""Implement a function `most_common_words(file_path: str, top_words: int) -> list`
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned

Example:

print(most_common_words(file_path, 3))
>>> ['donec', 'etiam', 'aliquam']
> NOTE: Remember about dots, commas, capital letters etc.
"""
from collections import Counter
import re


def most_common_words(text, top_words):
    with open(text, 'r') as file:
        text_without_punctuation = re.sub(r'[^\w\s]', '', file.read())
        list_of_words = text_without_punctuation.lower().split(' ')
        list_of_words[-1] = list_of_words[-1].strip()

        counter = Counter(list_of_words)
        the_most_common_words = counter.most_common(top_words)
        result = []
        for i in range(top_words):
            result.append(the_most_common_words[i][0])

        return result
