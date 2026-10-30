import re

results = {}

for line in open(0).read().splitlines():
    id, quest, part, time = map(int, re.findall(r"\d+", line))
    results.setdefault(id, 0)
    results[id] += time

checksum = 0

for rank, result in enumerate(sorted(results.values())):
    checksum += (rank + 1) * result

print(checksum)
