# Pyramid Array => https://www.codewars.com/kata/515f51d438015969f7000013

def pyramid(n: int) -> list[list[int]]:
    return [[1] * (i) for i in range(1, n + 1)]