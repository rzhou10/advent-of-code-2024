import re

def part_one(file):
    with open(file, 'r') as f:
        txt_str = f.readlines()

    txt_str = list(map(lambda s : s.replace('\n', ''), txt_str))

    sum = 0

    for string in txt_str:
        # regex to find all mul(numbers in string)
        all_muls = re.findall("(mul\((\d+),(\d+)\))", string)
        for mul in all_muls:
            sum += int(mul[1]) * int(mul[2])

    return sum

def part_two(file):
    with open(file, 'r') as f:
        txt_str = f.readlines()

    txt_str = list(map(lambda s : s.replace('\n', ''), txt_str))

    # concatenate to single string so that instructions are not broken up
    input = ''.join(txt_str)

    sum = 0

    # regex to find all mul(numbers in string) and do's and don'ts
    all_muls = re.findall("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", input)

    calculate_mul = True

    for mul in all_muls:
        # if do() is before mul, then set calculate_mul to True to perform calculation
        if mul[0] == "do()":
            calculate_mul = True
        elif mul[0] == "don't()":
            calculate_mul = False
        elif calculate_mul:
            sum += int(mul[1]) * int(mul[2])

    return sum