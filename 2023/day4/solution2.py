#!/bin/python3

DEBUG = 0

with open("input1.in", "r") as file:
    sum = 0
    card_dict = {"Card 1": 1}
    for line in file.readlines():
        matches = 0
        line_split = line.replace("\n", "").split(":")
        card = line_split[0].replace("   ", " ").replace("  ", " ")
        numbers_to_see = line_split[1].split("|")
        winning_numbers = numbers_to_see[0].strip().replace("  ", " ").split(" ")
        card_numbers = numbers_to_see[1].strip().replace("  ", " ").split(" ")
        if DEBUG:
            print(
                f"{card}\nWinning Numbers: {winning_numbers}\nCard Numbers: {card_numbers}"
            )
        for number in card_numbers:
            if number in winning_numbers:
                matches += 1
        # Add card amounts to dictionary
        if not card in card_dict:
            card_dict[card] = 1
        card_number = int(card.replace("   ", " ").replace("  ", " ").split(" ")[1])
        for i in range(matches):
            key = f"Card {card_number + i + 1}"
            if key in card_dict:
                card_dict[key] = card_dict[key] + (1 * card_dict[card])
            else:
                card_dict[key] = 1 + (1 * card_dict[card])
        sum += card_dict[card]
        if DEBUG:
            print(card_dict)

    print(f"The sum is: {sum}")
