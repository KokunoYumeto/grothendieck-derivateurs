def band_table():
    names = ["1"] + ["x%d%d" % (i, j) for i in (0, 1) for j in (0, 1)]
    ix = {n: i for i, n in enumerate(names)}
    n = len(names)
    T = [[0] * n for _ in range(n)]
    for a in names:
        for b in names:
            if a == "1": c = b
            elif b == "1": c = a
            else: c = "x%s%s" % (a[1], b[2])
            T[ix[a]][ix[b]] = ix[c]
    return names, T
def p3_table():
    names = ["1"] + ["x%d%d" % (i, j) for i in (0, 1) for j in (0, 1)] + ["q", "r"]
    ix = {n: i for i, n in enumerate(names)}
    n = len(names)
    T = [[0] * n for _ in range(n)]
    for a in names:
        for b in names:
            if a == "1": c = b
            elif b == "1": c = a
            elif a[0] == "x" and b[0] == "x": c = "x%s%s" % (a[1], b[2])
            elif a[0] == "x": c = "x%s0" % a[1]
            elif b[0] == "x": c = b
            else: c = a
            T[ix[a]][ix[b]] = ix[c]
    return names, T
