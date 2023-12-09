#!/bin/python3

import math

DEBUG = 0

with open("input1.in", "r") as file:
    instructions = file.readline().strip()
    file.readline()
    node_map = {}
    starting_nodes = []
    for line in file.readlines():
        nodes = (
            line.replace("=", "")
            .replace("(", "")
            .replace(")", "")
            .replace(",", "")
            .split()
        )
        node_map[nodes[0]] = (nodes[1], nodes[2])
        if nodes[0][-1] == "A":
            starting_nodes.append(nodes[0])
    instructions_length = len(instructions)
    if DEBUG:
        print("Starting Nodes:", starting_nodes)
    steps_bucket = []
    for current_node in starting_nodes:
        steps = 0
        instructions_length = len(instructions)
        while current_node[-1] != "Z":
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
        if DEBUG:
            print(steps)
        steps_bucket.append(steps)
    print(math.lcm(*steps_bucket))
