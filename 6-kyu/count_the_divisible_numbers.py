# Count the divisible numbers => https://www.codewars.com/kata/55a5c82cd8e9baa49000004c


def divisible_count(x: int, y: int, k: int) -> int:
    return y // k - (x - 1) // k
