sum_total = 0

math_problems = []

with open("input1.in", "r") as file:
    lines = file.readlines()
    for line in lines:
        math_problems.append(line.strip().split())

for i in range(len(math_problems[0])):
    operator = math_problems[-1][i]
    column_solution = 0
    if operator == '+':
        for j in range(len(math_problems) - 1):
            column_solution += int(math_problems[j][i])
    elif operator == '*':
        column_solution = 1
        for j in range(len(math_problems) - 1):
            column_solution *= int(math_problems[j][i])
    sum_total += column_solution

print(f"Sum Total: {sum_total}")