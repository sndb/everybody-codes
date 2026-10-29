def value(iso, num):
    r = 0
    for i, x in enumerate(num):
        r += x * iso[i % len(iso)] ** i
    return r

def digits(str):
    return [int(x) for x in reversed(str)]

result = 0

for line in open(0).read().splitlines():
    a, b = line[5:].split()
    iso = digits(a)
    num = digits(b)

    r = value(iso, num)
    for i in range(int(b)):
        if value(iso, digits(str(i))) == r:
            break
    else:
        result += r

print(result)
