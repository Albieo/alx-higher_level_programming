#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) == 1:
        print(0)
    elif len(sys.argv) == 2:
        pass
    else:
        sum = 0
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
        print(sum)


if __name__ == "__main__":
    main()
