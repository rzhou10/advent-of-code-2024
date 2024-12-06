import numpy as np

def part_one(file):
    with open(file, 'r') as f:
        grid = f.readlines()
    
    grid = list(map(lambda s : list(s.replace('\n', '')), grid))

    # use numpy to search for "^" in matrix, and then get indexes
    ls = np.array(grid)
    index = np.where(ls == "^")

    index_row = index[0][0]
    index_col = index[1][0]

    # keep track of which direction we want to go in
    direction_tracker = {"go_up": True, "go_down": False, "go_left": False, "go_right": False}
    # keep track of coordinates we've already passed so they aren't double counted
    # the number of unique coords is the number of squares walked
    passed_coordinates = set()

    # increment or decrement, rotating right if we hit "#"
    while True:
        print(f"We are at {[index_row]}, {[index_col]}; Count: {len(passed_coordinates)}")
        # if we hit the edges of the matrix 
        if (index_row == 0 or index_row == len(grid) - 1) or (index_col == 0 or index_row == len(grid[0]) - 1):
            break
        if direction_tracker["go_up"]:
            if index_row - 1 >= 0 and grid[index_row - 1][index_col] == "#":
                direction_tracker["go_up"] = False
                direction_tracker["go_right"] = True
            else:
                index_row -= 1

                if f"{index_row}, {index_col}" not in passed_coordinates:
                    passed_coordinates.add(f"{index_row}, {index_col}")
        elif direction_tracker["go_down"]:
            if index_row + 1 <= len(grid) - 1 and grid[index_row + 1][index_col] == "#":
                direction_tracker["go_down"] = False
                direction_tracker["go_left"] = True

            else:
                index_row += 1

                if f"{index_row}, {index_col}" not in passed_coordinates:
                    passed_coordinates.add(f"{index_row}, {index_col}")

        elif direction_tracker["go_left"]:
            if index_col - 1 >= 0 and grid[index_row][index_col - 1] == "#":
                direction_tracker["go_left"] = False
                direction_tracker["go_up"] = True

            else:
                index_col -= 1

                if f"{index_row}, {index_col}" not in passed_coordinates:
                    passed_coordinates.add(f"{index_row}, {index_col}")

        elif direction_tracker["go_right"]:
            if index_col + 1 <= len(grid[0]) - 1 and grid[index_row][index_col + 1] == "#":
                direction_tracker["go_right"] = False
                direction_tracker["go_down"] = True
            else:
                index_col += 1

                if f"{index_row}, {index_col}" not in passed_coordinates:
                    passed_coordinates.add(f"{index_row}, {index_col}")

    return len(passed_coordinates)