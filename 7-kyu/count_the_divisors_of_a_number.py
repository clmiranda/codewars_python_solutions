# Count the divisors of a number => https://www.codewars.com/kata/542c0f198e077084c0000c2e


def divisors(n):
    return len([i for i in range(2, n) if n % i == 0]) + 2 if n > 1 else 1
