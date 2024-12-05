def part_one(file):
    with open(file, 'r') as f:
        txt_nums = f.readlines()

    txt_nums = list(map(lambda s : s.replace('\n', ''), txt_nums))

    valid_reports = 0
    for report in txt_nums:
        nums = list(map(int, report.split(" ")))

        if calc_bad_nums(nums):
            valid_reports += 1

    return valid_reports

def part_two(file):
    with open(file, 'r') as f:
        txt_nums = f.readlines()

    txt_nums = list(map(lambda s : s.replace('\n', ''), txt_nums))

    valid_reports = 0
    counter = 1

    for report in txt_nums:
        nums = list(map(int, report.split(" ")))
        length = len(nums) - 1
        removed_bad_number = False

        for i in range(length):
            # check if the element is not within the range for  
            if not (1 <= abs(nums[i] - nums[i + 1]) <= 3):
                nums.pop(i + 1)
                removed_bad_number = True
                break

        if not removed_bad_number:
            length -= 1
            # check if the element is not either strictly increasing or decreasing
            for i in range(length):
                if not (nums[i] < nums[i + 1] < nums[i + 2] or nums[i] > nums[i + 1] > nums[i + 2]):
                    nums.pop(i + 1)
                    break

        if calc_bad_nums(nums):
            print("valid report!")
            print(f"counter: {counter}")
            valid_reports += 1
        counter += 1
    
    return valid_reports

# helper function to calculate the conditions
def calc_bad_nums(nums):

    # check if all increasing
    is_increasing = all(i < j for i, j in zip(nums, nums[1:]))
    is_decreasing = all(i > j for i, j in zip(nums, nums[1:]))
    is_safe_levels = True

    length = len(nums) - 1

    for i in range(length):
        if not (1 <= abs(nums[i] - nums[i + 1]) <= 3):
            is_safe_levels = False
            break
            
    return (is_increasing or is_decreasing) and is_safe_levels