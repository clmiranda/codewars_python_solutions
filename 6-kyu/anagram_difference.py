# Anagram difference => https://www.codewars.com/kata/5b1b27c8f60e99a467000041


def anagram_difference(w1: str, w2: str) -> int:
    return sum(abs(w1.count(char) - w2.count(char)) for char in set(w1 + w2))
