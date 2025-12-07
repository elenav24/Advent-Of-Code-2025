import sys
from functools import lru_cache

input = []
count = 0
for line in sys.stdin:
    input.append(line.strip())
    
@lru_cache(None)
def recursion(row, col):
    total = 0
    i = row + 1
        
    while i < len(input) and input[i][col] != "^":
        i += 1

    if i >= len(input):
        return 1 

    if col-1 >= 0:
        total += recursion(i, col-1)
    if col+1 < len(input[0]):
        total += recursion(i, col+1)

    return total

row, col = 1, input[0].index('S')
total = recursion(row, col)
print("answer:", total)

