# Find the next perfect square! => https://www.codewars.com/kata/56269eb78ad2e4ced1000013


def find_next_square(sq):
    return (int(pow(sq, 0.5)) + 1) ** 2 if str(pow(sq, 0.5))[-1] == "0" else -1
