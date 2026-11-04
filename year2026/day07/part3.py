import re
from collections import defaultdict

graph = {}
energies0 = {}
threshold = 1000000

for line in open(0).read().splitlines():
    id, energy, *conns = map(int, re.findall(r"\d+", line))
    energies0[id] = energy
    graph[id] = conns

def solve(target):
    energies = energies0.copy()
    impulses = {target: {10: 1}}
    while impulses:
        new_impulses = defaultdict(lambda: defaultdict(int))

        for cloud, charges in impulses.items():
            if cloud not in energies:
                continue
            for strength, count in charges.items():
                energies[cloud] += strength * count
                if strength > 1:
                    for conn in graph[cloud]:
                        new_impulses[conn][strength - 1] += count

        exploded = [cloud for cloud, energy in energies.items() if energy >= threshold]
        for cloud in exploded:
            del energies[cloud]
            for conn in graph[cloud]:
                if conn in energies:
                    new_impulses[conn][10] += 1

        impulses = new_impulses

    return sum(energies.values())

print(max(solve(id) for id in graph))
