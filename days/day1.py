def part_one(file):
    with open(file, 'r') as f:
        txt_nums = f.readlines()

    txt_nums = list(map(lambda s : s.replace('\n', ''), txt_nums))

    first_nums = []
    second_nums = []
    for code in txt_nums:
        nums = code.split("   ")
        first_nums.append(int(nums[0]))
        second_nums.append(int(nums[1]))

    # sort the numbers
    first_nums = sorted(first_nums)
    second_nums = sorted(second_nums)
    list_of_differences = []

    # get the difference between the numbers at each point in the list
    for i in range(len(first_nums)):
        list_of_differences.append(abs(first_nums[i] - second_nums[i]))
    
    return list_of_differences

def part_two(file):
    with open(file, 'r') as f:
        txt_nums = f.readlines()

    txt_nums = list(map(lambda s : s.replace('\n', ''), txt_nums))

    first_nums = []
    second_nums = []
    for code in txt_nums:
        nums = code.split("   ")
        first_nums.append(int(nums[0]))
        second_nums.append(int(nums[1]))

    list_of_differences = []
    
    for num in first_nums:
        # filter the second list to get all instances of the number in the first lists
        instances = len([x for x in second_nums if x == num])
        list_of_differences.append(num * instances)
    
    return list_of_differences