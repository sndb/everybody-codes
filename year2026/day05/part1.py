grid = [list(row) for row in open(0).read().splitlines()]
rows, cols = len(grid), len(grid[0])
grid[rows // 2][cols // 2] = "#"

dirs = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]

while True:
    progress = False
    new_grid = [row[:] for row in grid]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                continue

            adj = 0
            land = False
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] in ("1", "#"):
                    land |= grid[nr][nc] == "#"
                    adj += 1

            if land and adj >= 5:
                new_grid[r][c] = "#"
                progress = True

    grid = new_grid
    if not progress:
        break

if __name__ == "__main__":
    print(sum(x == "#" for row in grid for x in row))
