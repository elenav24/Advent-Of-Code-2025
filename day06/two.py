import sys

total = 0
i = 0
nums = []
operations = []
for line in sys.stdin:
    for char in line.strip():
        if char in ['+', '*']:
            operations.append(line)
            break
        else:
            nums.append(line.rstrip('\n'))
            break

count = 0
operation = ""
for i in range(len(nums[0])):
    if operations[0][i] in ['+', '*']:
        operation = operations[0][i]
        total += count
        count = 0
        
    temp = ""
    for row in range(len(nums)):
        if nums[row][i] != " ":
            temp += nums[row][i]
            
    if temp == "":
        continue
    
    if operation == "*":
        if count == 0:
            count += int(temp)
        else:
            count *= int(temp)
    else:
        count += int(temp)
    
total += count
    
print("answer:", total)