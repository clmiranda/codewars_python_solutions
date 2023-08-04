# Find the odd int => https://www.codewars.com/kata/54da5a58ea159efa38000836

from collections import Counter


def find_it(seq: list):
    return list(filter(lambda x: x[1] % 2 == 1, Counter(seq).items()))[0][0]
