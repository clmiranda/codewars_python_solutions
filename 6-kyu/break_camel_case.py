# Break camelCase => https://www.codewars.com/kata/5208f99aee097e6552000148

import re


def solution(string: str) -> str:
    return " ".join(re.findall("[a-zA-Z][^A-Z]*", string))
