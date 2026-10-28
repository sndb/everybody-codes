sum = 0

for line in open(0):
    graph = {}
    for order in line.split():
        a, x, b = order
        if x == ">":
            a, b = b, a
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set())

    result = []

    def dfs(a):
        if a in result:
            return
        for b in graph[a]:
            dfs(b)
        result.append(a)

    for a in graph.keys():
        dfs(a)

    sum += int("".join(result))

print(sum)
