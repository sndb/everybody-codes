import math

cones = map(int, open(0).read().split(","))
print(sum(math.ceil(math.sqrt(c)) ** 2 - c for c in cones))
