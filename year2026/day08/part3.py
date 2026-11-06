lines = open(0).read().splitlines()
grid = [[x if x == "." else int(x) for x in line] for line in lines]
rows, cols = len(grid), len(grid[0])

def march(r, c, dr, dc):
    energy, warriors, shadow = 0, 0, 0
    while 0 <= r < rows and 0 <= c < cols:
        if grid[r][c] != ".":
            height = grid[r][c]
            if height > shadow:
                if grid[r][c] == 9:
                    grid[r][c] = -2
                    warriors += 1
                else:
                    grid[r][c] += 1
                shadow = height
                energy += 1
            if height < 1:
                grid[r][c] += 1
        shadow = max(shadow - 1, 0)
        r, c = r + dr, c + dc
    return energy, warriors

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

total, army, round = 0, 0, 0

while army < 100000:
    order = ((1, 1), (1, -1), (0, -2), (-1, -1), (-1, 1), (0, 2))
    dr, dc = order[round % len(order)]
    for r, c in starts(dr, dc):
        energy, warriors = march(r, c, dr, dc)
        total += energy
        army += warriors
    round += 1

print(total)
