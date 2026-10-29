def digits(str):
    return [int(x) for x in reversed(str)]

result = 0

for line in open(0).read().splitlines():
    a, b = line[4:].split()
    iso = digits(a)
    num = digits(b)

    r = 0
    for i, x in enumerate(num):
        r += x * iso[i % len(iso)] ** i
    result += r

print(result)
