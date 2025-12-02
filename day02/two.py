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
        for j in range(half, 0, -1):
            if len(str(i)) % j != 0:
                continue
            num = int(len(str(i)) / j)
            test = str(i)[0:j] * num
            if str(i) == test:
                total += i
                break

print(total)
        