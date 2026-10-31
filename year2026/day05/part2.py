from part1 import *

grid = [[x if x == "#" else "." for x in row] for row in grid]

while True:
    progress = False
    new_grid = [row[:] for row in grid]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "#":
                continue

            if r in (0, rows - 1) or c in (0, cols - 1):
                new_grid[r][c] = "="
                progress = True
                continue

            adj = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if grid[nr][nc] == ".":
                    new_grid[r][c] = "="
                    progress = True
                if grid[nr][nc] == "=":
                    adj += 1

            if adj >= 5:
                new_grid[r][c] = "="
                progress = True

    grid = new_grid
    if not progress:
        break

if __name__ == "__main__":
    print(sum(x == "=" for row in grid for x in row))
