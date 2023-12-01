#!/bin/python3

import re

with open("input1.in", 'r') as file:
    sum = 0
    for line in file.readlines():
        first = line[re.search(r"\d", line).start()]
        last = line[len(line) - re.search(r"\d", line[::-1]).start() - 1]
        val = int(first + last)
        sum += val
    print(f"The sum is: {sum}")
        