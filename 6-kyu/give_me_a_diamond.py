# Give me a Diamond => https://www.codewars.com/kata/5503013e34137eeeaa001648

def diamond(n: int) -> str | None:
    if n <= 0 or n % 2 == 0:
        return None
    widths = list(range(1, n + 1, 2)) + list(range(n - 2, 0, -2))
    return ''.join([' ' * ((n - i) // 2) + '*' * i + '\n' for i in widths])