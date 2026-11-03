ingredients = {}

for line in open(0).read().splitlines():
    prod, ings = line[:4], line[5:].split(",")
    ingredients[prod] = ings

seen = set()
queue = ["NULL"]
while queue:
    prod = queue.pop()
    if prod not in seen:
        seen.add(prod)
        queue.extend(ingredients.get(prod, []))

print(len(seen - {"NULL"}))
