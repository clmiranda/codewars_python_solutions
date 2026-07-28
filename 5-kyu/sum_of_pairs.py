# Sum of Pairs => https://www.codewars.com/kata/54d81488b981293527000c8f

def sum_pairs(ints: list[int], s: int) -> list[int] | None:
    lst = set()
    for i in ints:
        if s - i in lst:
            return [s - i, i]
        lst.add(i)
    return None