# Consonant value => https://www.codewars.com/kata/59c633e7dcc4053512000073

import re, string


def solve(value):
    return max(
        sum(string.ascii_lowercase.index(x) + 1 for x in y)
        for y in re.split("a|e|i|o|u", value)
    )
