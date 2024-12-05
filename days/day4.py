def part_one(file):
    with open(file, 'r') as f:
        txt_str = f.readlines()
    
    txt_str = list(map(lambda s : s.replace('\n', ''), txt_str))

    return check_xmas_str(txt_str)

# helper function to check for xmas str
def check_xmas_str(txt_str):
    count = 0

    for i in range(len(txt_str)):
        row_len = len(txt_str[i])
        is_valid_forward_i = (i + 1 < row_len and i + 2 < row_len and i + 3 < row_len)
        is_valid_up_i = (i + 1 < len(txt_str) and i + 2 < len(txt_str) and i + 3 < len(txt_str))
        is_valid_backward_i = (i - 1 >= 0 and i - 2 >= 0 and i - 3 >= 0)

        for j in range(row_len):
            # forward
            if is_valid_forward(j, row_len) and f"{txt_str[i][i]}{txt_str[i][j + 1]}{txt_str[i][j + 2]}{txt_str[i][j + 3]}" == "XMAS":
                count += 1
            # backward
            if is_valid_backward(j) and f"{txt_str[i][j]}{txt_str[i][j - 1]}{txt_str[i][j - 2]}{txt_str[i][j - 3]}" == "XMAS":
                count += 1
        # diagonal south east
        if is_valid_forward_i and is_valid_up_i and f"{txt_str[i][i]}{txt_str[i + 1][i + 1]}{txt_str[i + 2][i + 2]}{txt_str[i + 3][i + 3]}" == "XMAS":
            count += 1
        # diagonal north east
        if is_valid_up_i and is_valid_backward_i and f"{txt_str[i][i]}{txt_str[i + 1][i - 1]}{txt_str[i + 2][i - 2]}{txt_str[i + 3][i - 3]}" == "XMAS":
            
            count += 1
        # diagonal south west
        print(f"south west: {txt_str[i][i]}{txt_str[i - 1][i - 1]}{txt_str[i - 2][i - 2]}{txt_str[i - 3][i - 3]}")
        if is_valid_backward_i and f"{txt_str[i][i]}{txt_str[i - 1][i - 1]}{txt_str[i - 2][i - 2]}{txt_str[i - 3][i - 3]}" == "XMAS":
            
            count += 1
        # diagonal north west
        print(f"north west: {txt_str[i][i]}{txt_str[i - 1][i + 1]}{txt_str[i - 2][i + 2]}{txt_str[i - 3][i + 3]}")
        if is_valid_up_i and is_valid_backward_i and f"{txt_str[i][i]}{txt_str[i - 1][i + 1]}{txt_str[i - 2][i + 2]}{txt_str[i - 3][i + 3]}" == "XMAS":
            
            count += 1
        # up
        print(f"up: {txt_str[i][i]}{txt_str[i - 1][i]}{txt_str[i - 2][i]}{txt_str[i - 3][i]}")
        if is_valid_backward_i and f"{txt_str[i][i]}{txt_str[i - 1][i]}{txt_str[i - 2][i]}{txt_str[i - 3][i]}" == "XMAS":
            
            count += 1
        # down
        print(f"down: {txt_str[i][i]}{txt_str[i + 1][i]}{txt_str[i + 2][i]}{txt_str[i + 3][i]}")
        if is_valid_up_i and f"{txt_str[i][i]}{txt_str[i + 1][i]}{txt_str[i + 2][i]}{txt_str[i + 3][i]}" == "XMAS":
            
            count += 1
        print("--------------------")
    
    return count

def is_valid_forward(j, row_len):
    return j + 1 < row_len and j + 2 < row_len and j + 3 < row_len

def is_valid_backward(j):
    return j - 1 >= 0 and j - 2 >= 0 and j - 3 >= 0