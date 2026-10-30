import re

results = {}

for line in open(0).read().splitlines():
    id, quest, part, time = map(int, re.findall(r"\d+", line))
    parts_done, total_time = results.setdefault(id, (0, 0))
    results[id] = (parts_done + 1, total_time + time)

checksum = 0

for rank, (parts, time) in enumerate(sorted(results.values(), key=lambda x: (-x[0], x[1]))):
    checksum += (rank + 1) * time

print(checksum)
