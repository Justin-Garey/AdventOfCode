#!/bin/python3

DEBUG = 0


def check(item):
    if not item.isdigit() and not item.isspace() and not item in ["."]:
        return True
    else:
        return False


def grab_and_replace(line, index):
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
    dots_to_replace = "." * (end - start - 1)
    line = line[: start + 1] + dots_to_replace + line[end:]
    if DEBUG:
        print(f"Found {value}")
    return (value, line)


def check_line(line, index):
    # Check for symbol behind
    if check(line[index - 1]):
        if DEBUG:
            print(f"Found special character behind {line[index]}: {line[index - 1]}")
        return grab_and_replace(line, index)
    # Check for symbol ahead
    if check(line[index + 1]):
        if DEBUG:
            print(f"Found special character ahead {line[index]}: {line[index + 1]}")
        return grab_and_replace(line, index)
    return (0, line)


def check_below(line, line_below, index):
    # Check for symbol directly below
    if check(line_below[index]):
        if DEBUG:
            print(f"Found special character below {line[index]}: {line_below[index]}")
        return grab_and_replace(line, index)
    # Check for symbol left and below
    if check(line_below[index - 1]):
        if DEBUG:
            print(
                f"Found special character left and below {line[index]}: {line_below[index - 1]}"
            )
        return grab_and_replace(line, index)
    # Check for symbol right and below
    if check(line_below[index + 1]):
        if DEBUG:
            print(
                f"Found special character right and below {line[index]}: {line_below[index + 1]}"
            )
        return grab_and_replace(line, index)
    return (0, line)


def check_above(line, line_above, index):
    # Check for symbol directly above
    if check(line_above[index]):
        if DEBUG:
            print(f"Found special character above {line[index]}: {line_above[index]}")
        return grab_and_replace(line, index)
    # Check for symbol left and above
    if check(line_above[index - 1]):
        if DEBUG:
            print(
                f"Found special character left and above {line[index]}: {line_above[index - 1]}"
            )
        return grab_and_replace(line, index)
    # Check for symbol right and above
    if check(line_above[index + 1]):
        if DEBUG:
            print(
                f"Found special character right and above {line[index]}: {line_above[index + 1]}"
            )
        return grab_and_replace(line, index)
    return (0, line)


with open("input1.in", "r") as file:
    sum = 0
    curr_line = file.readline()
    next_line = file.readline()
    # Search the first line for valid numbers
    for index in range(len(curr_line)):
        if curr_line[index].isdigit():
            (add_to_sum, set_to_curr_line) = check_line(curr_line, index)
            sum += add_to_sum
            curr_line = set_to_curr_line
        if curr_line[index].isdigit():
            (add_to_sum, set_to_curr_line) = check_below(curr_line, next_line, index)
            sum += add_to_sum
            curr_line = set_to_curr_line
    # Start the normal search process on the second line
    prev_line = curr_line
    curr_line = next_line
    for next_line in file.readlines():
        for index in range(len(curr_line)):
            if curr_line[index].isdigit():
                (add_to_sum, set_to_curr_line) = check_above(
                    curr_line, prev_line, index
                )
                sum += add_to_sum
                curr_line = set_to_curr_line
            if curr_line[index].isdigit():
                (add_to_sum, set_to_curr_line) = check_line(curr_line, index)
                sum += add_to_sum
                curr_line = set_to_curr_line
            if curr_line[index].isdigit():
                (add_to_sum, set_to_curr_line) = check_below(
                    curr_line, next_line, index
                )
                sum += add_to_sum
                curr_line = set_to_curr_line
        prev_line = curr_line
        curr_line = next_line
    # Search the last line for valid numbers
    for index in range(len(curr_line)):
        if curr_line[index].isdigit():
            (add_to_sum, set_to_curr_line) = check_line(curr_line, index)
            sum += add_to_sum
            curr_line = set_to_curr_line
        if curr_line[index].isdigit():
            (add_to_sum, set_to_curr_line) = check_above(curr_line, prev_line, index)
            sum += add_to_sum
            curr_line = set_to_curr_line
    print(f"The sum is: {sum}")
