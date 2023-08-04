# Bit Counting => https://www.codewars.com/kata/526571aae218b8ee490006f4


def count_bits(num):
    return "{0:08b}".format(num).count("1")
