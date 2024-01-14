import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()
    nums = np.sort(np.array([int(x) for x in lines[0].split(':')[1].strip().split(' ')]))
    converted = np.zeros((1, len(nums))).astype(np.int8)[0]
    for line in lines[2:]:
        if '-' in line or len(line) == 1:
            converted[:] = 0
        else:
            parsed_line = [int(x) for x in line.strip().split(' ')]
            mask = (nums >= parsed_line[1]) & (nums <= parsed_line[1]+parsed_line[2]-1) & (converted == 0)
            nums[mask] = parsed_line[0] + (nums[mask] - parsed_line[1])
            converted[mask] = 1
print(nums.min())