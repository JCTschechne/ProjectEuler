def rek(r, d):
    print(r, d)
    ret = 1 if r + d == 0 else 0
    if r > 0:
        ret += rek(r-1, d)
    if d > 0:
        ret += rek(r, d-1)
    return ret