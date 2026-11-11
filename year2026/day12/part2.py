grid = open(0).read().splitlines()
cells = {(r, c) for r, row in enumerate(grid) for c, x in enumerate(row) if x == "#"}

def spells(shape: set[tuple[int, int]]):
    h_merges = {(r, c) for r, c in shape if (r, c + 1) in shape}
    v_merges = {(r, c) for r, c in shape if (r + 1, c) in shape}
    v_to_h = {}

    def pair(h, seen):
        r, c = h
        for v in ((r, c), (r - 1, c), (r, c + 1), (r - 1, c + 1)):
            if v in v_merges and v not in seen:
                seen.add(v)
                if v not in v_to_h or pair(v_to_h[v], seen):
                    v_to_h[v] = h
                    return True
        return False

    conflicts = sum(pair(h, set()) for h in h_merges)
    return len(shape) - (len(h_merges) + len(v_merges) - conflicts)

result = 0

while cells:
    shape = [cells.pop()]
    for r, c in shape:
        for n in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if n in cells:
                cells.remove(n)
                shape.append(n)
    result += spells(set(shape))

print(result)
