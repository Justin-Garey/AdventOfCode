

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

            multiples = []
            for i in range(1, product_id_length):
                if product_id_length % i == 0:
                    multiples.append(i)
            for multiple in multiples:
                segments = [product_id[i:i + multiple] for i in range(0, product_id_length, multiple)]
                if all(segment == segments[0] for segment in segments):
                    invalid_id_total += int(product_id)
                    #print(f"Invalid ID found: {product_id} with multiple {multiple}")
                    break
                    

print(invalid_id_total)