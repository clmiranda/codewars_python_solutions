# Product of the main diagonal of a square matrix => https://www.codewars.com/kata/551204b7509063d9ba000b45

import math


def main_diagonal_product(mat) -> int:
    return math.prod([j[i] for i, j in enumerate(mat)])
