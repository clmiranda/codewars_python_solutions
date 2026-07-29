# Caesar Cipher Helper => https://www.codewars.com/kata/526d42b6526963598d0004db

class CaesarCipher(object):
    def __init__(self, shift: int):
        self.shift = shift % 26

    def _shift(self, string: str, n: int) -> str:
        return ''.join(chr((ord(c) - 65 + n) % 26 + 65) if c.isalpha() else c
                       for c in string.upper())

    def encode(self, st: str) -> str:
        return self._shift(st, self.shift)
        
    def decode(self, st: str) -> str:
        return self._shift(st, -self.shift)