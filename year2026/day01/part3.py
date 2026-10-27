result = 0
side = 3

for c in map(int, open(0).read().split(",")):
    while True:
        r = side * side - 1
        if c > r or side % 2 == 0:
            side += 1
        else:
            result += r - c
            break

print(result)
