# Unique In Order => https://www.codewars.com/kata/54e6533c92449cc251001667

from itertools import groupby


def unique_in_order(iterable):
    return [
        "".join(j)[0] if type(iterable) == str else list(j)[0]
        for _, j in groupby(iterable)
    ]
