

accessible_rolls = 0

warehouse_map = []

with open("input1.in", "r") as f:
    lines = f.readlines()
    line_number = 0
    for line in lines:
        map_row = []
        for char in line.strip():
            if char == ".":
                map_row.append(0)
            else:
                map_row.append(1)
        warehouse_map.append(map_row)
        line_number += 1

def accessible_roll(row_index, column_index):
    rolls = 0
    # Check top left
    if row_index > 0 and column_index > 0:
        if warehouse_map[row_index - 1][column_index - 1] == 1:
            rolls += 1
    # Check top
    if row_index > 0:
        if warehouse_map[row_index - 1][column_index] == 1:
            rolls += 1
    # Check top right
    if row_index > 0 and column_index < len(warehouse_map[row_index]) - 1:
        if warehouse_map[row_index - 1][column_index + 1] == 1:
            rolls += 1
    # Check left
    if column_index > 0:
        if warehouse_map[row_index][column_index - 1] == 1:
            rolls += 1
    # Check right
    if column_index < len(warehouse_map[row_index]) - 1:
        if warehouse_map[row_index][column_index + 1] == 1:
            rolls += 1
    # Check bottom left
    if row_index < len(warehouse_map) - 1 and column_index > 0:
        if warehouse_map[row_index + 1][column_index - 1] == 1:
            rolls += 1
    # Check bottom
    if row_index < len(warehouse_map) - 1:
        if warehouse_map[row_index + 1][column_index] == 1:
            rolls += 1
    # Check bottom right
    if row_index < len(warehouse_map) - 1 and column_index < len(warehouse_map[row_index]) - 1:
        if warehouse_map[row_index + 1][column_index + 1] == 1:
            rolls += 1
    if rolls < 4:
        return True
    return False

while True:
    updated_warehouse_map = [row[:] for row in warehouse_map]
    for row_index in range(len(warehouse_map)):
        for column_index in range(len(warehouse_map[row_index])):
            if warehouse_map[row_index][column_index] == 1:
                if accessible_roll(row_index, column_index):
                    accessible_rolls += 1
                    updated_warehouse_map[row_index][column_index] = 0
    if updated_warehouse_map == warehouse_map:
        break
    warehouse_map = updated_warehouse_map



print(f"Total Accessible Rolls: {accessible_rolls}")