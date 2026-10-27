result = 0
side = 3

for c in map(int, open(0).read().split(",")):
    while True:
        r = 2 * side + 2 * (side - 2)
        if c > r:
            side += 1
        else:
            result += r - c
            break

print(result)
