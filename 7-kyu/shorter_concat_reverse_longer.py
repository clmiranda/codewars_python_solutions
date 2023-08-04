# shorter concat [reverse longer] => https://www.codewars.com/kata/54557d61126a00423b000a45


def shorter_reverse_longer(a, b):
    return f"{a}{b[::-1]}{a}" if len(a) < len(b) else f"{b}{a[::-1]}{b}"
