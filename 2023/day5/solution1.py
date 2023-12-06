#!/bin/python3

DEBUG = 0


def fill_in(seeds, location):
    for index, item in enumerate(seeds[location]):
        if not seeds[location][index][1]:
            seeds[location][index] = (seeds[location - 1][index][0], True)
    return seeds


with open("input1.in", "r") as file:
    seeds = [file.readline().split(":")[1].strip().split(" ")]
    for index, item in enumerate(seeds[0]):
        seeds[0][index] = (int(item), True)
    for i in range(7):
        seeds.append([(0, False)] * len(seeds[0]))
    location = 0
    if DEBUG:
        print(f"Seeds: {seeds}")

    for line in file.readlines():
        # Don't do anything if the line contains nothing
        if not line.isspace():
            # This is where we find out what category we are in
            if "map" in line:
                if "seed-to-soil" in line:
                    location = 1
                elif "soil-to-fertilizer" in line:
                    fill_in(seeds, location)
                    location = 2
                elif "fertilizer-to-water" in line:
                    fill_in(seeds, location)
                    location = 3
                elif "water-to-light" in line:
                    fill_in(seeds, location)
                    location = 4
                elif "light-to-temperature" in line:
                    fill_in(seeds, location)
                    location = 5
                elif "temperature-to-humidity" in line:
                    fill_in(seeds, location)
                    location = 6
                elif "humidity-to-location" in line:
                    fill_in(seeds, location)
                    location = 7
                else:
                    print("Unkown line")
                    break
            else:
                for index, item in enumerate(seeds[location - 1]):
                    line_items = line.strip().split(" ")
                    dest_range = int(line_items[0])
                    source_range = int(line_items[1])
                    range_length = int(line_items[2])
                    seed = int(item[0])
                    if not seeds[location][index][1]:
                        if seed >= source_range and seed < (
                            source_range + range_length
                        ):
                            if DEBUG:
                                print(f"{seed} -> {dest_range + (seed - source_range)}")
                            seeds[location][index] = (
                                dest_range + (seed - source_range),
                                True,
                            )
    fill_in(seeds, location)
    if DEBUG:
        for i in seeds:
            print(i)

    closest_location = seeds[-1][0][0]
    for item in seeds[-1]:
        if item[0] < closest_location:
            closest_location = item[0]

    print(closest_location)
