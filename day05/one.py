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
    for item in inventory:
        if id in item:
            total += 1
            break
    
print("answer:", total)

# python one-line of part 1
print(len(set([id for id in [int(line.strip()) for line in open("in.txt") if len(line.strip()) > 0 and "-" not in line] for item in set([range(fresh[0], fresh[1]+1) for fresh in [list(map(int, line.strip().split("-"))) for line in open("in.txt") if "-" in line]]) if id in item])))

