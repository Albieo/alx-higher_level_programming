#!/usr/bin/python3
j = 122
while (j != 96):
    if j % 2 == 0:
        print("{}".format(chr(j)), end="")
        j -= 1
    else:
        j -= 32
        print("{}".format(chr(j)), end="")
        j += 31
