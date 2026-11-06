from re import findall
from collections import defaultdict

def solve(growth, limit):
    time = 1
    leaves = 1
    branches = {1: 1}

    while leaves < limit:
        longest = max(branches.keys())
        delta = growth - longest

        new_branches = defaultdict(int)
        for length, count in branches.items():
            if length == longest:
                new_branches[1] = count
                new_branches[growth // 2] += 2 * count
                leaves += count
            else:
                new_branches[length + delta] += count

        branches = new_branches
        time += delta

    return time

total = 0

for line in open(0).read().splitlines():
    id, growth, limit = map(int, findall(r"\d+", line))
    total += solve(growth, limit)

print(total)
