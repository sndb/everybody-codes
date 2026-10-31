from part2 import *

pattern = [
    (dr, dc)
    for dr in (-2, -1, 0, 1, 2)
    for dc in (-2, -1, 0, 1, 2)
    if dr not in (-2, 2) or dc not in (-2, 2)
]

for r in range(2, rows - 2):
    for c in range(2, cols - 2):
        for dr, dc in pattern:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] not in ("#", "@"):
                break
        else:
            grid[r][c] = "@"

for _ in range(2):
    new_grid = [row[:] for row in grid]

    for r in range(2, rows - 2):
        for c in range(2, cols - 2):
            trees = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if grid[nr][nc] == "=":
                    break
                if grid[nr][nc] == "@":
                    trees += 1
            else:
                if trees >= 4:
                    new_grid[r][c] = "@"

    grid = new_grid

if __name__ == "__main__":
    print(sum(x == "@" for row in grid for x in row))
