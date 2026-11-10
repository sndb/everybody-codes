lines = open(0).read().splitlines()
portals = int(lines[0].split()[1])
graph = [[] for _ in range(portals)]
for p in range(portals):
    for d in (-3, -2, -1, 1, 2, 3):
        graph[p].append((p + d) % portals)

def strain():
    total = 0
    for src in range(portals):
        step = 0
        queue = [src]
        seen = [False] * portals
        while queue:
            new_queue = []
            for p in queue:
                total += step
                for q in graph[p]:
                    if not seen[q]:
                        new_queue.append(q)
                        seen[q] = True
            queue = new_queue
            step += 1
    return total

def combinations(items):
    if not items:
        yield []
        return

    for i in range(1, len(items)):
        for rest in combinations(items[1:i] + items[i + 1 :]):
            yield [(items[0], items[i])] + rest

start = strain()

for line in lines[2:]:
    p, q = (int(x) - 1 for x in line.split())
    graph[p].append(q)
    graph[q].append(p)

answer = 0

for i in range(portals // 8):
    crystals = [i + portals // 8 * j for j in range(8)]
    for pairs in combinations(crystals):
        for p, q in pairs:
            graph[p].append(q)
            graph[q].append(p)
        answer = max(answer, start - strain())
        for p, q in pairs:
            del graph[p][-1]
            del graph[q][-1]

print(answer)
