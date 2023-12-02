#!/bin/python3

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

DEBUG = 0

with open("input1.in", 'r') as file:
    sum = 0
    for line in file.readlines():
        parts = line.split(':')
        game_id = int(parts[0].replace("Game", ''))
        if (DEBUG):
            print(game_id)
        game_sets = parts[1].split(';')
        valid_set = True
        for game_set in game_sets:
            cube_counts = game_set.split(',')
            for cube_count in cube_counts:
                cube_parts = cube_count.split(' ')
                cube_color = cube_parts[2].replace('\n', '')
                cube_amount = int(cube_parts[1])
                if (cube_color == "red"):
                    if (cube_amount > MAX_RED):
                        valid_set = False
                        if (DEBUG):
                            print("too much red")
                elif (cube_color == "green"):
                    if (cube_amount > MAX_GREEN):
                        valid_set = False
                        if (DEBUG):
                            print("too much green")
                elif (cube_color == "blue"):
                    if (cube_amount > MAX_BLUE):
                        valid_set = False
                        if (DEBUG):
                            print("too much blue")
                else:
                    print("Unknown color")
        if (valid_set):
            sum += game_id
    print(f"The sum is: {sum}")