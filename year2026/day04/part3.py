from collections import defaultdict
import itertools
import re

final_rankings = defaultdict(int)  # id -> points
finished_players = defaultdict(list)  # (quest, part) -> [id, ...]
completion_times = {}  # (id, quest, part) -> time

for line in open(0).read().splitlines():
    id, quest, part, time = map(int, re.findall(r"\d+", line))
    finished_players[quest, part].append(id)
    completion_times[(id, quest, part)] = time

for (quest, part), ids in finished_players.items():
    totals = []
    for id in ids:
        time = sum(completion_times[(id, quest, p + 1)] for p in range(part))
        totals.append((id, time))
    totals.sort(key=lambda x: x[1])

    reward = part * 50
    for _, window in itertools.groupby(totals, lambda x: x[1]):
        window = list(window)
        for id, _ in window:
            final_rankings[id] += reward
        reward -= len(window)
        if reward <= 0:
            break

checksum = 0
position = 1

for scores, group in itertools.groupby(reversed(sorted(final_rankings.values()))):
    size = len(list(group))
    checksum += size * scores * position
    position += size

print(checksum)
