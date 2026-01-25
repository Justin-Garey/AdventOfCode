total_splits = 0

mapped_paths = []

with open("input1.in", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        mapped_line = []
        skip_next = False
        for j in range(len(lines[i].strip())):
            if skip_next:
                skip_next = False
                continue
            if lines[i][j] == '.':
                if i > 0 and mapped_paths[i - 1][j].isdigit():
                    mapped_line.append(mapped_paths[i - 1][j])
                elif i > 0 and lines[i - 1][j] == 'S':
                    mapped_line.append('1')
                else:
                    mapped_line.append('.')
            elif lines[i][j] == 'S':
                mapped_line.append('S')
            else: # line character is '^'
                if i > 0 and (mapped_paths[i - 1][j].isdigit()):
                    above_count = int(mapped_paths[i - 1][j])
                    if mapped_line[-1].isdigit():
                        digit = mapped_line[-1]
                        mapped_line = mapped_line[:-1]
                        mapped_line.append(str(int(digit) + above_count))
                    else:
                        mapped_line = mapped_line[:-1]
                        mapped_line.append(str(above_count))
                    mapped_line.append('^')
                    if mapped_paths[i - 1][j+1].isdigit():
                        mapped_line.append(str(int(mapped_paths[i - 1][j+1]) + above_count))
                    else:
                        mapped_line.append(str(above_count))
                    skip_next = True
                    total_splits += 1
                else:
                    mapped_line.append('X')
        mapped_paths.append(mapped_line)

for line in mapped_paths:
    print(line) 


total_possible_paths = 0

for char in mapped_paths[-1]:
    if char.isdigit():
        total_possible_paths += int(char) 
    

print(f"Total Splits: {total_splits}")
print(f"Total Possible Paths: {total_possible_paths}")