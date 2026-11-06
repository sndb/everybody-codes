from re import findall
from collections import defaultdict

def solve(growth, limit):
    time = 1
    points = 0
    branches = {1: 1}

    while points + sum(l * c for l, c in branches.items()) < limit:
        new_branches = defaultdict(int)
        for length, count in branches.items():
            if length == growth - 1:
                new_branches[1] = count
                new_branches[growth // 2] += 2 * count
                points += count
            else:
                new_branches[length + 1] += count

        branches = new_branches
        time += 1

    return time

total = 0

for line in open(0).read().splitlines():
    id, growth, limit = map(int, findall(r"\d+", line))
    total += solve(growth, limit)

print(total)
