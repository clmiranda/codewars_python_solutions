# Multiples of 3 or 5 => https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number) -> int:
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)