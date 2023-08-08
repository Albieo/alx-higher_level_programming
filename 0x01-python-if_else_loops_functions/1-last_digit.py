#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    if int(str(number)[-1]) == 0:
        print(f"Last digit of {number} is {str(number)[-1]} and is 0")
    elif int(str(number)[-1]) > 5:
        print(f"Last digit of {number} is {str(number)[-1]} and is greater than 5")
    else: 
        print(f"Last digit of {number} is {str(number)[-1]} ", end="")
        print("and is less than 6 and not 0")
else:
    i = int(str(number)[-1]) * -1
    if i == 0:
        print(f"Last digit of {number} is {i} and is 0")
    else:
        print(f"Last digit of {number} is {i} ", end="")
        print("and is less than 6 and not 0")
