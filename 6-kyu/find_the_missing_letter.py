# Find the missing letter => https://www.codewars.com/kata/5839edaa6754d6fec10000a2

def find_missing_letter(chars: list[str]) -> str:
    chars_iter = iter(chars)
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet[
        [x for x in range(alphabet.index(chars[0]), alphabet.index(chars[-1]))
            if alphabet[x] == next(chars_iter)][-1] + 1
    ]