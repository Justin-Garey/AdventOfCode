#!/bin/python3

DEBUG = 0


# returns a value between 0 and 6 inclusive
def get_hand_strength(cards):
    # 5 of a kind
    if cards.count(cards[0]) == 5:
        return 6
    # 4 of a kind
    if cards.count(cards[0]) == 4 or cards.count(cards[1]) == 4:
        return 5
    # Full house options and 3 of a kind
    if cards.count(cards[0]) == 3:
        cards = cards.replace(cards[0], "")
        if cards[0] == cards[1]:
            return 4
        else:
            return 3
    if cards.count(cards[1]) == 3:
        cards = cards.replace(cards[1], "")
        if cards[0] == cards[1]:
            return 4
        else:
            return 3
    if cards.count(cards[2]) == 3:
        cards = cards.replace(cards[2], "")
        if cards[0] == cards[1]:
            return 4
        else:
            return 3
    # 2 pair and 1 pair
    if cards.count(cards[0]) == 2:
        cards = cards.replace(cards[0], "")
        if cards.count(cards[0]) == 2 or cards.count(cards[1]) == 2:
            return 2
        else:
            return 1
    if cards.count(cards[1]) == 2:
        cards = cards.replace(cards[1], "")
        if cards.count(cards[0]) == 2 or cards.count(cards[1]) == 2:
            return 2
        else:
            return 1
    if cards.count(cards[2]) == 2:
        cards = cards.replace(cards[2], "")
        if cards.count(cards[0]) == 2 or cards.count(cards[1]) == 2:
            return 2
        else:
            return 1
    if cards.count(cards[3]) == 2:
        cards = cards.replace(cards[3], "")
        if cards.count(cards[0]) == 2 or cards.count(cards[1]) == 2:
            return 2
        else:
            return 1
    return 0


with open("input1.in", "r") as file:
    solution = 0
    five_bucket = []
    four_bucket = []
    full_bucket = []
    three_bucket = []
    two_pair_bucket = []
    one_pair_bucket = []
    high_card_bucket = []
    for line in file.readlines():
        split_line = line.split()
        cards = split_line[0]
        bid = int(split_line[1])
        strength = get_hand_strength(cards)
        if DEBUG:
            print(f"Cards: {cards} with bid: {bid} and strength: {strength}")
        if strength == 6:
            five_bucket.append((cards, bid))
        elif strength == 5:
            four_bucket.append((cards, bid))
        elif strength == 4:
            full_bucket.append((cards, bid))
        elif strength == 3:
            three_bucket.append((cards, bid))
        elif strength == 2:
            two_pair_bucket.append((cards, bid))
        elif strength == 1:
            one_pair_bucket.append((cards, bid))
        else:
            high_card_bucket.append((cards, bid))
    order = "23456789TJQKA"
    five_bucket = sorted(
        five_bucket, key=lambda word: [order.index(letter) for letter in word[0]]
    )
    four_bucket = sorted(
        four_bucket, key=lambda word: [order.index(letter) for letter in word[0]]
    )
    full_bucket = sorted(
        full_bucket, key=lambda word: [order.index(letter) for letter in word[0]]
    )
    three_bucket = sorted(
        three_bucket, key=lambda word: [order.index(letter) for letter in word[0]]
    )
    two_pair_bucket = sorted(
        two_pair_bucket, key=lambda word: [order.index(letter) for letter in word[0]]
    )
    one_pair_bucket = sorted(
        one_pair_bucket, key=lambda word: [order.index(letter) for letter in word[0]]
    )
    high_card_bucket = sorted(
        high_card_bucket, key=lambda word: [order.index(letter) for letter in word[0]]
    )
    if DEBUG:
        print("Five of a kinds", five_bucket)
        print("Four of a kinds", four_bucket)
        print("Full House", full_bucket)
        print("Three of a kinds", three_bucket)
        print("Two Pairs", two_pair_bucket)
        print("One Pairs", one_pair_bucket)
        print("High Cards", high_card_bucket)

    rank = 1
    for i in high_card_bucket:
        solution += i[1] * rank
        rank += 1
    for i in one_pair_bucket:
        solution += i[1] * rank
        rank += 1
    for i in two_pair_bucket:
        solution += i[1] * rank
        rank += 1
    for i in three_bucket:
        solution += i[1] * rank
        rank += 1
    for i in full_bucket:
        solution += i[1] * rank
        rank += 1
    for i in four_bucket:
        solution += i[1] * rank
        rank += 1
    for i in five_bucket:
        solution += i[1] * rank
        rank += 1

    print(solution)
