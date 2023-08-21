# Persistent Bugger => https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
import math


def persistence(number: int) -> int:
    counter = 0
    while len(str(number)) > 1:
        number = math.prod(int(x) for x in str(number))
        counter += 1
    return counter
