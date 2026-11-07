from collections import defaultdict

grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

ghosts = defaultdict(list)
for r in range(rows):
    for c in range(cols):
        directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
        if grid[r][c] in directions:
            ghosts[(r, c)].append(directions[grid[r][c]])

collisions = 0

for round in range(10):
    new_ghosts = defaultdict(list)

    for (r, c), dirs in ghosts.items():
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] == "#":
                new_ghosts[(r, c)].append((dc, -dr))
                collisions += 1
            else:
                new_ghosts[(nr, nc)].append((dr, dc))

    for (r, c), dirs in new_ghosts.items():
        if len(dirs) > 1:
            new_ghosts[(r, c)] = [(-dr, -dc) for dr, dc in dirs]
            collisions += len(dirs)

    ghosts = new_ghosts

print(collisions)
