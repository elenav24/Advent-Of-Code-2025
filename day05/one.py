import sys


input = []
food = []
inventory = set()
check = False
total = 0

for line in sys.stdin:
    if line == "\n":
        check = True
        continue
    if check:   
        food.append(int(line.strip()))
    else:
        input.append(list(map(int, line.strip().split("-"))))
        

for fresh in input:
    inventory.add(range(fresh[0], fresh[1]+1))
    
for id in food:
    for range in inventory:
        if id in range:
            total += 1
            break
    
    
print("answer:", total)