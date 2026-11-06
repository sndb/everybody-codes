grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

def starts():
    yield from ((r, 0) for r in range(rows))
    yield from ((0, c) for c in range(1, cols))

energy = 0

for r, c in starts():
    shadow = 0
    while r < rows and c < cols:
        if grid[r][c] != ".":
            height = int(grid[r][c])
            if height > shadow:
                shadow = height
                energy += 1
        r, c = r + 1, c + 1
        shadow -= 1

print(energy)
