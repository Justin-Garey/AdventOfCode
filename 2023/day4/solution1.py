#!/bin/python3

DEBUG = 0

with open("input1.in", "r") as file:
    sum = 0
    for line in file.readlines():
        points = 0
        numbers_to_see = line.replace("\n", "").split(":")[1].split("|")
        winning_numbers = numbers_to_see[0].strip().replace("  ", " ").split(" ")
        card_numbers = numbers_to_see[1].strip().replace("  ", " ").split(" ")
        if DEBUG:
            print(f"Winning Numbers: {winning_numbers}\nCard Numbers: {card_numbers}")
        for number in card_numbers:
            if number in winning_numbers:
                if points == 0:
                    points += 1
                else:
                    points *= 2
        sum += points

    print(f"The sum is: {sum}")
