#!/bin/python3

DEBUG = 0


def check(item):
    if item.isdigit():
        return True
    else:
        return False


def grab(line, index):
    end = index
    for char in line[index:]:
        if char.isnumeric():
            end += 1
        else:
            break
    start = index
    for char in line[index::-1]:
        if char.isnumeric():
            start -= 1
        else:
            break
    value = int(line[start + 1 : end])
    if DEBUG:
        print(f"Grabbed {value}")
    dots_to_replace = "." * (end - start - 1)
    line = line[: start + 1] + dots_to_replace + line[end:]
    return (value, line)


def check_line(line, index):
    values = []
    # Check for number behind
    if check(line[index - 1]):
        (value, line) = grab(line, index - 1)
        values.append(value)
    # Check for number ahead
    if check(line[index + 1]):
        (value, line) = grab(line, index + 1)
        values.append(value)
    return values


def check_below(line_below, index):
    values = []
    # Check for number directly below
    if check(line_below[index]):
        (value, line_below) = grab(line_below, index)
        values.append(value)
    # Check for number left and below
    if check(line_below[index - 1]):
        (value, line_below) = grab(line_below, index - 1)
        values.append(value)
    # Check for symbol right and below
    if check(line_below[index + 1]):
        (value, line_below) = grab(line_below, index + 1)
        values.append(value)
    return values


def check_above(line_above, index):
    values = []
    # Check for number directly above
    if check(line_above[index]):
        (value, line_above) = grab(line_above, index)
        values.append(value)
    # Check for number left and above
    if check(line_above[index - 1]):
        (value, line_above) = grab(line_above, index - 1)
        values.append(value)
    # Check for number right and above
    if check(line_above[index + 1]):
        (value, line_above) = grab(line_above, index + 1)
        values.append(value)
    return values


with open("input1.in", "r") as file:
    sum = 0
    curr_line = file.readline()
    next_line = file.readline()
    # Search the first line for stars
    for index in range(len(curr_line)):
        star_numbers = []
        if curr_line[index] == "*":
            numbers = check_line(curr_line, index)
            star_numbers += numbers
            numbers = check_below(next_line, index)
            star_numbers += numbers
            if DEBUG:
                print(f"Numbers surrounding star are: {star_numbers}")
            if len(star_numbers) == 2:
                sum += star_numbers[0] * star_numbers[1]

    # Start the normal search process on the second line
    prev_line = curr_line
    curr_line = next_line
    for next_line in file.readlines():
        for index in range(len(curr_line)):
            star_numbers = []
            if curr_line[index] == "*":
                numbers = check_above(prev_line, index)
                star_numbers += numbers
                numbers = check_line(curr_line, index)
                star_numbers += numbers
                numbers = check_below(next_line, index)
                star_numbers += numbers
                if DEBUG:
                    print(f"Numbers surrounding star are: {star_numbers}")
                if len(star_numbers) == 2:
                    sum += star_numbers[0] * star_numbers[1]
        prev_line = curr_line
        curr_line = next_line
    # Search the last line for stars
    for index in range(len(curr_line)):
        star_numbers = []
        if curr_line[index] == "*":
            numbers = check_line(curr_line, index)
            star_numbers += numbers
            numbers = check_above(prev_line, index)
            star_numbers += numbers
            if DEBUG:
                print(f"Numbers surrounding star are: {star_numbers}")
            if len(star_numbers) == 2:
                sum += star_numbers[0] * star_numbers[1]
    print(f"The sum is: {sum}")
