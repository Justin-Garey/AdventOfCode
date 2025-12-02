START = 50
current = START
count_of_0 = 0

with open( "input.in", "r") as f:
    data = f.read().splitlines()
    for line in data:

        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            current -= distance
        elif direction == "R":
            current += distance
        
        while current < 0:
            current += 100
        while current >= 100:
            current -= 100

        if current == 0:
            count_of_0 += 1

print("Total count of positions ending with 0:", count_of_0)