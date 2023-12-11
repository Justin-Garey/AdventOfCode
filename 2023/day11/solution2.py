#!/bin/python3

import itertools

DEBUG = 0

with open("input1.in", "r") as file:
    universe_map = []
    rows = []
    columns = []
    line_number = 0
    for line in file.readlines():
        universe_map.append([])
        for index in range(len(line.strip())):
            universe_map[line_number].append(line[index])
            if line[index] == "#":
                columns.append(index)
                rows.append(line_number)
        line_number += 1
    empty_rows = []
    empty_columns = []
    for i in range(len(universe_map)):
        if i not in rows:
            empty_rows.append(i)
    for i in range(len(universe_map[0])):
        if i not in columns:
            empty_columns.append(i)
    if DEBUG:
        for line in universe_map:
            print("".join(line))
        print(f"Empty rows: {empty_rows}")
        print(f"Empty columns: {empty_columns}")

    galaxies = []
    for k in range(len(universe_map)):
        for i in range(len(universe_map[k])):
            if universe_map[k][i] == "#":
                galaxies.append((k, i))

    unique_combinations = list(itertools.combinations(galaxies, 2))
    if DEBUG:
        print(f"There are {len(unique_combinations)} unique combinations")

    path_sum = 0

    for pair in unique_combinations:
        path_sum += abs(pair[1][0] - pair[0][0]) + abs(pair[1][1] - pair[0][1])
        for i in range(min(pair[0][1], pair[1][1]), max(pair[0][1], pair[1][1])):
            if i in empty_columns:
                if DEBUG:
                    print(
                        f"X1: {pair[0][0]}, X2: {pair[1][0]}, Y1: {pair[0][1]}, Y2: {pair[1][1]}"
                    )
                    print(
                        f"Distance is {abs(pair[1][0] - pair[0][0]) + abs(pair[1][1] - pair[0][1])}"
                    )
                    print(f"Empty column is {i}")
                path_sum += 999999
        for i in range(min(pair[0][0], pair[1][0]), max(pair[0][0], pair[1][0])):
            if i in empty_rows:
                path_sum += 999999
    print(path_sum)
