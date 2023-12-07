#!/bin/python3

DEBUG = 0

with open("input1.in", "r") as file:
    solution = 1
    time = int("".join(file.readline().split(":")[1].strip().split()))
    best = int("".join(file.readline().split(":")[1].strip().split()))

    if DEBUG:
        print("Race Time: ", time)
        print("Race Distance: ", best)
    better_times = 0
    if time % 2 == 1:
        hold = time // 2
        current_distance = (time - hold) * hold
        while current_distance > best:
            better_times += 2
            hold -= 1
            current_distance = (time - hold) * hold
    else:
        hold = time / 2
        if ((time - hold) * hold) > best:
            better_times += 1
            hold -= 1
        current_distance = (time - hold) * hold
        while current_distance > best:
            better_times += 2
            hold -= 1
            current_distance = (time - hold) * hold
    if DEBUG:
        print(f"{better_times} better races than {best} mm in {time} ms")
    solution *= better_times
    print(solution)
