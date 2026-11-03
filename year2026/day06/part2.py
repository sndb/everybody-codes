from collections import defaultdict

used_in = defaultdict(set)

for line in open(0).read().splitlines():
    prod, ings = line[:4], line[5:].split(",")
    for ing in ings:
        used_in[ing].add(prod)

seen = set()
queue = ["NULL"]
while queue:
    item = queue.pop()
    if item not in seen:
        seen.add(item)
        queue.extend(used_in[item])

print(len(seen - {"NULL"}))
