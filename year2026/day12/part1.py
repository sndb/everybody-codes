grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

result = 0

for r in range(rows):
    for c in range(cols):
        if (
            grid[r][c] == "#"
            and (r == 0 or grid[r - 1][c] == ".")
            and (c == 0 or grid[r][c - 1] == ".")
        ):
            r_end, c_end = r, c
            while r_end < rows and grid[r_end][c] == "#":
                r_end += 1
            while c_end < cols and grid[r][c_end] == "#":
                c_end += 1
            result += min(r_end - r, c_end - c)

print(result)
