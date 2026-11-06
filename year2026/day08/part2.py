grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

def march(r, c, dr, dc):
    energy, shadow = 0, 0
    while 0 <= r < rows and 0 <= c < cols:
        if grid[r][c] != ".":
            height = int(grid[r][c])
            if height > shadow:
                shadow = height
                energy += 1
        r, c = r + dr, c + dc
        shadow -= 1
    return energy

def starts(dr, dc):
    mid = rows // 2
    match (dr, dc):
        case (1, 1):
            yield from ((r, 0) for r in range(rows))
            yield from ((0, c) for c in range(1, cols))
        case (1, -1):
            yield from ((r, cols - 1) for r in range(rows))
            yield from ((0, c) for c in range(cols - 1))
        case (0, -2):
            yield from ((r, cols - 1 - abs(mid - r)) for r in range(rows))
        case (0, 2):
            yield from ((r, abs(mid - r)) for r in range(rows))
        case (-1, 1):
            yield from ((r, 0) for r in range(rows))
            yield from ((rows - 1, c) for c in range(1, cols))
        case (-1, -1):
            yield from ((r, cols - 1) for r in range(rows))
            yield from ((rows - 1, c) for c in range(cols - 1))

total = 0

for dr, dc in ((1, 1), (1, -1), (0, -2), (-1, -1), (-1, 1), (0, 2)):
    for r, c in starts(dr, dc):
        total += march(r, c, dr, dc)

print(total)
