import sys

total = 0
i = 0
nums = []
operations = []
for line in sys.stdin:
    for char in line.strip():
        if char == ' ':
            continue
        if char in ['+', '*']:
            operations.append(char)
        else:
            nums.append(list(map(int, line.split())))
            break

for col in range(len(operations)):
    count = 0
    for row in range(len(nums)):
        if operations[col] == "*":
            if count == 0:
                count += nums[row][col]
            else:
                count *= nums[row][col]
        else:
            count += nums[row][col]
    total += count
    
print("answer:", total)