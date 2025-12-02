START = 50
current = START
count_of_0 = 0

with open( "input.in", "r") as f:
    data = f.read().splitlines()
    for line in data:

        direction = line[0]
        distance = int(line[1:])

        current_start = current

        count_of_0 += distance // 100
        distance = distance % 100

        if direction == "L":
            current -= distance
        elif direction == "R":
            current += distance

        if current < 0:
            current += 100
            if current_start != 0:
                count_of_0 += 1
        
        if current == 0 and current_start != 0:
            count_of_0 += 1


        if current >= 100:
            count_of_0 += 1
            current -= 100        

print("Total count of passes of 0:", count_of_0)