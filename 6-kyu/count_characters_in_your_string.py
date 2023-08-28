# Count characters in your string => https://www.codewars.com/kata/52efefcbcdf57161d4000091

from collections import Counter


def count(string: str) -> dict:
    return dict(Counter(string))
