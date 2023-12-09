#!/bin/python3

DEBUG = 0

with open("input1.in", "r") as file:
    instructions = file.readline().strip()
    file.readline()
    node_map = {}
    for line in file.readlines():
        nodes = (
            line.replace("=", "")
            .replace("(", "")
            .replace(")", "")
            .replace(",", "")
            .split()
        )
        node_map[nodes[0]] = (nodes[1], nodes[2])
    steps = 0
    current_node = "AAA"
    instructions_length = len(instructions)
    while current_node != "ZZZ":
        next_move = instructions[steps % instructions_length]
        if DEBUG:
            print(
                f"Currently on step {steps} and node {current_node} with the next move being {next_move}"
            )
        if next_move == "L":
            next_node = node_map[current_node][0]
        else:
            next_node = node_map[current_node][1]
        steps += 1
        current_node = next_node
    print(steps)
