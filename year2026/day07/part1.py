import re

graph = {}
energies = {}

for line in open(0).read().splitlines():
    id, energy, *conns = map(int, re.findall(r"\d+", line))
    energies[id] = energy
    graph[id] = conns

target = max(graph, key=lambda k: len(graph[k]))

def send_impulse(strength, cloud):
    if strength >= 1:
        energies[cloud] += strength
        for conn in graph[cloud]:
            send_impulse(strength - 1, conn)

send_impulse(5, target)
print(sum(energies.values()))
