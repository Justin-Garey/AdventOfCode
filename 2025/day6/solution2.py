sum_total = 0

columns = []

with open("input1.in", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.replace('\n', '')
        if columns == []:
            for i in range(len(line)):
                columns.append([])
        for i in range(len(line)):
            columns[i].append(line[i])

columns.reverse()
numbers = []

for col in columns:
    number_str = ''.join(col[:-1]).strip()
    if number_str.isdigit():
        numbers.append(int(number_str))
    if col[-1] == '+':
        for n in numbers:
            sum_total += n
        numbers = []
    elif col[-1] == '*':
        solution = 1
        for n in numbers:
            solution *= n
        sum_total += solution
        numbers = []

print(f"Sum Total: {sum_total}")