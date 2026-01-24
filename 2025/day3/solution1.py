
sum_joltage = 0

with open("input1.in", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        jolt1 = 0
        jolt2 = 0
        for char in line[:-1]:
            val = int(char)
            if val > jolt1:
                jolt1 = val
        jolt1_index = line.index(str(jolt1))
        for char in line[jolt1_index+1:]:
            val = int(char)
            if val > jolt2:
                jolt2 = val
        line_joltage = str(jolt1) + str(jolt2)
        #print(f"Line Joltage: {line_joltage}")
        sum_joltage += int(line_joltage)

print(f"Total Joltage: {sum_joltage}")