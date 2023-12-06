#!/bin/python3

DEBUG = 1

with open("input1.in", "r") as file:
    seeds_line = file.readline().split(":")[1].strip().split(" ")
    seeds = []
    for index in range(len(seeds_line) // 2):
        seeds.append(
            (
                int(seeds_line[index * 2]),
                int(seeds_line[index * 2]) + int(seeds_line[index * 2 + 1]),
            )
        )
    if DEBUG:
        print(f"Seeds: {seeds}")
    sections = file.read().strip().split("\n\n")
    for section in sections:
        ranges = []
        for line in section.splitlines()[1:]:
            items = line.split()
            ranges.append((int(items[0]), int(items[1]), int(items[2])))
        new_ranges = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            for dest, src, ran in ranges:
                range_start = max(start, src)
                range_end = min(end, src + ran)
                if range_start < range_end:
                    new_ranges.append(
                        (range_start - src + dest, range_end - src + dest)
                    )
                    if range_start > start:
                        seeds.append((start, range_start))
                    if end > range_end:
                        seeds.append((range_end, end))
                    break
            else:
                new_ranges.append((start, end))
        seeds = new_ranges
    if DEBUG:
        print(f"Final Seeds: {seeds}")
    print(min(seeds)[0])
