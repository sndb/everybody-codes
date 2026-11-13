grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

result = 2 * (rows + cols)

for r in range(rows):
    for c in range(cols):
        if c + 1 < cols and grid[r][c + 1] != grid[r][c]:
            result += 1
        if r + 1 < rows and grid[r + 1][c] != grid[r][c]:
            result += 1

print(result)
