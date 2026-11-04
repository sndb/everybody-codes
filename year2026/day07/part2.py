import re
from collections import defaultdict

graph = {}
energies = {}

for line in open(0).read().splitlines():
    id, energy, *conns = map(int, re.findall(r"\d+", line))
    energies[id] = energy
    graph[id] = conns

target = max(graph, key=lambda k: len(graph[k]))

impulses = {target: {10: 1}}
while impulses:
    new_impulses = defaultdict(lambda: defaultdict(int))

    for cloud, charges in impulses.items():
        for strength, count in charges.items():
            energies[cloud] += strength * count
            if strength > 1:
                for conn in graph[cloud]:
                    new_impulses[conn][strength - 1] += count

    impulses = new_impulses

print(sum(energies.values()))
