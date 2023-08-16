#!/usr/bin/python3
def uniq_add(my_list=[]):
    non_unique = []
    sum = 0
    for i in range(len(my_list)):
        if my_list[i] in non_unique:
            continue
        else:
            sum = sum + my_list[i]
            non_unique.append(my_list[i])
    return sum
