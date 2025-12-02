import sys

input = []
for line in sys.stdin:
    input.append(line.strip())
    
ranges = [x.split(",") for x in input]
ranges = [x.split("-") for y in ranges for x in y]

total = 0
for x in ranges:
    for i in range(int(x[0]), int(x[1]) + 1):
        if i < 10:
            continue
        half = int(len(str(i)) / 2)
        if str(i)[0:half] == str(i)[half:]:
            total += int(i)

print(total)
        