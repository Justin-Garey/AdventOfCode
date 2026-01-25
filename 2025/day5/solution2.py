fresh_ingredients = 0

ranges = []

saved_ranges = []

def add_range(new_start, new_end):
    #print(f"Saved ranges before adding: {saved_ranges}")
    if saved_ranges == []:
        saved_ranges.append((new_start, new_end))
        #print(f"Adding first range {new_start}-{new_end}")
        return
    for saved_range in saved_ranges:
        # If new range starts in saved range
        if saved_range[0] <= new_start <= saved_range[1]:
            # If new range ends in saved range, do nothing
            if saved_range[0] <= new_end <= saved_range[1]:
                return
            # Else: new range extends past saved range
            else:
                # Extend saved range to end of new range
                saved_ranges.remove(saved_range)
                add_range(saved_range[0], new_end)
                #print(f"Extending range {saved_range[0]}-{saved_range[1]} to {saved_range[0]}-{new_end}")
                return

        # If new range ends within existing range, extend to beginning of new range
        elif saved_range[0] <= new_end <= saved_range[1]:
            saved_ranges.remove(saved_range)
            add_range(new_start, saved_range[1])
            #print(f"Extending range {saved_range[0]}-{saved_range[1]} to {new_start}-{saved_range[1]}")
            return

        # If new range contains existing range, switch to new range
        elif new_start <= saved_range[0] and new_end >= saved_range[1]:
            saved_ranges.remove(saved_range)
            add_range(new_start, new_end)
            #print(f"Replacing range {saved_range[0]}-{saved_range[1]} with {new_start}-{new_end}")
            return

    else:
        #print(f"Adding new range {new_start}-{new_end}")
        saved_ranges.append((new_start, new_end))

with open("input1.in", "r") as f:
    lines = f.readlines()
    for line in lines:
        if '-' in line:
            line_range = line.strip().split('-')
            start = int(line_range[0])
            end = int(line_range[1])
            ranges.append((start, end))

for start, end in ranges:
    add_range(start, end)

for range_pair in saved_ranges:
    start, end = range_pair
    fresh_ingredients += (end - start + 1)

print(f"Total Fresh Ingredients: {fresh_ingredients}")