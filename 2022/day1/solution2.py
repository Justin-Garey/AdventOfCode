#!/bin/python3

DEBUG = 0

with open("./input", "r") as file:
    current_elf = 0
    current_sum = 0
    first_elf, second_elf, third_elf = 0, 0, 0
    first_sum, second_sum, third_sum = 0, 0, 0
    for line in file:
        if not line.isspace():
            current_sum += int(line.strip())
        else:
            current_elf += 1
            if DEBUG:
                print(f"Elf {current_elf} has {current_sum} calories")
            if current_sum > first_sum:
                # Update second and third elves
                third_sum = second_sum
                third_elf = second_elf
                second_sum = first_sum
                second_elf = first_elf
                # Update the first elf and current sum
                first_sum = current_sum
                current_sum = 0
                first_elf = current_elf
            elif current_sum > second_sum:
                # Update third elf
                third_sum = second_sum
                third_elf = second_elf
                # Update the second elf and current sum
                second_sum = current_sum
                current_sum = 0
                second_elf = current_elf
            elif current_sum > third_sum:
                # Update the third elf and current sum
                third_sum = current_sum
                current_sum = 0
                third_elf = current_elf
            else:
                current_sum = 0
    if current_sum != 0:
        current_elf += 1
        if DEBUG:
            print(f"Elf {current_elf} has {current_sum} calories")
        if current_sum > first_sum:
            # Update second and third elves
            third_sum = second_sum
            third_elf = second_elf
            second_sum = first_sum
            second_elf = first_elf
            # Update the first elf and current sum
            first_sum = current_sum
            current_sum = 0
            first_elf = current_elf
        elif current_sum > second_sum:
            # Update third elf
            third_sum = second_sum
            third_elf = second_elf
            # Update the second elf and current sum
            second_sum = current_sum
            current_sum = 0
            second_elf = current_elf
        elif current_sum > third_sum:
            # Update the third elf and current sum
            third_sum = current_sum
            current_sum = 0
            third_elf = current_elf
        else:
            current_sum = 0


    print(f"\nElves {first_elf}, {second_elf}, {third_elf} have a total of {first_sum + second_sum + third_sum} calories")
