#!/usr/bin/python3
for i in range(100):
    if len(str(i)) == 1:
        print("{:02d}".format(i), end=", " if i < 99 else "\n")
    else:
        print("{}".format(i), end="\n" if i == 99 else ", ")
