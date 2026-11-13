from collections import defaultdict

grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

graph = defaultdict(lambda: defaultdict(int))
for r, row in enumerate(grid):
    for c, u in enumerate(row):
        if r in (0, rows - 1):
            graph[u]["frame"] += 1
            graph["frame"][u] += 1
        if c in (0, cols - 1):
            graph[u]["frame"] += 1
            graph["frame"][u] += 1
        if r + 1 < rows and (v := grid[r + 1][c]) != u:
            graph[u][v] += 1
            graph[v][u] += 1
        if c + 1 < cols and (v := grid[r][c + 1]) != u:
            graph[u][v] += 1
            graph[v][u] += 1

parent = {u: u for u in graph}

def root(x):
    if parent[x] != x:
        parent[x] = root(parent[x])
    return parent[x]

edges = sorted(
    (w, u, v)
    for u, neighbors in graph.items()
    for v, w in neighbors.items()
)

result = 0
for w, u, v in edges:
    ru = root(u)
    rv = root(v)
    if ru != rv:
        parent[ru] = rv
        result += w
print(result)
