result = 0

for line in open(0).read().splitlines():
    iso, num = map(int, line[4:].split())

    r = 0
    for i in range(4):
        r += (num % 10) * (iso % 10) ** i
        iso //= 10
        num //= 10
    result += r

print(result)
