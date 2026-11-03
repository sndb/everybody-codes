from collections import defaultdict

used_in = defaultdict(set)

for line in open(0).read().splitlines():
    prod, ings = line[:4], line[5:].split(",")
    for ing in ings:
        used_in[ing].add(prod)

def all_users(ing):
    seen = set()
    queue = [ing]
    while queue:
        item = queue.pop()
        if item not in seen:
            seen.add(item)
            queue.extend(used_in[item])
    return seen

n1 = all_users("NULLv1")
n2 = all_users("NULLv2")
n3 = all_users("NULLv3")

print(len(n1 & n2 | n1 & n3 | n2 & n3))
