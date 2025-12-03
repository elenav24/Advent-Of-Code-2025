import sys

batteries = []
total = 0
for line in sys.stdin:
    batteries.append([int(x) for x in line.strip()])
    
for line in batteries:
    maximum = max(line)
    index = line.index(maximum)
    first = None
    if index == len(line) - 1:
        temp = line[:len(line)-1]
        first = max(temp)
    else:
        second = max(line[index+1:])
    
    if first:
        joltage = int(str(first) + str(maximum))
    else:
        joltage = int(str(maximum) + str(second))
        
    total += joltage
    
print("answer:", total)