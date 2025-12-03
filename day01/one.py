import sys

rotations = []
for line in sys.stdin:
    rotations.append(line.strip())

index = 50
ans = 0
for x in rotations:
    if x[0] == "R":
        index += int(x[1:])
    else:
        index -= int(x[1:]) 
    
    if index % 100 == 0:
        ans += 1
            
print("answer:", ans)
    
