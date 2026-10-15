# The latest clock => https://www.codewars.com/kata/58925dcb71f43f30cd00005f

from itertools import permutations


def latest_clock(a: int, b: int, c: int, d: int) -> str:
    r = []
    for p in permutations([a, b, c, d]):
        h, m = p[0] * 10 + p[1], p[2] * 10 + p[3]
        if h <= 23 and m <= 59:
            r.append((h, m))
    h, m = max(r)
    return f"{h:02d}:{m:02d}"
