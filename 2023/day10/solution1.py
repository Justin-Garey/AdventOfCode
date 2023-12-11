#!/bin/python3

import collections

DEBUG = 0

north = ["|", "L", "J"]
south = ["|", "7", "F"]
east = ["-", "L", "F"]
west = ["-", "J", "7"]


def get_next(line, position):
    next_steps = []
    # Check spot north of pos
    if line != 0 and pipe_map[line - 1][position] in south:
        next_steps.append((line - 1, position))
    # Check spot south of pos
    if line < (len(pipe_map) - 1):
        if pipe_map[line + 1][position] in north:
            next_steps.append((line + 1, start_index))
    # Check spot west of pos
    if position != 0 and pipe_map[line][position - 1] in east:
        next_steps.append((line, position - 1))
    # Check spot east of pos
    if position < len(pipe_map[0]) - 1:
        if pipe_map[line][position + 1] in west:
            next_steps.append((line, position + 1))
    return next_steps


# Breadth first search
def discover_main_loop(pipe_map, start_line, start_index, end):
    queue = collections.deque([[(start_line, start_index)]])
    visited = set([(start_line, start_index)])
    path = []
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if pipe_map[x][y] == end:
            return path
        # Check spot north
        if x > 0 and pipe_map[x - 1][y] in south and (x - 1, y) not in visited:
            queue.append(path + [(x - 1, y)])
            visited.add((x - 1, y))
        # Check spot south
        if (
            x < (len(pipe_map) - 1)
            and pipe_map[x + 1][y] in north
            and (x + 1, y) not in visited
        ):
            queue.append(path + [(x + 1, y)])
            visited.add((x + 1, y))
        # Check spot west
        if y > 0 and pipe_map[x][y - 1] in east and (x, y - 1) not in visited:
            queue.append(path + [(x, y - 1)])
            visited.add((x, y - 1))
        # Check spot east
        if (
            y < (len(pipe_map[0]) - 1)
            and pipe_map[x][y + 1] in west
            and (x, y + 1) not in visited
        ):
            queue.append(path + [(x, y + 1)])
            visited.add((x, y + 1))
    return path


with open("input1.in", "r") as file:
    pipe_map = []
    line_number = 0
    start_line = 0
    start_index = 0
    for line in file.readlines():
        pipe_map.append([])
        for index in range(len(line.strip())):
            pipe_map[line_number].append(line[index])
            if line[index] == "S":
                start_line = line_number
                start_index = index
        line_number += 1
    next_steps = get_next(start_line, start_index)
    pipe_map[start_line][start_index] = "C"
    if DEBUG:
        print(f"Starting position is on line {start_line} and position {start_index}")
        print(f"The next steps are {next_steps}")

    end = "*"
    start_line = next_steps[0][0]
    start_index = next_steps[0][1]
    pipe_map[next_steps[1][0]][next_steps[1][1]] = "*"
    # Need to discover the main loop first and set the rest of the items to .
    path = discover_main_loop(pipe_map, start_line, start_index, end)
    if DEBUG:
        print(f"Final path is {path}")
    print((len(path) + 2) / 2)
