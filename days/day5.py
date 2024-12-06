def part_one(file_ordering, file_updates):
    with open(file_ordering, 'r') as f:
        order_str = f.readlines()
    
    order_str = list(map(lambda s : s.replace('\n', ''), order_str))

    with open(file_updates, 'r') as f:
        updates_str = f.readlines()
    
    updates_str = list(map(lambda s : s.replace('\n', ''), updates_str))

    sum = 0

    for update in updates_str:
        # convert to ints
        update_list = list(map(int, update.split(",")))

        # create index map with the position that the number is at
        index_map = {index: i for i, index in enumerate(update_list)}
        valid_list = True
        print(index_map)

        # iterate over ordering and check if the numbers exist and in the right order
        for order in order_str:
            [x, y] = list(map(int, order.split("|")))
            print(f"x: {x}")
            print(f"y: {y}")
            if x in index_map and y in index_map and index_map[x] > index_map[y]:
                valid_list = False
                break
        # if valid_list:
        if valid_list:
            middle = update_list[len(update_list) // 2]
            sum += middle

    return sum