#!/bin/python3

DEBUG = 0

with open("./input", "r") as file:
    saved_elf = 0
    current_elf = 0
    saved_sum = 0
    current_sum = 0
    for line in file:
        if not line.isspace():
            current_sum += int(line.strip())
        else:
            current_elf += 1
            if DEBUG:
                print(f"Elf {current_elf} has {current_sum} calories")
            if current_sum > saved_sum:
                saved_sum = current_sum
                current_sum = 0
                saved_elf = current_elf
            else:
                current_sum = 0
    if current_sum != 0:
        current_elf += 1
        if DEBUG:
            print(f"Elf {current_elf} has {current_sum} calories")
        if current_sum > saved_sum:
            saved_sum = current_sum
            current_sum = 0
            saved_elf = current_elf
        else:
            current_sum = 0

    print(f"\nElf {saved_elf} has {saved_sum} calories")
