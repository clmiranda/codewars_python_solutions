# Ordered Count of Characters => https://www.codewars.com/kata/57a6633153ba33189e000074

def ordered_count(inp: str) -> list:
    return [(x, inp.count(x)) for x in dict.fromkeys(inp)]