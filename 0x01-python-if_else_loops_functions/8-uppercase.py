#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)

        def print_word():
            print("{}".format(chr(num)), end="")
        if num >= 97 and num <= 122:
            num -= 32
            print_word()
        else:
            print_word()
    print("\n", end="")
