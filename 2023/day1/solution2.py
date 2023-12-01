#!/bin/python3

import re

with open("input1.in", 'r') as file:
    sum = 0

    numbers = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    for line in file.readlines():
        values = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        first = numbers[values[0]] if values[0] in numbers else values[0]
        last = numbers[values[-1]] if values[-1] in numbers else values[-1]
        #print(first, last)
        sum += int(first + last)
    print(f"The sum is: {sum}")
        