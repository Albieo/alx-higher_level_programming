#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        argument_count = len(sys.argv) - 1

        print(f"{argument_count} arguments:")
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")


if __name__ in "__main__":
    main()
