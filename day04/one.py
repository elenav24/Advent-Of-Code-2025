import sys

def check_adjacent_positions(grid, row, col):
    directions = [(-1, 0), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (0, -1), (-1, -1)]
    count = 0
    for direction in directions:
        i, j = direction[0] + row, direction[1] + col
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            continue
        
        if grid[i][j] == "@":
            count += 1
            
        if count >= 4:
            return 0
    return 1
        
        
total = 0
grid = []
for line in sys.stdin:
    grid.append(line.strip())


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            total += check_adjacent_positions(grid, i, j)
        
print("answer:", total)
    