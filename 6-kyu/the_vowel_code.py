# The Vowel Code => https://www.codewars.com/kata/53697be005f803751e0015aa

vowels = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
digits = {v: k for k, v in vowels.items()}

def _translate(st: str, dct: dict):
    return "".join(dct.get(char, char) for char in st)

def encode(st: str):
    return _translate(st, vowels)

def decode(st: str):
    return _translate(st, digits)
