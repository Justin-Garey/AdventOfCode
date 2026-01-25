fresh_ingredients = 0

ranges = []

with open("example1.in", "r") as f:
    lines = f.readlines()
    for line in lines:
        if '-' in line:
            line_range = line.strip().split('-')
            start = int(line_range[0])
            end = int(line_range[1])
            ranges.append((start, end))
        elif line.strip().isdigit():
            number = int(line.strip())
            for start, end in ranges:
                if start <= number <= end:
                    fresh_ingredients += 1
                    break

print(f"Total Fresh Ingredients: {fresh_ingredients}")