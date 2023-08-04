# Squares sequence => https://www.codewars.com/kata/5546180ca783b6d2d5000062


def squares(x, n):
    list_numbers = []
    for _ in range(n):
        list_numbers.append(x)
        x *= x
    return list_numbers
