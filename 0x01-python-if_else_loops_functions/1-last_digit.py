#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if number < 0:
    number = number * -1
while number >= 10:
    number = number // 10
if number > 5:
    print("Last digit of {} is {} and is greater than 5".format(n, number))
elif number == 0:
    print("Last digit of {} is {} and is 0".format(n, number))
else:
    print("Last digit of {} is {}"
          " and is less than 6 and not 0".format(n, number))
