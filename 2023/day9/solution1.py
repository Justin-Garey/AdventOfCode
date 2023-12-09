#!/bin/python3

DEBUG = 0

with open("input1.in", "r") as file:
    sum = 0
    for line in file.readlines():
        sequences = [[]]
        sequences[0] = [int(x) for x in line.strip().split()]
        if DEBUG:
            print(f"History is {sequences[0]}")
        while True:
            prev_x = sequences[-1][0]
            new_sequence = []
            for x in sequences[-1][1:]:
                new_sequence.append(x - prev_x)
                prev_x = x
            sequences.append(new_sequence)
            if DEBUG:
                print(f"New sequence {new_sequence}")
            if len(set(new_sequence)) <= 1:
                break
        sequences[-1].append(sequences[-1][0])
        sequences.reverse()
        for index in range(len(sequences) - 1):
            # Modifying sequences[index + 1]
            sequences[index + 1].append(sequences[index][-1] + sequences[index + 1][-1])

        sum += sequences[-1][-1]
    print(sum)
