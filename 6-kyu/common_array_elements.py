# Common array elements => https://www.codewars.com/kata/5a6225e5d8e145b540000127

from collections import Counter


def common(a: list[int], b: list[int], c: list[int]) -> int:
    common_values = Counter(a) & Counter(b) & Counter(c)
    return sum(key * value for key, value in common_values.items())
