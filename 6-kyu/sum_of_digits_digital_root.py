# Sum of Digits / Digital Root => https://www.codewars.com/kata/541c8630095125aba6000c00


def digital_root(num):
    result = sum([int(i) for i in str(num)])
    return result if result < 10 else digital_root(result)
