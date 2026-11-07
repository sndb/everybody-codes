from collections import defaultdict

limit = 10000
grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

ghosts = defaultdict(list)
for r in range(rows):
    for c in range(cols):
        directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
        if grid[r][c] in directions:
            ghosts[(r, c)].append((*directions[grid[r][c]], 0))

round = 0

while ghosts:
    new_ghosts = defaultdict(list)

    for (r, c), dirs in ghosts.items():
        for dr, dc, cs in dirs:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] == "#":
                if cs + 1 < limit:
                    new_ghosts[(r, c)].append((dc, -dr, cs + 1))
            else:
                new_ghosts[(nr, nc)].append((dr, dc, cs))

    for (r, c), dirs in new_ghosts.items():
        if len(dirs) > 1:
            dirs = [(-dr, -dc, cs + 1) for dr, dc, cs in dirs if cs + 1 < limit]
            new_ghosts[(r, c)] = dirs

    ghosts = new_ghosts
    round += 1

print(round)
