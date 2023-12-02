#!/bin/python3

DEBUG = 0

with open("input1.in", 'r') as file:
    sum = 0
    for line in file.readlines():
        game_sets = line.split(':')[1].split(';')
        max_red = 1
        max_blue = 1
        max_green = 1
        for game_set in game_sets:
            cube_counts = game_set.split(',')
            for cube_count in cube_counts:
                cube_parts = cube_count.split(' ')
                cube_color = cube_parts[2].replace('\n', '')
                cube_amount = int(cube_parts[1])
                if (cube_color == "red"):
                    if (cube_amount > max_red):
                        max_red = cube_amount
                elif (cube_color == "green"):
                    if (cube_amount > max_green):
                        max_green = cube_amount
                elif (cube_color == "blue"):
                    if (cube_amount > max_blue):
                        max_blue = cube_amount
                else:
                    print("Unknown color")
        if (DEBUG):
            print(f"Red: {max_red}, Blue: {max_blue}, Green: {max_green}")
        sum += max_red * max_green * max_blue
    print(f"The sum is: {sum}")