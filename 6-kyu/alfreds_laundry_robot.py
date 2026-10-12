# Alfred's Laundry Robot => https://www.codewars.com/kata/583d704a70407fcb43000443


def path_finding(path: str) -> bool:
    MOVES = {"n": (0, 1), "s": (0, -1), "e": (1, 0), "w": (-1, 0)}
    posi = [
        (sum(MOVES[s][0] for s in route), sum(MOVES[s][1] for s in route))
        for route in (path, "eneen", "wnwnwwn")
    ]
    return posi[0] in posi[1:]
