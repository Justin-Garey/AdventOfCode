total_splits = 0

mapped_paths = []

with open("input1.in", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        mapped_line = ''
        skip_next = False
        for j in range(len(lines[i].strip())):
            if skip_next:
                skip_next = False
                continue
            if lines[i][j] == '.':
                if i > 0 and mapped_paths[i - 1][j] == '|':
                    mapped_line += '|'
                elif i > 0 and lines[i - 1][j] == 'S':
                    mapped_line += '|'
                else:
                    mapped_line += '.'
            elif lines[i][j] == 'S':
                mapped_line += 'S'
            else: # line character is '^'
                if i > 0 and (mapped_paths[i - 1][j] == '|' or lines[i - 1][j] == 'S'):
                    mapped_line = mapped_line[:-1] + '|'
                    mapped_line += '^'
                    mapped_line += '|'
                    skip_next = True
                    total_splits += 1
                else:
                    mapped_line += 'X'
        mapped_paths.append(mapped_line)

for line in mapped_paths:
    print(line) 

print(f"Total Splits: {total_splits}")