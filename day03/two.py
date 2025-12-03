import sys

batteries = []
total = 0
for line in sys.stdin:
    batteries.append([int(x) for x in line.strip()])
    
for line in batteries:
    maximum = max(line[:-11])
    max_index = line.index(maximum)
    temp = [maximum]
    temp.extend(line[max_index+1:])
    final = []
    i = 11
    
    while len(final) < 12:
        if i == 0:
            maximum = max(temp)
        else:
            maximum = max(temp[:-i])
        final.append(maximum)
        index = temp.index(maximum)
        temp = temp[index+1:]
        i -= 1
        
    final = [str(x) for x in final]
    num_str = "".join(final)
    total += int(num_str)
    
print("answer:", total)