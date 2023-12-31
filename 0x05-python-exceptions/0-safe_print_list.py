#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
        print("")
        return (my_list[i])
    except (IndexError):
        print("")
        return (my_list[-1])
