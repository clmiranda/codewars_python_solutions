# Take a Ten Minutes Walk => https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk: list[str]) -> bool:
    return walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e') and len(walk) == 10