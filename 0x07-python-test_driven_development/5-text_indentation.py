#!/usr/bin/python3
""" Text indentation """


def text_indentation(text):
    """
    Indent and print each sentence in the given text.

    Args:
        text (str): The input text containing one or more sentences.

    Raises:
        TypeError: If the input text is not a string.

    Example:
        text_indentation("This is a sample text. \
        It has multiple sentences: like this one? And this one!")
        Output:
        This is a sample text.

        It has multiple sentences: like this one?

        And this one!
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    sentence = []
    word = ""
    for i in text:
        if i in [".", "?", ":"]:
            word += i
            sentence.append(word.strip())
            word = ""
        else:
            word += i
    sentence.append(word.strip())
    for j in range(len(sentence) - 1):
        print(sentence[j], end="")
        print('\n')
    print(sentence[-1])
