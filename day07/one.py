import sys
from copy import deepcopy

input = []
total = 0
for line in sys.stdin:
    input.append(line.strip())
    
route = []
route.append(input[0].index('S'))
for i in range(len(input)):
    if i == 0:
        continue
    
    copy = deepcopy(route)
    for index in copy:
        if input[i][index] != "^":
            continue
        else:
            temp = index
            if index-1 >= 0 and index-1 not in route:
                route.append(index-1)
            if index+1 < len(input[0]) and index+1 not in route:
                route.append(index+1)
            route.remove(index)
            total += 1
    
print("answer:", total)