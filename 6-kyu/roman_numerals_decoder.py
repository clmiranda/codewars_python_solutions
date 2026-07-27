# Roman Numerals Decoder => https://www.codewars.com/kata/51b6249c4612257ac0000005

def solution(roman : str) -> int:
    symbols = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    n, index = 0, 0
    while index < len(roman):
        pair = roman[index:index + 2]
        if pair in symbols:
            n += symbols[pair]
            index += 2
        else:
            n += symbols[roman[index]]
            index += 1
    return n