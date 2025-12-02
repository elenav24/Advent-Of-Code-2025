import sys
import math

rotations = []
for line in sys.stdin:
    rotations.append(line.strip())

index = 50
ans = 0
for x in rotations:
    turn = int(x[1:])
    prev = index
    if x[0] == "R":
        index += turn
    else:
        index -= turn
        
    if index % 100 == 0:
        if turn < 100:
            ans += 1
        else:
            ans += math.ceil(turn / 100)
        index = 0
        
    count = turn
        
    while index < 0:
        index += 100
        if count >= 100 or prev != 0:
            ans += 1
            count -= 100
        
    while index > 99:
        index -= 100
        if count >= 100 or prev != 0:
            ans += 1
            count -= 100
            
print(ans)