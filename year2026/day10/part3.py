from collections import defaultdict
from math import inf

limit = 1000000000000
grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

ghosts = defaultdict(list)
for r in range(rows):
    for c in range(cols):
        directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
        if grid[r][c] in directions:
            ghosts[(r, c)].append((*directions[grid[r][c]], 0))

def hash(ghosts):
    h = []
    for (r, c), dirs in ghosts.items():
        h.append(((r, c), tuple(sorted((dr, dc) for dr, dc, _ in dirs))))
    return tuple(sorted(h))

def maximize(g1, g2):
    q = inf
    for k in g1:
        for (_, _, cs0), (_, _, cs1) in zip(g1[k], g2[k]):
            if (diff := cs1 - cs0) > 0:
                q = min(q, (limit - 1 - cs1) // diff)

    result = defaultdict(list)
    for k in g1:
        for (dx, dy, cs0), (_, _, cs1) in zip(g1[k], g2[k]):
            result[k].append((dx, dy, cs1 + (cs1 - cs0) * q))
    return result, q

round = 0
cache = {}

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
        new_ghosts[(r, c)] = sorted(dirs)

    ghosts = new_ghosts
    round += 1

    h = hash(ghosts)
    if h in cache:
        prev_round, prev_ghosts = cache[h]
        ghosts, q = maximize(prev_ghosts, ghosts)
        round += (round - prev_round) * q
        cache = {}
    cache[h] = (round, ghosts)

print(round)
