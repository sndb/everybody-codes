sum = 0

for line in open(0):
    graph = {}
    for order in line.split():
        a, x, b = order
        if x == ">":
            a, b = b, a
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, [])

    result = sorted(graph.keys(), key=lambda a: len(graph[a]))
    sum += int("".join(result))

print(sum)
