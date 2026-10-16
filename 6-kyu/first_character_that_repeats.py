# first character that repeats => https://www.codewars.com/kata/54f9f4d7c41722304e000bbb

from collections import Counter


def first_dup(s: str) -> str | None:
    c = Counter(s)
    for i in s:
        if c[i] > 1:
            return i
    return None
