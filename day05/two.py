import sys


input = []
inventory = []
total = 0

for line in sys.stdin:
    if line == "\n":
        break
    else:
        input.append(list(map(int, line.strip().split("-"))))

for fresh in input:
    inventory.append(range(fresh[0], fresh[1]+1))
    
inventory = sorted(inventory, key=lambda x: x.start)
merged = []

for item in inventory:
    if len(merged) < 1:
        merged.append(item)
        continue
    if item.start in merged[-1] and item.stop - 1 in merged[-1]:
        continue
    
    if item.start in merged[-1] and item.stop - 1 not in merged[-1]:
        merged[-1] = range(merged[-1].start, item.stop)
    elif item.start not in merged[-1]:
        merged.append(item)
        
for item in merged:
    total += len(item)
    
print("answer:", total)