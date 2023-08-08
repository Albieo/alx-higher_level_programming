#!/usr/bin/python3
for i in range(100):
    if len(str(i)) == 1:
        print(f"{i:02d}", end=", " if i < 99 else "\n")
    else:
        print(i, end="\n" if i == 99 else ", ")
