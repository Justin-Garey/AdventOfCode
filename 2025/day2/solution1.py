

invalid_id_total = 0

with open("input1.in", "r") as f:
    line = f.readline().strip()
    segments = line.split(",")
    for segment in segments:
        product_ids = segment.split("-")
        ids_list = list(range(int(product_ids[0]), int(product_ids[1]) + 1))
        for product_id in ids_list:
            product_id = str(product_id)
            product_id_length = len(product_id)
            first_half = product_id[:product_id_length // 2]
            second_half = product_id[product_id_length // 2:]
            #print(f"Checking ID: {product_id}, First half: {first_half}, Second half: {second_half}")
            if product_id[:product_id_length // 2] == product_id[product_id_length // 2:]:
                invalid_id_total += int(product_id)
                #print(f"Invalid ID found: {product_id}")

print(invalid_id_total)