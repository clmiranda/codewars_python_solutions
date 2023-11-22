# Highest Rank Number in an Array => https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004

from collections import Counter


def highest_rank(arr) -> int:
    arr_counter = Counter(arr)
    v_max = max([x for x in arr_counter.values()])
    return max([x for x in filter(lambda v: arr_counter[v] == v_max, arr)])
