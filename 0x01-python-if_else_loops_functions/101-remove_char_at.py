#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return str
    else:
        word = ""
        j = 0
        for i in str:
            j += 1
            if j == n + 1:
                word = word + ""
            else:
                word = word + i
        return word
