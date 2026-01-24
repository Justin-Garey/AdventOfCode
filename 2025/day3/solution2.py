
sum_joltage = 0

with open("input1.in", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line_joltage_string = ""
        starting_index = 0
        for i in range(12):
            jolt = 0
            end_index = -(12-(i+1)) if (12-(i+1)) > 0 else None
            for char in line[starting_index:end_index]:
                val = int(char)
                if val > jolt:
                    jolt = val
            line_joltage_string += str(jolt)
            starting_index = line.index(str(jolt), starting_index) + 1
        #print(f"Line Joltage String: {line_joltage_string}")
        sum_joltage += int(line_joltage_string)

print(f"Total Joltage: {sum_joltage}")